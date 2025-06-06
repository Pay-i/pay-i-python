import os
import json
from typing import Any, Sequence
from functools import wraps
from typing_extensions import override

from wrapt import ObjectProxy, wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiCategories, PayiHeaderNames, payi_aws_bedrock_url
from payi.types.ingest_units_params import Units, IngestUnitsParams
from payi.types.pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

from .instrument import _IsStreaming, _StreamingType, _ProviderRequest, _PayiInstrumentor

_supported_model_prefixes = ["meta.llama3", "anthropic.", "amazon.nova-pro", "amazon.nova-lite", "amazon.nova-micro"]

class BedrockInstrumentor:
    _instrumentor: _PayiInstrumentor

    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        BedrockInstrumentor._instrumentor = instrumentor

        try:
            import boto3  # type: ignore #  noqa: F401  I001

            wrap_function_wrapper(
                "botocore.client",
                "ClientCreator.create_client",
                create_client_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "botocore.session",
                "Session.create_client",
                create_client_wrapper(instrumentor),
            )

        except Exception as e:
            instrumentor._logger.debug(f"Error instrumenting bedrock: {e}")
            return

@_PayiInstrumentor.payi_wrapper
def create_client_wrapper(instrumentor: _PayiInstrumentor, wrapped: Any, instance: Any, *args: Any, **kwargs: Any) -> Any: #  noqa: ARG001
    if kwargs.get("service_name") != "bedrock-runtime":
        instrumentor._logger.debug(f"skipping client wrapper creation for {kwargs.get('service_name', '')} service")
        return wrapped(*args, **kwargs)

    try:
        client: Any = wrapped(*args, **kwargs)
        client.invoke_model = wrap_invoke(instrumentor, client.invoke_model)
        client.invoke_model_with_response_stream = wrap_invoke_stream(instrumentor, client.invoke_model_with_response_stream)
        client.converse = wrap_converse(instrumentor, client.converse)
        client.converse_stream = wrap_converse_stream(instrumentor, client.converse_stream)

        instrumentor._logger.debug(f"Instrumented bedrock client")

        if BedrockInstrumentor._instrumentor._proxy_default:
            # Register client callbacks to handle the Pay-i extra_headers parameter in the inference calls and redirect the request to the Pay-i endpoint
            _register_bedrock_client_callbacks(client)
            instrumentor._logger.debug(f"Registered bedrock client callbaks for proxy")

        return client
    except Exception as e:
        instrumentor._logger.debug(f"Error instrumenting bedrock client: {e}")
    
    return wrapped(*args, **kwargs)

BEDROCK_REQUEST_NAMES = [
    'request-created.bedrock-runtime.Converse',
    'request-created.bedrock-runtime.ConverseStream',
    'request-created.bedrock-runtime.InvokeModel',
    'request-created.bedrock-runtime.InvokeModelWithResponseStream',
]

def _register_bedrock_client_callbacks(client: Any) -> None:
    # Pass a unqiue_id to avoid registering the same callback multiple times in case this cell executed more than once
    # Redirect the request to the Pay-i endpoint after the request has been signed. 
    client.meta.events.register_last('request-created', _redirect_to_payi, unique_id=_redirect_to_payi)

def _redirect_to_payi(request: Any, event_name: str, **_: 'dict[str, Any]') -> None:
    from urllib3.util import parse_url
    from urllib3.util.url import Url

    if not event_name in BEDROCK_REQUEST_NAMES:
        return
    
    parsed_url: Url = parse_url(request.url)
    route_path = parsed_url.path
    request.url = f"{payi_aws_bedrock_url()}{route_path}"

    request.headers[PayiHeaderNames.api_key] = os.environ.get("PAYI_API_KEY", "")
    request.headers[PayiHeaderNames.provider_base_uri] = parsed_url.scheme + "://" + parsed_url.host # type: ignore
    
    extra_headers = BedrockInstrumentor._instrumentor._create_extra_headers()

    for key, value in extra_headers.items():
        request.headers[key] = value


class InvokeResponseWrapper(ObjectProxy): # type: ignore
    def __init__(
        self,
        response: Any,
        instrumentor: _PayiInstrumentor,
        ingest: IngestUnitsParams,
        log_prompt_and_response: bool
        ) -> None:

        super().__init__(response) # type: ignore
        self._response = response
        self._instrumentor = instrumentor
        self._ingest = ingest
        self._log_prompt_and_response = log_prompt_and_response

    def read(self, amt: Any =None) -> Any: # type: ignore
        # data is array of bytes
        data: bytes = self.__wrapped__.read(amt) # type: ignore
        response = json.loads(data) # type: ignore

        resource = self._ingest["resource"]
        if not resource:
            return
        
        input: int = 0
        output: int = 0
        units: dict[str, Units] = self._ingest["units"]

        if resource.startswith("meta.llama3"):
            input = response['prompt_token_count']
            output = response['generation_token_count']
        elif resource.startswith("anthropic."):
            usage = response['usage']
            input = usage['input_tokens']
            output = usage['output_tokens']
        units["text"] = Units(input=input, output=output)

        if self._log_prompt_and_response:
            self._ingest["provider_response_json"] = data.decode('utf-8') # type: ignore
            
        self._instrumentor._ingest_units(self._ingest)

        return data # type: ignore

def _is_supported_model(modelId: str) -> bool:
    return any(prefix in modelId for prefix in _supported_model_prefixes)

def wrap_invoke(instrumentor: _PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: 'dict[str, Any]') -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if _is_supported_model(modelId):
            instrumentor._logger.debug(f"bedrock invoke wrapper, modelId: {modelId}")
            return instrumentor.invoke_wrapper(
                _BedrockInvokeSynchronousProviderRequest(instrumentor=instrumentor),
                _IsStreaming.false,
                wrapped,
                None,
                args,
                kwargs,
            )   

        instrumentor._logger.debug(f"bedrock invoke wrapper, unsupported modelId: {modelId}")
        return wrapped(*args, **kwargs)
    
    return invoke_wrapper

def wrap_invoke_stream(instrumentor: _PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: Any) -> Any:
        modelId: str = kwargs.get("modelId", "") # type: ignore

        if _is_supported_model(modelId):
            instrumentor._logger.debug(f"bedrock invoke stream wrapper, modelId: {modelId}")
            return instrumentor.invoke_wrapper(
                _BedrockInvokeStreamingProviderRequest(instrumentor=instrumentor, model_id=modelId),
                _IsStreaming.true,
                wrapped,
                None,
                args,
                kwargs,
            )
        instrumentor._logger.debug(f"bedrock invoke stream wrapper, unsupported modelId: {modelId}")
        return wrapped(*args, **kwargs)

    return invoke_wrapper

def wrap_converse(instrumentor: _PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: 'dict[str, Any]') -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if _is_supported_model(modelId):
            instrumentor._logger.debug(f"bedrock converse wrapper, modelId: {modelId}")
            return instrumentor.invoke_wrapper(
                _BedrockConverseSynchronousProviderRequest(instrumentor=instrumentor),
                _IsStreaming.false,
                wrapped,
                None,
                args,
                kwargs,
        )
        instrumentor._logger.debug(f"bedrock converse wrapper, unsupported modelId: {modelId}")
        return wrapped(*args, **kwargs)
    
    return invoke_wrapper

def wrap_converse_stream(instrumentor: _PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: Any) -> Any:
        modelId: str = kwargs.get("modelId", "") # type: ignore

        if _is_supported_model(modelId):
            instrumentor._logger.debug(f"bedrock converse stream wrapper, modelId: {modelId}")
            return instrumentor.invoke_wrapper(
                _BedrockConverseStreamingProviderRequest(instrumentor=instrumentor),
                _IsStreaming.true,
                wrapped,
                None,
                args,
                kwargs,
            )
        instrumentor._logger.debug(f"bedrock converse stream wrapper, unsupported modelId: {modelId}")
        return wrapped(*args, **kwargs)

    return invoke_wrapper

class _BedrockProviderRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(
            instrumentor=instrumentor,
            category=PayiCategories.aws_bedrock,
            streaming_type=_StreamingType.iterator,
            )

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        # boto3 doesn't allow extra_headers
        kwargs.pop("extra_headers", None)
        self._ingest["resource"] = kwargs.get("modelId", "")
        return True

    @override
    def process_exception(self, exception: Exception, kwargs: Any, ) -> bool:
        try:
            if hasattr(exception, "response"):
                response: dict[str, Any] = getattr(exception, "response", {})
                status_code: int = response.get('ResponseMetadata', {}).get('HTTPStatusCode', 0)
                if status_code == 0:
                    return False

                self._ingest["http_status_code"] = status_code
                
                request_id = response.get('ResponseMetadata', {}).get('RequestId', "")
                if request_id:
                    self._ingest["provider_response_id"] = request_id

                error = response.get('Error', "")
                if error:
                    self._ingest["provider_response_json"] = json.dumps(error)

            return True

        except Exception as e:
            self._instrumentor._logger.debug(f"Error processing exception: {e}")
            return False

class _BedrockInvokeStreamingProviderRequest(_BedrockProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor, model_id: str):
        super().__init__(instrumentor=instrumentor)
        self._is_anthropic: bool = model_id.startswith("anthropic.")

    @override
    def process_chunk(self, chunk: Any) -> bool:
        if self._is_anthropic:
            return self.process_invoke_streaming_anthropic_chunk(chunk)
        else:
            return self.process_invoke_streaming_llama_chunk(chunk)

    def process_invoke_streaming_anthropic_chunk(self, chunk: str) -> bool:
        chunk_dict =  json.loads(chunk)
        type = chunk_dict.get("type", "")

        if type == "message_start":
            usage = chunk_dict['message']['usage']
            units = self._ingest["units"]

            input = _PayiInstrumentor.update_for_vision(usage['input_tokens'], units, self._estimated_prompt_tokens)

            units["text"] = Units(input=input, output=0)

            text_cache_write: int = usage.get("cache_creation_input_tokens", 0)
            if text_cache_write > 0:
                units["text_cache_write"] = Units(input=text_cache_write, output=0)

            text_cache_read: int = usage.get("cache_read_input_tokens", 0)
            if text_cache_read > 0:
                units["text_cache_read"] = Units(input=text_cache_read, output=0)

        elif type == "message_delta":
            usage = chunk_dict['usage']
            self._ingest["units"]["text"]["output"] = usage['output_tokens']

        return True    

    def process_invoke_streaming_llama_chunk(self, chunk: str) -> bool:
        chunk_dict =  json.loads(chunk)
        metrics = chunk_dict.get("amazon-bedrock-invocationMetrics", {})
        if metrics:
            input = metrics.get("inputTokenCount", 0)
            output = metrics.get("outputTokenCount", 0)
            self._ingest["units"]["text"] = Units(input=input, output=output)

        return True

class _BedrockInvokeSynchronousProviderRequest(_BedrockProviderRequest):
    @override
    def process_synchronous_response(
        self,
        response: Any,
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:

        metadata = response.get("ResponseMetadata", {})

        request_id = metadata.get("RequestId", "")
        if request_id:
            self._ingest["provider_response_id"] = request_id

        response_headers = metadata.get("HTTPHeaders", {}).copy()
        if response_headers:
            self._ingest["provider_response_headers"] = [PayICommonModelsAPIRouterHeaderInfoParam(name=k, value=v) for k, v in response_headers.items()]

        response["body"] = InvokeResponseWrapper(
            response=response["body"],
            instrumentor=self._instrumentor,
            ingest=self._ingest,
            log_prompt_and_response=log_prompt_and_response)

        return response

class _BedrockConverseSynchronousProviderRequest(_BedrockProviderRequest):
    @override
    def process_synchronous_response(
        self,
        response: 'dict[str, Any]',
        log_prompt_and_response: bool,
        kwargs: Any) -> Any:

        usage = response["usage"]
        input = usage["inputTokens"]
        output = usage["outputTokens"]
        
        units: dict[str, Units] = self._ingest["units"]
        units["text"] = Units(input=input, output=output)

        metadata = response.get("ResponseMetadata", {})

        request_id = metadata.get("RequestId", "")
        if request_id:
            self._ingest["provider_response_id"] = request_id

        response_headers = metadata.get("HTTPHeaders", {})
        if response_headers:
            self._ingest["provider_response_headers"] = [PayICommonModelsAPIRouterHeaderInfoParam(name=k, value=v) for k, v in response_headers.items()]

        if log_prompt_and_response:
            response_without_metadata = response.copy()
            response_without_metadata.pop("ResponseMetadata", None)
            self._ingest["provider_response_json"] = json.dumps(response_without_metadata)

        return None    

class _BedrockConverseStreamingProviderRequest(_BedrockProviderRequest):
    @override
    def process_chunk(self, chunk: 'dict[str, Any]') -> bool:
        metadata = chunk.get("metadata", {})

        if metadata:
            usage = metadata['usage']
            input = usage["inputTokens"]
            output = usage["outputTokens"]
            self._ingest["units"]["text"] = Units(input=input, output=output)

        return True