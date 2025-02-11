import logging
from typing import Any, Union

import tiktoken
from wrapt import wrap_function_wrapper  # type: ignore

from payi.types import IngestUnitsParams
from payi.types.ingest_units_params import Units

from .instrument import IsStreaming, PayiInstrumentor


class AnthropicIntrumentor:
    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
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


@PayiInstrumentor.payi_wrapper
def chat_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.anthropic",
        process_chunk,
        process_request,
        process_synchronous_response,
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
        "system.anthropic",
        process_chunk,
        process_request,
        process_synchronous_response,
        IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )


def process_chunk(chunk: Any, ingest: IngestUnitsParams) -> None:
    if chunk.type == "message_start":
        ingest["provider_response_id"] = chunk.message.id

        usage = chunk.message.usage
        units = ingest["units"]

        input = PayiInstrumentor.update_for_vision(usage.input_tokens, units)

        units["text"] = Units(input=input, output=0)

        if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
            text_cache_write = usage.cache_creation_input_tokens
            units["text_cache_write"] = Units(input=text_cache_write, output=0)

        if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
            text_cache_read = usage.cache_read_input_tokens
            units["text_cache_read"] = Units(input=text_cache_read, output=0)

    elif chunk.type == "message_delta":
        usage = chunk.usage
        ingest["units"]["text"]["output"] = usage.output_tokens


def process_synchronous_response(response: Any, ingest: IngestUnitsParams, log_prompt_and_response: bool, *args: Any, **kwargs: 'dict[str, Any]') -> Any: # noqa: ARG001
    usage = response.usage
    input = usage.input_tokens
    output = usage.output_tokens
    units: dict[str, Units] = ingest["units"]

    if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
        text_cache_write = usage.cache_creation_input_tokens
        units["text_cache_write"] = Units(input=text_cache_write, output=0)

    if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
        text_cache_read = usage.cache_read_input_tokens
        units["text_cache_read"] = Units(input=text_cache_read, output=0)

    input = PayiInstrumentor.update_for_vision(input, units)

    units["text"] = Units(input=input, output=output)

    if log_prompt_and_response:
        ingest["provider_response_json"] = response.to_json()
    
    ingest["provider_response_id"] = response.id
    
    return None

def has_image_and_get_texts(encoding: tiktoken.Encoding, content: Union[str, 'list[Any]']) -> 'tuple[bool, int]':
    if isinstance(content, str):
        return False, 0
    elif isinstance(content, list): # type: ignore
        has_image = any(item.get("type") == "image" for item in content)
        if has_image is False:
            return has_image, 0
        
        token_count = sum(len(encoding.encode(item.get("text", ""))) for item in content if item.get("type") == "text")
        return has_image, token_count

def process_request(ingest: IngestUnitsParams, *args: Any, **kwargs: Any) -> None: # noqa: ARG001
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

    ingest["units"][PayiInstrumentor.estimated_prompt_tokens] = Units(input=estimated_token_count, output=0)
