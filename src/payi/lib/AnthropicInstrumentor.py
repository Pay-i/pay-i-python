import logging
from typing import Any, Union
from typing_extensions import override

import tiktoken
from wrapt import wrap_function_wrapper  # type: ignore

from payi.types.ingest_units_params import Units

from .instrument import _IsStreaming, _ProviderRequest, _PayiInstrumentor


class AnthropicIntrumentor:
    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            import anthropic  # type: ignore #  noqa: F401  I001

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "Messages.create",
                chat_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "Messages.stream",
                chat_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "AsyncMessages.create",
                achat_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "AsyncMessages.stream",
                achat_wrapper(instrumentor),
            )

        except Exception as e:
            logging.debug(f"Error instrumenting anthropic: {e}")
            return


@_PayiInstrumentor.payi_wrapper
def chat_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.anthropic",
        _AnthropicProviderRequest(instrumentor),
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
        "system.anthropic",
        _AnthropicProviderRequest(instrumentor),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

class _AnthropicProviderRequest(_ProviderRequest):
    @override
    def process_chunk(self, chunk: Any) -> bool:
        if chunk.type == "message_start":
            self._ingest["provider_response_id"] = chunk.message.id

            usage = chunk.message.usage
            units = self._ingest["units"]

            input = _PayiInstrumentor.update_for_vision(usage.input_tokens, units, self._estimated_prompt_tokens)

            units["text"] = Units(input=input, output=0)

            if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
                text_cache_write = usage.cache_creation_input_tokens
                units["text_cache_write"] = Units(input=text_cache_write, output=0)

            if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
                text_cache_read = usage.cache_read_input_tokens
                units["text_cache_read"] = Units(input=text_cache_read, output=0)

        elif chunk.type == "message_delta":
            usage = chunk.usage
            self._ingest["units"]["text"]["output"] = usage.output_tokens
        
        return True

    @override
    def process_synchronous_response(self, response: Any, log_prompt_and_response: bool, kwargs: Any) -> Any:
        usage = response.usage
        input = usage.input_tokens
        output = usage.output_tokens
        units: dict[str, Units] = self._ingest["units"]

        if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
            text_cache_write = usage.cache_creation_input_tokens
            units["text_cache_write"] = Units(input=text_cache_write, output=0)

        if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
            text_cache_read = usage.cache_read_input_tokens
            units["text_cache_read"] = Units(input=text_cache_read, output=0)

        input = _PayiInstrumentor.update_for_vision(input, units, self._estimated_prompt_tokens)

        units["text"] = Units(input=input, output=output)

        if log_prompt_and_response:
            self._ingest["provider_response_json"] = response.to_json()
        
        self._ingest["provider_response_id"] = response.id
        
        return None

    @override
    def process_request(self, kwargs: Any) -> None:
        messages = kwargs.get("messages")
        if not messages or len(messages) == 0:
            return
        
        estimated_token_count = 0 
        has_image = False

        enc = tiktoken.get_encoding("cl100k_base")
        
        for message in messages:
            msg_has_image, msg_prompt_tokens = has_image_and_get_texts(enc, message.get('content', ''))
            if msg_has_image:
                has_image = True
                estimated_token_count += msg_prompt_tokens
        
        if not has_image or estimated_token_count == 0:
            return
        self._estimated_prompt_tokens = estimated_token_count

def has_image_and_get_texts(encoding: tiktoken.Encoding, content: Union[str, 'list[Any]']) -> 'tuple[bool, int]':
    if isinstance(content, str):
        return False, 0
    elif isinstance(content, list): # type: ignore
        has_image = any(item.get("type") == "image" for item in content)
        if has_image is False:
            return has_image, 0
        
        token_count = sum(len(encoding.encode(item.get("text", ""))) for item in content if item.get("type") == "text")
        return has_image, token_count

