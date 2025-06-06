from typing import Any, Union, Optional, Sequence
from typing_extensions import override

import tiktoken
from wrapt import wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiCategories
from payi.types.ingest_units_params import Units

from .instrument import _IsStreaming, _StreamingType, _ProviderRequest, _PayiInstrumentor


class AnthropicInstrumentor:
    @staticmethod
    def is_vertex(instance: Any) -> bool:
        from anthropic import AnthropicVertex, AsyncAnthropicVertex  # type: ignore # noqa: I001

        return isinstance(instance._client, (AsyncAnthropicVertex, AnthropicVertex))

    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            import anthropic  # type: ignore #  noqa: F401  I001

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "Messages.create",
                messages_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "Messages.stream",
                stream_messages_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "AsyncMessages.create",
                amessages_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "anthropic.resources.messages",
                "AsyncMessages.stream",
                astream_messages_wrapper(instrumentor),
            )

        except Exception as e:
            instrumentor._logger.debug(f"Error instrumenting anthropic: {e}")
            return


@_PayiInstrumentor.payi_wrapper
def messages_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Anthropic messages wrapper")
    return instrumentor.invoke_wrapper(
        _AnthropicProviderRequest(instrumentor=instrumentor, streaming_type=_StreamingType.iterator, instance=instance),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def stream_messages_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Anthropic stream wrapper")
    return instrumentor.invoke_wrapper(
        _AnthropicProviderRequest(instrumentor=instrumentor, streaming_type=_StreamingType.stream_manager, instance=instance),
        _IsStreaming.true,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_awrapper
async def amessages_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("aync Anthropic messages wrapper")
    return await instrumentor.async_invoke_wrapper(
        _AnthropicProviderRequest(instrumentor=instrumentor, streaming_type=_StreamingType.iterator, instance=instance),
        _IsStreaming.kwargs,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_awrapper
async def astream_messages_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("aync Anthropic stream wrapper")
    return await instrumentor.async_invoke_wrapper(
        _AnthropicProviderRequest(instrumentor=instrumentor, streaming_type=_StreamingType.stream_manager, instance=instance),
        _IsStreaming.true,
        wrapped,
        instance,
        args,
        kwargs,
    )

class _AnthropicProviderRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor, streaming_type: _StreamingType, instance: Any = None) -> None:
        self._vertex: bool = AnthropicInstrumentor.is_vertex(instance)
        super().__init__(
            instrumentor=instrumentor,
            category=PayiCategories.google_vertex if self._vertex else PayiCategories.anthropic,
            streaming_type=streaming_type,
            )

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
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        self._ingest["resource"] = ("anthropic." if self._vertex else "") + kwargs.get("model", "")

        messages = kwargs.get("messages")
        if messages:
            estimated_token_count = 0 
            has_image = False

            try:
                enc = tiktoken.get_encoding("cl100k_base")
                for message in messages:
                    msg_has_image, msg_prompt_tokens = has_image_and_get_texts(enc, message.get('content', ''))
                    if msg_has_image:
                        has_image = True
                        estimated_token_count += msg_prompt_tokens
                
                if has_image and estimated_token_count > 0:
                    self._estimated_prompt_tokens = estimated_token_count
     
            except Exception:
                self._instrumentor._logger.warning("Error getting encoding for cl100k_base")

        return True

    @override
    def process_exception(self, exception: Exception, kwargs: Any, ) -> bool:
        try:
            status_code: Optional[int] = None

            if hasattr(exception, "status_code"):
                status_code = getattr(exception, "status_code", None)
                if isinstance(status_code, int):
                    self._ingest["http_status_code"] = status_code

            if not status_code:
                self.exception_to_semantic_failure(exception,)
                return True

            if hasattr(exception, "request_id"):
                request_id = getattr(exception, "request_id", None)
                if isinstance(request_id, str):
                    self._ingest["provider_response_id"] = request_id

            if hasattr(exception, "response"):
                response = getattr(exception, "response", None)
                if hasattr(response, "text"):
                    text = getattr(response, "text", None)
                    if isinstance(text, str):
                        self._ingest["provider_response_json"] = text

        except Exception as e:
            self._instrumentor._logger.debug(f"Error processing exception: {e}")
            return False

        return True


def has_image_and_get_texts(encoding: tiktoken.Encoding, content: Union[str, 'list[Any]']) -> 'tuple[bool, int]':
    if isinstance(content, list): # type: ignore
        has_image = any(item.get("type") == "image" for item in content)
        if has_image is False:
            return has_image, 0
        
        token_count = sum(len(encoding.encode(item.get("text", ""))) for item in content if item.get("type") == "text")
        return has_image, token_count
    
    return False, 0