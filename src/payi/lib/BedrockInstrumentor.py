import json
import logging
from typing import Any
from functools import wraps

from wrapt import ObjectProxy, wrap_function_wrapper  # type: ignore

from payi.types.ingest_units_params import Units, IngestUnitsParams
from payi.types.pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

from .instrument import IsStreaming, PayiInstrumentor


class BedrockInstrumentor:
    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
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
            logging.debug(f"Error instrumenting bedrock: {e}")
            return

@PayiInstrumentor.payi_wrapper
def create_client_wrapper(instrumentor: PayiInstrumentor, wrapped: Any, instance: Any, *args: Any, **kwargs: Any) -> Any: #  noqa: ARG001
    if kwargs.get("service_name") != "bedrock-runtime":
        return wrapped(*args, **kwargs)

    try:
        client: Any = wrapped(*args, **kwargs)
        client.invoke_model = wrap_invoke(instrumentor, client.invoke_model)
        client.invoke_model_with_response_stream = wrap_invoke_stream(instrumentor, client.invoke_model_with_response_stream)
        client.converse = wrap_converse(instrumentor, client.converse)
        client.converse_stream = wrap_converse_stream(instrumentor, client.converse_stream)

        return client
    except Exception as e:
        logging.debug(f"Error instrumenting bedrock client: {e}")
    
    return wrapped(*args, **kwargs)
    
class InvokeResponseWrapper(ObjectProxy): # type: ignore
    def __init__(
        self,
        response: Any,
        instrumentor: PayiInstrumentor,
        ingest: IngestUnitsParams,
        log_prompt_and_response: bool
        ) -> None:

        super().__init__(response) # type: ignore
        self._response = response
        self._instrumentor = instrumentor
        self._ingest = ingest
        self._log_prompt_and_response = log_prompt_and_response

    def read(self, amt: Any =None): # type: ignore
        # data is array of bytes
        data: Any = self.__wrapped__.read(amt) # type: ignore
        response = json.loads(data)

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
            self._ingest["provider_response_json"] = data.decode('utf-8')
            
        self._instrumentor._ingest_units(self._ingest)

        return data

def wrap_invoke(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: 'dict[str, Any]') -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                "system.aws.bedrock",
                None,
                process_invoke_request,  
                process_synchronous_invoke_response,  
                IsStreaming.false,
                wrapped,
                None,
                args,
                kwargs,
        )
        return wrapped(*args, **kwargs)
    
    return invoke_wrapper

def wrap_invoke_stream(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: Any) -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                "system.aws.bedrock",
                process_invoke_streaming_anthropic_chunk if modelId.startswith("anthropic.") else process_invoke_streaming_llama_chunk,
                process_invoke_request, 
                None,  
                IsStreaming.true,
                wrapped,
                None,
                args,
                kwargs,
            )
        return wrapped(*args, **kwargs)

    return invoke_wrapper

def wrap_converse(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: 'dict[str, Any]') -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                "system.aws.bedrock",
                None,
                process_converse_request,  
                process_synchronous_converse_response,  
                IsStreaming.false,
                wrapped,
                None,
                args,
                kwargs,
        )
        return wrapped(*args, **kwargs)
    
    return invoke_wrapper

def wrap_converse_stream(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: Any) -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                "system.aws.bedrock",
                process_converse_streaming_chunk,
                process_converse_request, 
                None,  
                IsStreaming.true,
                wrapped,
                None,
                args,
                kwargs,
            )
        return wrapped(*args, **kwargs)

    return invoke_wrapper

def process_invoke_streaming_anthropic_chunk(chunk: str, ingest: IngestUnitsParams) -> None:
    chunk_dict =  json.loads(chunk)
    type = chunk_dict.get("type", "")

    if type == "message_start":
        usage = chunk_dict['message']['usage']
        units = ingest["units"]

        input = PayiInstrumentor.update_for_vision(usage['input_tokens'], units)

        units["text"] = Units(input=input, output=0)

        text_cache_write: int = usage.get("cache_creation_input_tokens", 0)
        if text_cache_write > 0:
            units["text_cache_write"] = Units(input=text_cache_write, output=0)

        text_cache_read: int = usage.get("cache_read_input_tokens", 0)
        if text_cache_read > 0:
            units["text_cache_read"] = Units(input=text_cache_read, output=0)

    elif type == "message_delta":
        usage = chunk_dict['usage']
        ingest["units"]["text"]["output"] = usage['output_tokens']

def process_invoke_streaming_llama_chunk(chunk: str, ingest: IngestUnitsParams) -> None:
    chunk_dict =  json.loads(chunk)
    metrics = chunk_dict.get("amazon-bedrock-invocationMetrics", {})
    if metrics:
        input = metrics.get("inputTokenCount", 0)
        output = metrics.get("outputTokenCount", 0)
        ingest["units"]["text"] = Units(input=input, output=output)
    
def process_synchronous_invoke_response(
        response: Any,
        ingest: IngestUnitsParams,
        log_prompt_and_response: bool,
        instrumentor: PayiInstrumentor,
        **kargs: Any) -> Any: #  noqa: ARG001

    metadata = response.get("ResponseMetadata", {})

    request_id = metadata.get("RequestId", "")
    if request_id:
        ingest["provider_response_id"] = request_id

    response_headers = metadata.get("HTTPHeaders", {}).copy()
    if response_headers:
        ingest["provider_response_headers"] = [PayICommonModelsAPIRouterHeaderInfoParam(name=k, value=v) for k, v in response_headers.items()]

    response["body"] = InvokeResponseWrapper(
        response=response["body"],
        instrumentor=instrumentor,
        ingest=ingest,
        log_prompt_and_response=log_prompt_and_response)

    return response

def process_invoke_request(ingest: IngestUnitsParams, *args: Any, **kwargs: Any) -> None: #  noqa: ARG001
    return

def process_converse_streaming_chunk(chunk: 'dict[str, Any]', ingest: IngestUnitsParams) -> None:
    metadata = chunk.get("metadata", {})

    if metadata:
        usage = metadata['usage']
        input = usage["inputTokens"]
        output = usage["outputTokens"]
        ingest["units"]["text"] = Units(input=input, output=output)

def process_synchronous_converse_response(
        response: 'dict[str, Any]',
        ingest: IngestUnitsParams,
        log_prompt_and_response: bool,
        **kargs: Any) -> Any: #  noqa: ARG001

    usage = response["usage"]
    input = usage["inputTokens"]
    output = usage["outputTokens"]
    
    units: dict[str, Units] = ingest["units"]
    units["text"] = Units(input=input, output=output)

    metadata = response.get("ResponseMetadata", {})

    request_id = metadata.get("RequestId", "")
    if request_id:
        ingest["provider_response_id"] = request_id

    response_headers = metadata.get("HTTPHeaders", {})
    if response_headers:
        ingest["provider_response_headers"] = [PayICommonModelsAPIRouterHeaderInfoParam(name=k, value=v) for k, v in response_headers.items()]

    if log_prompt_and_response:
        response_without_metadata = response.copy()
        response_without_metadata.pop("ResponseMetadata", None)
        ingest["provider_response_json"] = json.dumps(response_without_metadata)

    return None    

def process_converse_request(ingest: IngestUnitsParams, *args: Any, **kwargs: Any) -> None: #  noqa: ARG001
    return
