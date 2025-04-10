import json
import logging
from typing import Any, Union, Optional
from typing_extensions import override
from importlib.metadata import version

import tiktoken  # type: ignore
from wrapt import wrap_function_wrapper  # type: ignore

from payi.types import IngestUnitsParams
from payi.types.ingest_units_params import Units

from .instrument import _IsStreaming, _ProviderRequest, _PayiInstrumentor


class OpenAiInstrumentor:
    @staticmethod
    def is_azure(instance: Any) -> bool:
        from openai import AzureOpenAI, AsyncAzureOpenAI # type: ignore # noqa: I001

        return isinstance(instance._client, (AsyncAzureOpenAI, AzureOpenAI))

    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            from openai import OpenAI  # type: ignore #  noqa: F401  I001
            
            wrap_function_wrapper(
                "openai.resources.chat.completions",
                "Completions.create",
                chat_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "openai.resources.chat.completions",
                "AsyncCompletions.create",
                achat_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "openai.resources.embeddings",
                "Embeddings.create",
                embeddings_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "openai.resources.embeddings",
                 "AsyncEmbeddings.create",
                aembeddings_wrapper(instrumentor),
            )

        except Exception as e:
            logging.debug(f"Error instrumenting openai: {e}")
            return


@_PayiInstrumentor.payi_wrapper
def embeddings_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.openai",
        _OpenAiEmbeddingsProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
async def aembeddings_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return await instrumentor.achat_wrapper(
        "system.openai",
        _OpenAiEmbeddingsProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def chat_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.openai",
        _OpenAiChatProviderRequest(instrumentor),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_awrapper
async def achat_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return await instrumentor.achat_wrapper(
        "system.openai",
        _OpenAiChatProviderRequest(instrumentor),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

class _OpenAiEmbeddingsProviderRequest(_ProviderRequest):
    @override
    def process_synchronous_response(
        self,
        response: Any,
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:
        return process_chat_synchronous_response(response, self._ingest, log_prompt_and_response, self._estimated_prompt_tokens)

class _OpenAiChatProviderRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor)
        self._include_usage_added = False

    @override
    def process_chunk(self, chunk: Any) -> bool:
        model = model_to_dict(chunk)
        
        if "provider_response_id" not in self._ingest:
            response_id = model.get("id", None)
            if response_id:
                self._ingest["provider_response_id"] = response_id

        send_chunk_to_client = True

        usage = model.get("usage")
        if usage:
            add_usage_units(usage, self._ingest["units"], self._estimated_prompt_tokens)

            # If we aded "include_usage" in the request on behalf of the client, do not return the extra 
            # packet which contains the usage to the client as they are not expecting the data
            if self._include_usage_added:
                send_chunk_to_client = False

        return send_chunk_to_client

    @override
    def process_request(self, kwargs: Any) -> None: # noqa: ARG001
        messages = kwargs.get("messages", None)
        if not messages or len(messages) == 0:
            return
        
        estimated_token_count = 0 
        has_image = False

        try: 
            enc = tiktoken.encoding_for_model(kwargs.get("model")) # type: ignore
        except KeyError:
            enc = tiktoken.get_encoding("o200k_base") # type: ignore
        
        for message in messages:
            msg_has_image, msg_prompt_tokens = has_image_and_get_texts(enc, message.get('content', ''))
            if msg_has_image:
                has_image = True
                estimated_token_count += msg_prompt_tokens
        
        if has_image and estimated_token_count > 0:
            self._estimated_prompt_tokens = estimated_token_count

        stream: bool = kwargs.get("stream", False)
        if stream:
            add_include_usage = True

            stream_options: dict[str, Any] = kwargs.get("stream_options", None)
            if stream_options and "include_usage" in stream_options:
                add_include_usage = stream_options["include_usage"] == False

            if add_include_usage:
                kwargs['stream_options'] = {"include_usage": True}
                self._include_usage_added = True

    @override
    def process_synchronous_response(
        self,
        response: Any,
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:
        process_chat_synchronous_response(response, self._ingest, log_prompt_and_response, self._estimated_prompt_tokens)

def process_chat_synchronous_response(response: str, ingest: IngestUnitsParams, log_prompt_and_response: bool, estimated_prompt_tokens: Optional[int]) -> Any:
    response_dict = model_to_dict(response)

    add_usage_units(response_dict.get("usage", {}), ingest["units"], estimated_prompt_tokens)

    if log_prompt_and_response:
        ingest["provider_response_json"] = [json.dumps(response_dict)]

    if "id" in response_dict:
        ingest["provider_response_id"] = response_dict["id"]

    return None

def model_to_dict(model: Any) -> Any:
    if version("pydantic") < "2.0.0":
        return model.dict()
    if hasattr(model, "model_dump"):
        return model.model_dump()
    elif hasattr(model, "parse"):  # Raw API response
        return model_to_dict(model.parse())
    else:
        return model


def add_usage_units(usage: "dict[str, Any]", units: "dict[str, Units]", estimated_prompt_tokens: Optional[int]) -> None:
    input = usage["prompt_tokens"] if "prompt_tokens" in usage else 0
    output = usage["completion_tokens"] if "completion_tokens" in usage else 0
    input_cache = 0

    prompt_tokens_details = usage.get("prompt_tokens_details")
    if prompt_tokens_details:
        input_cache = prompt_tokens_details.get("cached_tokens", 0)
        if input_cache != 0:
            units["text_cache_read"] = Units(input=input_cache, output=0)

    input = _PayiInstrumentor.update_for_vision(input - input_cache, units, estimated_prompt_tokens)

    units["text"] = Units(input=input, output=output)

def has_image_and_get_texts(encoding: tiktoken.Encoding, content: Union[str, 'list[Any]']) -> 'tuple[bool, int]':
    if isinstance(content, str):
        return False, 0
    elif isinstance(content, list): # type: ignore
        has_image = any(item.get("type") == "image_url" for item in content)
        if has_image is False:
            return has_image, 0
        
        token_count = sum(len(encoding.encode(item.get("text", ""))) for item in content if item.get("type") == "text")
        return has_image, token_count