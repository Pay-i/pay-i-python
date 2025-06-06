import json
import math
from typing import Any, List, Union, Optional, Sequence
from typing_extensions import override

from wrapt import wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiCategories
from payi.types.ingest_units_params import Units

from .instrument import _IsStreaming, _StreamingType, _ProviderRequest, _PayiInstrumentor


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
            instrumentor._logger.debug(f"Error instrumenting vertex: {e}")
            return

@_PayiInstrumentor.payi_wrapper
def generate_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("vertexai generate_content wrapper")
    return instrumentor.invoke_wrapper(
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
    instrumentor._logger.debug("async vertexai generate_content wrapper")
    return await instrumentor.async_invoke_wrapper(
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
        super().__init__(
            instrumentor=instrumentor,
            category=PayiCategories.google_vertex,
            streaming_type=_StreamingType.generator,
            )
        self._prompt_character_count = 0
        self._candiates_character_count = 0

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
            items = value.parts # type: ignore
        if isinstance(value, (str, Image, Part)):
            items = [value] # type: ignore
        if isinstance(value, list):
            items = value # type: ignore

        for item in items: # type: ignore
            text = ""
            if isinstance(item, Part):
                d = item.to_dict() # type: ignore
                if "text" in d:
                    text = d["text"] # type: ignore
            elif isinstance(item, str):
                text = item

            if text != "":
                self._prompt_character_count += count_chars_skip_spaces(text) # type: ignore
             
        return True

    @override
    def process_request_prompt(self, prompt: 'dict[str, Any]', args: Sequence[Any], kwargs: 'dict[str, Any]') -> None:
        from vertexai.generative_models import Content, Image, Part, Tool # type: ignore #  noqa: F401  I001

        key = "contents"

        if not args:
            return
        
        value: Union[ # type: ignore
            Content,
            str,
            Image,
            Part,
            List[Union[str, Image, Part]],
        ] = args[0] # type: ignore

        items: List[Union[str, Image, Part]] = [] # type: ignore #  noqa: F401  I001

        if not value:
            return

        if isinstance(value, str):
            prompt[key] = Content(parts=[Part.from_text(value)]).to_dict() # type: ignore
        elif isinstance(value, (Image, Part)):
            prompt[key] = Content(parts=[value]).to_dict() # type: ignore
        elif isinstance(value, Content):
            prompt[key] = value.to_dict() # type: ignore
        elif isinstance(value, list):
            items = value # type: ignore
            parts = []

            for item in items: # type: ignore
                if isinstance(item, str):
                    parts.append(Part.from_text(item)) # type: ignore
                elif isinstance(item, Part):
                    parts.append(item) # type: ignore
                elif isinstance(item, Image):
                    parts.append(Part.from_image(item)) # type: ignore
                        
            prompt[key] = Content(parts=parts).to_dict() # type: ignore

        tools: Optional[list[Tool]] = kwargs.get("tools", None)  # type: ignore
        if tools:
            t: list[dict[Any, Any]] = []
            for tool in tools: # type: ignore
                if isinstance(tool, Tool):
                    t.append(tool.to_dict())  # type: ignore
            if t:
                prompt["tools"] = t

        tool_config = kwargs.get("tool_config", None)  # type: ignore
        if tool_config:
            # tool_config does not have to_dict or any other serializable object
            prompt["tool_config"] = str(tool_config)  # type: ignore

    @override
    def process_chunk(self, chunk: Any) -> bool:
        response_dict: dict[str, Any] = chunk.to_dict()
        if "provider_response_id" not in self._ingest:
            id = response_dict.get("response_id", None)
            if id:
                self._ingest["provider_response_id"] = id

        model: str = response_dict.get("model_version", "")

        self._ingest["resource"] = "google." + model

        for candidate in response_dict.get("candidates", []):
            parts = candidate.get("content", {}).get("parts", [])
            for part in parts:
                self._candiates_character_count += count_chars_skip_spaces(part.get("text", ""))

        usage = response_dict.get("usage_metadata", {})
        if usage and "prompt_token_count" in usage and "candidates_token_count" in usage:
            self._compute_usage(response_dict, streaming_candidates_characters=self._candiates_character_count)

        return True
    
    @staticmethod
    def _is_character_billing_model(model: str) -> bool:
        return model.startswith("gemini-1.")
    
    @override
    def process_synchronous_response(
        self,
        response: Any,
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:
        response_dict = response.to_dict()

        id: Optional[str] = response_dict.get("response_id", None)
        if id:
            self._ingest["provider_response_id"] = id
        
        model: Optional[str] = response_dict.get("model_version", None)
        if model:
            self._ingest["resource"] = "google." + model

        self._compute_usage(response_dict)
        
        if log_prompt_and_response:
            self._ingest["provider_response_json"] = [json.dumps(response_dict)]

        return None

    def add_units(self, key: str, input: Optional[int] = None, output: Optional[int] = None) -> None:
        if key not in self._ingest["units"]:
            self._ingest["units"][key] = {}
        if input is not None:
            self._ingest["units"][key]["input"] = input
        if output is not None:
            self._ingest["units"][key]["output"] = output

    def _compute_usage(self, response_dict: 'dict[str, Any]', streaming_candidates_characters: Optional[int] = None) -> None:
        usage = response_dict.get("usage_metadata", {})
        input = usage.get("prompt_token_count", 0)

        prompt_tokens_details: list[dict[str, Any]] = usage.get("prompt_tokens_details")
        candidates_tokens_details: list[dict[str, Any]] = usage.get("candidates_tokens_details")

        model: str = response_dict.get("model_version", "")

        if self._is_character_billing_model(model):
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
                        # back up calc if nothing was calculated from the prompt
                        input = response_dict["usage_metadata"]["prompt_token_count"] * 4

                    output = 0
                    if streaming_candidates_characters is None:
                        for candidate in response_dict.get("candidates", []):
                            parts = candidate.get("content", {}).get("parts", [])
                            for part in parts:
                                output += count_chars_skip_spaces(part.get("text", ""))

                        if output == 0:
                            # back up calc if no parts
                            output = response_dict["usage_metadata"]["candidates_token_count"] * 4
                    else:
                        output = streaming_candidates_characters

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

        elif model.startswith("gemini-2.0"):
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
