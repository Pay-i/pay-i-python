import json
import math
import logging
from typing import Any, List, Union, Optional, Sequence
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

def count_chars_skip_spaces(text: str) -> int:
    return sum(1 for c in text if not c.isspace())

class _GoogleVertexRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, category=PayiCategories.google_vertex)
        self._prompt_character_count = 0

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        from vertexai.generative_models import Content, Image, Part # type: ignore #  noqa: F401  I001

        if not args:
            return True
        
        value: Union[ # type: ignore
            Content,
            str,
            Image,
            Part,
            List[Union[str, Image, Part]],
        ] = args[0] # type: ignore

        items: List[Union[str, Image, Part]] = [] # type: ignore #  noqa: F401  I001

        if not value:
            raise TypeError("value must not be empty")

        if isinstance(value, Content):
            return value.parts # type: ignore
        if isinstance(value, (str, Image, Part)):
            items = [value] # type: ignore

        elif isinstance(value, list):
            items = value # type: ignore

        for item in items: # type: ignore
            text = ""
            if isinstance(item, Part):
                d = item.to_dict() # type: ignore
                if "text" in d:
                    text = d["text"] # type: ignore
            elif isinstance(item, str):
                text = item

            if text:
                self._prompt_character_count += count_chars_skip_spaces(text) # type: ignore
             
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
            self._compute_usage(response_dict)

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

        self._compute_usage(response_dict)
        
        if log_prompt_and_response:
            self._ingest["provider_response_json"] = [json.dumps(response_dict)]

        return None

    def add_units(self, key: str, input: Optional[int] = None, output: Optional[int] = None) -> None:
        if input is not None:
            self._ingest["units"][key]["input"] = input
        if output is not None:
            self._ingest["units"][key]["output"] = output

    def _compute_usage(self, response_dict: 'dict[str, Any]') -> None:
        usage = response_dict.get("usage_metadata", {})
        input = usage.get("prompt_token_count", 0)
        prompt_tokens_details: list[dict[str, Any]] = usage.get("prompt_tokens_details")
        candidates_tokens_details: list[dict[str, Any]] = usage.get("candidates_tokens_details")

        if response_dict["model_version"].startswith("gemini-1."):
            # gemini 1.0 and 1.5 units are reported in characters, per second, per image, etc...
            large_context = "" if input < 128000 else "_large_context"
        
            for details in prompt_tokens_details:
                modality = details.get("modality", "")
                if not modality:
                    continue

                modality_token_count = details.get("token_count", 0)
                if modality == "TEXT":
                    input = self._prompt_character_count
                    if input == 0:
                        input = response_dict["usage_metadata"]["prompt_token_count"] * 4

                    output = 0
                    for candidate in response_dict["candidates"]:
                        parts = candidate.get("content", {}).get("parts", [])
                        for part in parts:
                            if "text" in part:
                                output += count_chars_skip_spaces(part["text"])

                    if output == 0:
                        output = response_dict["usage_metadata"]["candidates_token_count"] * 4

                    self._ingest["units"]["text"+large_context] = Units(input=input, output=output)

                elif modality == "IMAGE":
                    num_images = math.ceil(modality_token_count / 258)
                    self.add_units("vision"+large_context, input=num_images)

                elif modality == "VIDEO":
                    video_seconds = math.ceil(modality_token_count / 285)
                    self.add_units("video"+large_context, input=video_seconds)

                elif modality == "AUDIO":
                    audio_seconds = math.ceil(modality_token_count / 25)
                    self.add_units("audio"+large_context, input=audio_seconds)

        elif response_dict["model_version"].startswith("gemini-2.0"):
            for details in prompt_tokens_details:
                modality = details.get("modality", "")
                if not modality:
                    continue

                modality_token_count = details.get("token_count", 0)
                if modality == "IMAGE":
                    self.add_units("vision", input=modality_token_count)
                elif modality in ("VIDEO", "AUDIO", "TEXT"):
                    self.add_units(modality.lower(), input=modality_token_count)
            for details in candidates_tokens_details:
                modality = details.get("modality", "")
                if not modality:
                    continue

                modality_token_count = details.get("token_count", 0)
                if modality in ("VIDEO", "AUDIO", "TEXT", "IMAGE"):
                    self.add_units(modality.lower(), output=modality_token_count)
