import logging
from typing import Any

from wrapt import wrap_function_wrapper  # type: ignore

from payi.types import IngestUnitsParams
from payi.types.ingest_units_params import Units

from .instrument import PayiInstrumentor


class AnthropicIntrumentor:
    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
        try:
            import anthropic  # type: ignore #  noqa: F401  I001

            # wrap_function_wrapper(
            #     "anthropic.resources.completions",
            #     "Completions.create",
            #     chat_wrapper(instrumentor),
            # )

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

        except Exception as e:
            logging.debug(f"Error instrumenting anthropic: {e}")
            return


@PayiInstrumentor.payi_wrapper
def chat_wrapper(
    instrumentor: PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    args: Any,
    kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        "system.anthropic",
        process_chunk,
        process_synchronous_response,
        wrapped,
        instance,
        args,
        kwargs,
    )


def process_chunk(chunk: Any, ingest: IngestUnitsParams) -> None:
    if chunk.type == "message_start":
        usage = chunk.message.usage
        units = ingest["units"]

        units["text"] = Units(input=usage.input_tokens, output=0)

        if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
            text_cache_write = usage.cache_creation_input_tokens
            units["text_cache_write"] = Units(input=text_cache_write, output=0)

        if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
            text_cache_read = usage.cache_read_input_tokens
            units["text_cache_read"] = Units(input=text_cache_read, output=0)

    elif chunk.type == "message_delta":
        usage = chunk.usage
        ingest["units"]["text"]["output"] = usage.output_tokens


def process_synchronous_response(response: Any, ingest: IngestUnitsParams, log_prompt_and_response: bool) -> None:
    usage = response.usage
    input = usage.input_tokens
    ouptut = usage.output_tokens
    units: dict[str, Units] = ingest["units"]

    if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
        text_cache_write = usage.cache_creation_input_tokens
        units["text_cache_write"] = Units(input=text_cache_write, output=0)

    if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
        text_cache_read = usage.cache_read_input_tokens
        units["text_cache_read"] = Units(input=text_cache_read, output=0)

    units["text"] = Units(input=input, output=ouptut)

    if log_prompt_and_response:
        ingest["provider_response_json"] = response.to_json()
