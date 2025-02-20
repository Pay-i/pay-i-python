import json
import logging
from typing import Any, Union
from importlib.metadata import version

import tiktoken  # type: ignore
from wrapt import wrap_function_wrapper  # type: ignore

from payi.types import IngestUnitsParams
from payi.types.ingest_units_params import Units

from .instrument import IsStreaming, PayiInstrumentor


class OpenAiInstrumentor:
    @staticmethod
    def is_azure(instance: Any) -> bool:
        from openai import AzureOpenAI, AsyncAzureOpenAI # type: ignore # noqa: I001

        return isinstance(instance._client, (AsyncAzureOpenAI, AzureOpenAI))

    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
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


@PayiInstrumentor.payi_wrapper
def embeddings_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.openai",
        None, # process_chat_chunk,
        None, # process_chat_request,
        process_ebmeddings_synchronous_response,
        IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@PayiInstrumentor.payi_wrapper
async def aembeddings_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return await instrumentor.achat_wrapper(
        "system.openai",
        None, # process_chat_chunk,
        None, # process_chat_request,
        process_ebmeddings_synchronous_response,
        IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@PayiInstrumentor.payi_wrapper
def chat_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.openai",
        process_chat_chunk,
        process_chat_request,
        process_chat_synchronous_response,
        IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

@PayiInstrumentor.payi_awrapper
async def achat_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return await instrumentor.achat_wrapper(
        "system.openai",
        process_chat_chunk,
        process_chat_request,
        process_chat_synchronous_response,
        IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

def process_ebmeddings_synchronous_response(response: str, ingest: IngestUnitsParams, log_prompt_and_response: bool, **kwargs: Any) -> Any: #  noqa: ARG001
    return process_chat_synchronous_response(response, ingest, log_prompt_and_response, **kwargs)

def process_chat_synchronous_response(response: str, ingest: IngestUnitsParams, log_prompt_and_response: bool, **kwargs: Any) -> Any: #  noqa: ARG001
    response_dict = model_to_dict(response)

    add_usage_units(response_dict.get("usage", {}), ingest["units"])

    if log_prompt_and_response:
        ingest["provider_response_json"] = [json.dumps(response_dict)]

    if "id" in response_dict:
        ingest["provider_response_id"] = response_dict["id"]

    return None

def process_chat_chunk(chunk: Any, ingest: IngestUnitsParams) -> None:
    model = model_to_dict(chunk)
    
    if "provider_response_id" not in ingest:
        response_id = model.get("id", None)
        if response_id:
            ingest["provider_response_id"] = response_id

    usage = model.get("usage")
    if usage:
        add_usage_units(usage, ingest["units"])


def model_to_dict(model: Any) -> Any:
    if version("pydantic") < "2.0.0":
        return model.dict()
    if hasattr(model, "model_dump"):
        return model.model_dump()
    elif hasattr(model, "parse"):  # Raw API response
        return model_to_dict(model.parse())
    else:
        return model


def add_usage_units(usage: "dict[str, Any]", units: "dict[str, Units]") -> None:
    input = usage["prompt_tokens"] if "prompt_tokens" in usage else 0
    output = usage["completion_tokens"] if "completion_tokens" in usage else 0
    input_cache = 0

    prompt_tokens_details = usage.get("prompt_tokens_details")
    if prompt_tokens_details:
        input_cache = prompt_tokens_details.get("cached_tokens", 0)
        if input_cache != 0:
            units["text_cache_read"] = Units(input=input_cache, output=0)

    input = PayiInstrumentor.update_for_vision(input - input_cache, units)

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

def process_chat_request(ingest: IngestUnitsParams, *args: Any, **kwargs: Any) -> None: # noqa: ARG001
    messages = kwargs.get("messages")
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
    
    if not has_image or estimated_token_count == 0:
        return

    ingest["units"][PayiInstrumentor.estimated_prompt_tokens] = Units(input=estimated_token_count, output=0)
