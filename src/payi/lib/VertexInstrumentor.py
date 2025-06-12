import json
import math
from typing import Any, List, Union, Optional, Sequence
from typing_extensions import override

from wrapt import wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiCategories
from payi.types.ingest_units_params import Units

from .instrument import _ChunkResult, _IsStreaming, _StreamingType, _ProviderRequest, _PayiInstrumentor


class VertexInstrumentor:
    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            wrap_function_wrapper(
                "vertexai.generative_models",
                "GenerativeModel.generate_content",
                generate_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "vertexai.generative_models",
                "GenerativeModel.generate_content_async",
                agenerate_wrapper(instrumentor),
            )

        except Exception as e:
            instrumentor._logger.debug(f"Error instrumenting vertex: {e}")
            return

        # separate instrumetning preview functionality from released in case it fails
        try:
            wrap_function_wrapper(
                "vertexai.preview.generative_models",
                "GenerativeModel.generate_content",
                generate_wrapper(instrumentor),
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
            is_google_vertex_or_genai_client=True,
            )
        self._prompt_character_count = 0
        self._candidates_character_count = 0
        self._model_name: Optional[str] = None

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        from vertexai.generative_models import Content, Image, Part # type: ignore #  noqa: F401  I001

        # Try to extra the model name as a backup if the response does not provide it (older vertexai versions do not)
        if instance and hasattr(instance, "_model_name"):
            model = instance._model_name
            if model and isinstance(model, str):
                # Extract the model name after the last slash
                self._model_name = model.split('/')[-1]
        
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

    def _get_model_name(self, response: 'dict[str, Any]') -> Optional[str]:
        model: Optional[str] = response.get("model_version", None)
        if model:
            return model

        return self._model_name

    @override
    def process_chunk(self, chunk: Any) -> _ChunkResult:
        ingest = False
        response_dict: dict[str, Any] = chunk.to_dict()
        if "provider_response_id" not in self._ingest:
            id = response_dict.get("response_id", None)
            if id:
                self._ingest["provider_response_id"] = id

        if "resource" not in self._ingest: 
            model: Optional[str] = self._get_model_name(response_dict)  # type: ignore[unreachable]
            if model:
                self._ingest["resource"] = "google." + model

        for candidate in response_dict.get("candidates", []):
            parts = candidate.get("content", {}).get("parts", [])
            for part in parts:
                self._candidates_character_count += count_chars_skip_spaces(part.get("text", ""))

        usage = response_dict.get("usage_metadata", {})
        if usage and "prompt_token_count" in usage and "candidates_token_count" in usage:
            vertex_compute_usage(
                request=self,
                model=self._get_model_name(response_dict),
                response_dict=response_dict,
                prompt_character_count=self._prompt_character_count,
                streaming_candidates_characters=self._candidates_character_count,
            )
            ingest = True

        return _ChunkResult(send_chunk_to_caller=True, ingest=ingest)
    
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
        
        model: Optional[str] = self._get_model_name(response_dict)
        if model:
            self._ingest["resource"] = "google." + model

        vertex_compute_usage(
            request=self,
            model=model,
            response_dict=response_dict,
            prompt_character_count=self._prompt_character_count,
            streaming_candidates_characters=self._candidates_character_count
            )
        
        if log_prompt_and_response:
            self._ingest["provider_response_json"] = [json.dumps(response_dict)]

        return None

def vertex_compute_usage(
    request: _ProviderRequest,
    model: Optional[str],
    response_dict: 'dict[str, Any]',
    prompt_character_count: int = 0,
    streaming_candidates_characters: Optional[int] = None) -> None:

    def is_character_billing_model(model: str) -> bool:
        return model.startswith("gemini-1.")

    def is_large_context_token_model(model: str, input_tokens: int) -> bool:
        return model.startswith("gemini-2.5-pro") and input_tokens > 200_000

    def add_units(request: _ProviderRequest, key: str, input: Optional[int] = None, output: Optional[int] = None) -> None:
        if key not in request._ingest["units"]:
            request._ingest["units"][key] = {}
        if input is not None:
            request._ingest["units"][key]["input"] = input
        if output is not None:
            request._ingest["units"][key]["output"] = output

    usage = response_dict.get("usage_metadata", {})
    input = usage.get("prompt_token_count", 0)

    prompt_tokens_details: list[dict[str, Any]] = usage.get("prompt_tokens_details", [])
    candidates_tokens_details: list[dict[str, Any]] = usage.get("candidates_tokens_details", [])

    if not model:
        model = ""
    
    large_context = ""

    if is_character_billing_model(model):
        if input > 128000: 
            large_context = "_large_context"

        # gemini 1.0 and 1.5 units are reported in characters, per second, per image, etc...
        for details in prompt_tokens_details:
            modality = details.get("modality", "")
            if not modality:
                continue

            modality_token_count = details.get("token_count", 0)
            if modality == "TEXT":
                input = prompt_character_count
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

                request._ingest["units"]["text"+large_context] = Units(input=input, output=output)

            elif modality == "IMAGE":
                num_images = math.ceil(modality_token_count / 258)
                add_units(request, "vision"+large_context, input=num_images)

            elif modality == "VIDEO":
                video_seconds = math.ceil(modality_token_count / 285)
                add_units(request, "video"+large_context, input=video_seconds)

            elif modality == "AUDIO":
                audio_seconds = math.ceil(modality_token_count / 25)
                add_units(request, "audio"+large_context, input=audio_seconds)

        # No need to gover the candidates_tokens_details as all the character based 1.x models only output TEXT
        # for details in candidates_tokens_details:

    else:
        # thinking tokens introduced in 2.5 after the transition to token based billing
        thinking_token_count = usage.get("thoughts_token_count", 0)

        if is_large_context_token_model(model, input):
            large_context = "_large_context"

        for details in prompt_tokens_details:
            modality = details.get("modality", "")
            if not modality:
                continue

            modality_token_count = details.get("token_count", 0)
            if modality == "IMAGE":
                add_units(request, "vision"+large_context, input=modality_token_count)
            elif modality in ("VIDEO", "AUDIO", "TEXT"):
                add_units(request, modality.lower()+large_context, input=modality_token_count)
        for details in candidates_tokens_details:
            modality = details.get("modality", "")
            if not modality:
                continue

            modality_token_count = details.get("token_count", 0)
            if modality in ("VIDEO", "AUDIO", "TEXT", "IMAGE"):
                add_units(request, modality.lower()+large_context, output=modality_token_count)

        if thinking_token_count > 0:
            add_units(request, "reasoning"+large_context, output=thinking_token_count)

    if not request._ingest["units"]:
        input = usage.get("prompt_token_count", 0)
        output = usage.get("candidates_token_count", 0) * 4
        
        if is_character_billing_model(model):
            if prompt_character_count > 0:
                input = prompt_character_count
            else:
                input *= 4

            # if no units were added, add a default unit and assume 4 characters per token
            request._ingest["units"]["text"+large_context] = Units(input=input, output=output)
        else:
            # if no units were added, add a default unit
            request._ingest["units"]["text"] = Units(input=input, output=output)