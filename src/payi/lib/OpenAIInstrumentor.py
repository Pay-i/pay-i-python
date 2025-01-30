import json
import logging
from typing import Any
from importlib.metadata import version

from wrapt import wrap_function_wrapper  # type: ignore

from payi.types import IngestUnitsParams
from payi.types.ingest_units_params import Units

from .instrument import PayiInstrumentor


class OpenAiInstrumentor:
    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
        try:
            from openai import OpenAI  # type: ignore #  noqa: F401  I001

            wrap_function_wrapper(
                "openai.resources.chat.completions",
                "Completions.create",
                chat_wrapper(instrumentor),
            )
        except Exception as e:
            logging.debug(f"Error instrumenting openai: {e}")
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
        "system.openai",
        process_chat_chunk,
        process_chat_synchronous_response,
        wrapped,
        instance,
        args,
        kwargs,
    )


def process_chat_synchronous_response(response: str, ingest: IngestUnitsParams, log_prompt_and_response: bool) -> None:
    response_dict = model_to_dict(response)

    add_usage_units(response_dict["usage"], ingest["units"])

    if log_prompt_and_response:
        ingest["provider_response_json"] = [json.dumps(response_dict)]


def process_chat_chunk(chunk: Any, ingest: IngestUnitsParams) -> None:
    model = model_to_dict(chunk)
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

    input -= input_cache

    units["text"] = Units(input=input, output=output)
