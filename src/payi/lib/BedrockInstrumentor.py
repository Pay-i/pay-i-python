import json
import logging
from typing import Any
from functools import wraps

from wrapt import ObjectProxy, wrap_function_wrapper  # type: ignore

from payi.types.ingest_units_params import Units, IngestUnitsParams

from .instrument import IsStreaming, PayiInstrumentor


class BedrockInstrumentor:
    @staticmethod
    def instrument(instrumentor: PayiInstrumentor) -> None:
        try:
            import boto3  # type: ignore #  noqa: F401  I001

            # wrap_function_wrapper(
            #     "anthropic.resources.completions",
            #     "Completions.create",
            #     chat_wrapper(instrumentor),
            # )

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
def create_client_wrapper(instrumentor: PayiInstrumentor, wrapped: Any, instance: Any, args: Any, kwargs: Any) -> Any: #  noqa: ARG001
    if kwargs.get("service_name") != "bedrock-runtime":
        return wrapped(*args, **kwargs)

    try:
        client: Any = wrapped(*args, **kwargs)
        client.invoke_model = wrap_invoke(instrumentor, client.invoke_model)
        client.invoke_model_with_response_stream = wrap_streaming_invoke(instrumentor, client.invoke_model_with_response_stream)

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
        
        # if hasattr(usage, "cache_creation_input_tokens") and usage.cache_creation_input_tokens > 0:
        #     text_cache_write = usage.cache_creation_input_tokens
        #     units["text_cache_write"] = Units(input=text_cache_write, output=0)

        # if hasattr(usage, "cache_read_input_tokens") and usage.cache_read_input_tokens > 0:
        #     text_cache_read = usage.cache_read_input_tokens
        #     units["text_cache_read"] = Units(input=text_cache_read, output=0)

        # input = PayiInstrumentor.update_for_vision(input, units)

        units["text"] = Units(input=input, output=output)

        if self._log_prompt_and_response:
            self._ingest["provider_response_json"] = data.decode('utf-8')
            
        self._instrumentor._ingest_units(self._ingest)

        return data

def wrap_invoke(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: 'dict[str, Any]') -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore TODO get resource name

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                category="system.aws.bedrock",
                process_chunk=process_chunk,
                process_request=process_request,  
                process_synchronous_response=process_synchronous_invoke_response,  
                is_streaming=IsStreaming.false,
                wrapped=wrapped,
                instance=None,
                args=args,
                kwargs=kwargs,
        )
        return wrapped(*args, **kwargs)
    
    return invoke_wrapper

def wrap_streaming_invoke(instrumentor: PayiInstrumentor, wrapped: Any) -> Any:
    @wraps(wrapped)
    def invoke_wrapper(*args: Any, **kwargs: Any) -> Any:
        modelId:str = kwargs.get("modelId", "") # type: ignore TODO get resource name

        if modelId.startswith("meta.llama3") or modelId.startswith("anthropic."):
            return instrumentor.chat_wrapper(
                category="system.aws.bedrock",
                process_chunk=process_chunk,
                process_request=process_request, 
                process_synchronous_response=None,  
                is_streaming=IsStreaming.true,
                wrapped=wrapped,
                instance=None,
                args=args,
                kwargs=kwargs,
            )
        return wrapped(*args, **kwargs)

    return invoke_wrapper

def process_chunk(chunk: Any, ingest: IngestUnitsParams) -> None:
    if not chunk:
        return

        # response: Any,
        # instrumentor: PayiInstrumentor,
        # ingest: IngestUnitsParams,
        # log_prompt_and_response: bool

def process_synchronous_invoke_response(
        response: Any,
        ingest: IngestUnitsParams,
        log_prompt_and_response: bool,
        instrumentor: PayiInstrumentor,
        **kargs: Any) -> Any: #  noqa: ARG001
    
    response["body"] = InvokeResponseWrapper(
        response=response["body"],
        instrumentor=instrumentor,
        ingest=ingest,
        log_prompt_and_response=log_prompt_and_response)

    return response

def process_request(ingest: IngestUnitsParams, kwargs: Any) -> None: #  noqa: ARG001
    return
    # messages = kwargs.get("messages")
    # if not messages or len(messages) == 0:
    #     return
    
    # estimated_token_count = 0 
    # has_image = False

    # enc = tiktoken.get_encoding("cl100k_base")
    
    # for message in messages:
    #     msg_has_image, msg_prompt_tokens = has_image_and_get_texts(enc, message.get('content', ''))
    #     if msg_has_image:
    #         has_image = True
    #         estimated_token_count += msg_prompt_tokens
    
    # if not has_image or estimated_token_count == 0:
    #     return

    # ingest["units"][PayiInstrumentor.estimated_prompt_tokens] = Units(input=estimated_token_count, output=0)
