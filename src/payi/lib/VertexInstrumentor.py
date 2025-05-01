import json
import logging
import math
from typing import Any, List, Sequence, Union
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

VERTEX_CHARACTER_BILLING_MODELS = [
    "google.gemini-1.5-pro",
    "google.gemini-1.5-pro-001",
    "google.gemini-1.5-pro-002",
    "google.gemini-1.5-flash",
    "google.gemini-1.5-flash-001",
    "google.gemini-1.5-flash-002",
    ]

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
            input: int = 0
            output: int = 0

            if self._ingest["resource"] in VERTEX_CHARACTER_BILLING_MODELS:
                input = usage["prompt_token_count"] * 4
                output = usage["candidates_token_count"] * 4
    
                prompt_tokens_details: list[dict[str, Any]] = usage.get("prompt_tokens_details")
                large_context = "" if usage["prompt_token_count"] < 128000 else "_large_context"
                
                for details in prompt_tokens_details:
                    modality = details.get("modality", None)
                    if modality:
                        if modality == "VIDEO":
                            token_count = details.get("token_count", 0)
                            video_seconds = math.ceil(token_count / 258)
                            self._ingest["units"]["video"+large_context] = Units(input=video_seconds)

            else:
                input = usage["prompt_token_count"] * 4
                output = usage["candidates_token_count"] * 4

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

        usage = response_dict.get("usage_metadata", {})

        input = usage.get("prompt_token_count", 0)


        if response_dict["model_version"].startswith("gemini-1."):
            # gemini 1.0 and 1.5 units are reported in characters, per second, per image, etc...
            large_context = "" if input < 128000 else "_large_context"

            prompt_tokens_details: list[dict[str, Any]] = usage.get("prompt_tokens_details")
            
            for details in prompt_tokens_details:
                modality = details.get("modality", "")
                if not modality:
                    continue

                input_token_details = details.get("token_count", 0)
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
                    num_images = math.ceil(input_token_details / 258)
                    self._ingest["units"]["vision"+large_context] = Units(input=num_images)

                elif modality == "VIDEO":
                    video_seconds = math.ceil(input_token_details / 285)
                    self._ingest["units"]["video"+large_context] = Units(input=video_seconds)

                elif modality == "AUDIO":
                    audio_seconds = math.ceil(input_token_details / 25)
                    self._ingest["units"]["audio"+large_context] = Units(input=audio_seconds)
        else:
            # other models are reported in tokens
            self._ingest["units"]["text"] = Units(
                input=response_dict["usage_metadata"]["prompt_token_count"],
                output=response_dict["usage_metadata"]["candidates_token_count"])

        if log_prompt_and_response:
            self._ingest["provider_response_json"] = [json.dumps(response_dict)]

        return None
