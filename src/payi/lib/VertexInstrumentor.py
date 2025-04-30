import json
import logging
from typing import Any
from typing_extensions import override

from wrapt import wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiCategories
from payi.types.ingest_units_params import Units

from .instrument import _IsStreaming, _ProviderRequest, _PayiInstrumentor


class VertexInstrumentor:
    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            import vertexai  # type: ignore #  noqa: F401  I001

            wrap_function_wrapper(
                "vertexai.generative_models",
                "GenerativeModel.generate_content",
                generate_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "vertexai.preview.generative_models",
                "GenerativeModel.generate_content",
                generate_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "vertexai.generative_models",
                "GenerativeModel.generate_content_async",
                agenerate_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "vertexai.preview.generative_models",
                "GenerativeModel.generate_content_async",
                agenerate_wrapper(instrumentor),
            )

        except Exception as e:
            logging.debug(f"Error instrumenting vertex: {e}")
            return

@_PayiInstrumentor.payi_wrapper
def generate_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return instrumentor.chat_wrapper(
        _GoogleVertexRequest(instrumentor),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_awrapper
async def agenerate_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    return await instrumentor.achat_wrapper(
        _GoogleVertexRequest(instrumentor),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

class _GoogleVertexRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, category=PayiCategories.google_vertex)

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', kwargs: Any) -> bool:

        return True

    @override
    def process_chunk(self, chunk: Any) -> bool:
        response_dict: dict[str, Any] = chunk.to_dict()
        if "provider_response_id" not in self._ingest:
            id = response_dict.get("response_id", None)
            if id:
                self._ingest["provider_response_id"] = id

        if "resource" not in self._ingest:
            model = response_dict.get("model_version") # type: ignore
            if model is not None:
                self._ingest["resource"] = "google." + model
 
        usage = response_dict.get("usage_metadata", {})
        if usage and "prompt_token_count" in usage and "candidates_token_count" in usage:
            inputChars = usage["prompt_token_count"] * 4
            outputChars = usage["candidates_token_count"] * 4

            key = "text" if inputChars < 128000 else "text_large_context"
            self._ingest["units"][key] = Units(input=inputChars, output=outputChars)

        return True
    
    @override
    def process_synchronous_response(
        self,
        response: Any,
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:
        response_dict = response.to_dict()

        self._ingest["provider_response_id"] = response_dict["response_id"]

        self._ingest["resource"] = "google." + response_dict["model_version"]
        self._ingest["units"]["text"] = Units(
            input=response_dict["usage_metadata"]["prompt_token_count"],
            output=response_dict["usage_metadata"]["candidates_token_count"])

        if log_prompt_and_response:
            self._ingest["provider_response_json"] = [json.dumps(response_dict)]

        return None
