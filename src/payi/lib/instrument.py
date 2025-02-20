import json
import uuid
import asyncio
import inspect
import logging
import traceback
from enum import Enum
from typing import Any, Set, Union, Callable, Optional, TypedDict

import nest_asyncio  # type: ignore
from wrapt import ObjectProxy  # type: ignore

from payi import Payi, AsyncPayi
from payi.types import IngestUnitsParams
from payi.lib.helpers import PayiHeaderNames
from payi.types.ingest_response import IngestResponse
from payi.types.ingest_units_params import Units
from payi.types.pay_i_common_models_api_router_header_info_param import PayICommonModelsAPIRouterHeaderInfoParam

from .helpers import PayiCategories
from .Stopwatch import Stopwatch


class Context(TypedDict, total=False):
    proxy: bool
    experience_name: Optional[str]
    experience_id: Optional[str]
    limit_ids: Optional['list[str]']
    request_tags: Optional['list[str]']
    user_id: Optional[str]

class IsStreaming(Enum):
    false = 0
    true = 1 
    kwargs = 2

class PayiInstrumentor:
    estimated_prompt_tokens: str = "estimated_prompt_tokens"

    def __init__(
        self,
        payi: Optional[Payi],
        apayi: Optional[AsyncPayi],
        instruments: Union[Set[str], None] = None,
        log_prompt_and_response: bool = True,
        prompt_and_response_logger: Optional[
            Callable[[str, "dict[str, str]"], None]
        ] = None,  # (request id, dict of data to store) -> None
    ):
        self._payi: Optional[Payi] = payi
        self._apayi: Optional[AsyncPayi] = apayi
        self._context_stack: list[Context] = []  # Stack of context dictionaries
        self._log_prompt_and_response: bool = log_prompt_and_response
        self._prompt_and_response_logger: Optional[Callable[[str, dict[str, str]], None]] = prompt_and_response_logger

        self._blocked_limits: set[str] = set()
        self._exceeded_limits: set[str] = set()

        if instruments is None or "*" in instruments:
            self._instrument_all()
        else:
            self._instrument_specific(instruments)

    def _instrument_all(self) -> None:
        self._instrument_openai()
        self._instrument_anthropic()
        self._instrument_aws_bedrock()

    def _instrument_specific(self, instruments: Set[str]) -> None:
        if PayiCategories.openai in instruments or PayiCategories.azure_openai in instruments:
            self._instrument_openai()
        if PayiCategories.anthropic in instruments:
            self._instrument_anthropic()
        if PayiCategories.aws_bedrock in instruments:
            self._instrument_aws_bedrock()

    def _instrument_openai(self) -> None:
        from .OpenAIInstrumentor import OpenAiInstrumentor

        try:
            OpenAiInstrumentor.instrument(self)

        except Exception as e:
            logging.error(f"Error instrumenting OpenAI: {e}")

    def _instrument_anthropic(self) -> None:
        from .AnthropicInstrumentor import AnthropicIntrumentor

        try:
            AnthropicIntrumentor.instrument(self)

        except Exception as e:
            logging.error(f"Error instrumenting Anthropic: {e}")

    def _instrument_aws_bedrock(self) -> None:
        from .BedrockInstrumentor import BedrockInstrumentor

        try:
            BedrockInstrumentor.instrument(self)

        except Exception as e:
            logging.error(f"Error instrumenting AWS bedrock: {e}")

    def _process_ingest_units(self, ingest_units: IngestUnitsParams, log_data: 'dict[str, str]') -> bool:
        if int(ingest_units.get("http_status_code") or 0) < 400:
            units = ingest_units.get("units", {})
            if not units or all(unit.get("input", 0) == 0 and unit.get("output", 0) == 0 for unit in units.values()):
                logging.error(
                    'No units to ingest.  For OpenAI streaming calls, make sure you pass stream_options={"include_usage": True}'
                )
                return False

        if self._log_prompt_and_response and self._prompt_and_response_logger:
            response_json = ingest_units.pop("provider_response_json", None)
            request_json = ingest_units.pop("provider_request_json", None)
            stack_trace = ingest_units.get("properties", {}).pop("system.stack_trace", None)  # type: ignore

            if response_json is not None:
                # response_json is a list of strings, convert a single json string
                log_data["provider_response_json"] = json.dumps(response_json)
            if request_json is not None:
                log_data["provider_request_json"] = request_json
            if stack_trace is not None:
                log_data["stack_trace"] = stack_trace

        return True

    def _process_ingest_units_response(self, ingest_response: IngestResponse) -> None:
        if ingest_response.xproxy_result.limits:
            for limit_id, state in ingest_response.xproxy_result.limits.items():
                removeBlockedId: bool = False

                if state.state == "blocked":
                    self._blocked_limits.add(limit_id)
                elif state.state == "exceeded":
                    self._exceeded_limits.add(limit_id)
                    removeBlockedId = True
                elif state.state == "ok":
                    removeBlockedId = True

                # opportunistically remove blocked limits
                if removeBlockedId:
                    self._blocked_limits.discard(limit_id)

    async def _aingest_units(self, ingest_units: IngestUnitsParams) -> Optional[IngestResponse]:
        ingest_response: Optional[IngestResponse] = None
    
        # return early if there are no units to ingest and on a successul ingest request
        log_data: 'dict[str,str]' = {}
        if not self._process_ingest_units(ingest_units, log_data):
            return None

        try:
            if self._apayi:    
                ingest_response= await self._apayi.ingest.units(**ingest_units)
            elif self._payi:
                ingest_response = self._payi.ingest.units(**ingest_units)
            else:
                logging.error("No payi instance to ingest units")
                return None         

            if ingest_response:
                self._process_ingest_units_response(ingest_response)

                if ingest_response and self._log_prompt_and_response and self._prompt_and_response_logger:
                    request_id = ingest_response.xproxy_result.request_id
                    self._prompt_and_response_logger(request_id, log_data)  # type: ignore

            return ingest_response
        except Exception as e:
            logging.error(f"Error Pay-i ingesting result: {e}")
    
        return None         
    
    def _call_aingest_sync(self, ingest_units: IngestUnitsParams) -> Optional[IngestResponse]:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None
        
        try:
            if loop and loop.is_running():
                nest_asyncio.apply(loop) # type: ignore
                return asyncio.run(self._aingest_units(ingest_units))                
            else:
                # When there's no running loop, create a new one
                return asyncio.run(self._aingest_units(ingest_units))
        except Exception as e:
            logging.error(f"Error calling aingest_units synchronously: {e}")
        return None
        
    def _ingest_units(self, ingest_units: IngestUnitsParams) -> Optional[IngestResponse]:
        ingest_response: Optional[IngestResponse] = None
        
        # return early if there are no units to ingest and on a successul ingest request
        log_data: 'dict[str,str]' = {}
        if not self._process_ingest_units(ingest_units, log_data):
            return None

        try:
            if self._payi:
                ingest_response = self._payi.ingest.units(**ingest_units)
                self._process_ingest_units_response(ingest_response)

                if self._log_prompt_and_response and self._prompt_and_response_logger:
                    request_id = ingest_response.xproxy_result.request_id
                    self._prompt_and_response_logger(request_id, log_data)  # type: ignore

                return ingest_response
            elif self._apayi:
                # task runs async. aingest_units will invoke the callback and post process
                ingest_response = self._call_aingest_sync(ingest_units)
                return ingest_response
            else:
                logging.error("No payi instance to ingest units")

        except Exception as e:
            logging.error(f"Error Pay-i ingesting result: {e}")
        
        return None

    def _setup_call_func(
        self
        ) -> 'tuple[Context, Optional[str], Optional[str]]':
        context: Context = {}

        if len(self._context_stack) > 0:
            # copy current context into the upcoming context
            context = self._context_stack[-1].copy()
            context.pop("proxy")
            previous_experience_name = context.get("experience_name", None)
            previous_experience_id = context.get("experience_id", None)
        else:
            previous_experience_name = None
            previous_experience_id = None
        return (context, previous_experience_name, previous_experience_id)

    def _init_context(
        self,
        context: Context,
        previous_experience_name: Optional[str],
        previous_experience_id: Optional[str],
        proxy: bool,
        limit_ids: Optional["list[str]"],
        request_tags: Optional["list[str]"],
        experience_name: Optional[str],
        experience_id: Optional[str],
        user_id: Optional[str],
        ) -> None:
        context["proxy"] = proxy

        # Handle experience name and ID logic
        if not experience_name:
            # If no experience_name specified, use previous values
            context["experience_name"] = previous_experience_name
            context["experience_id"] = previous_experience_id
        else:
            # If experience_name is specified
            if experience_name == previous_experience_name:
                # Same experience name, use previous ID unless new one specified
                context["experience_name"] = experience_name
                context["experience_id"] = experience_id if experience_id else previous_experience_id
            else:
                # Different experience name, use specified ID or generate one
                context["experience_name"] = experience_name
                context["experience_id"] = experience_id if experience_id else str(uuid.uuid4())

        # set any values explicitly passed by the caller, otherwise use what is already in the context
        if limit_ids:
            context["limit_ids"] = limit_ids
        if request_tags:
            context["request_tags"] = request_tags
        if user_id:
            context["user_id"] = user_id

        self.set_context(context)
        
    async def _acall_func(
        self,
        func: Any,
        proxy: bool,
        limit_ids: Optional["list[str]"],
        request_tags: Optional["list[str]"],
        experience_name: Optional[str],
        experience_id: Optional[str],
        user_id: Optional[str],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        context, previous_experience_name, previous_experience_id = self._setup_call_func()

        with self:
            self._init_context(
                context,
                previous_experience_name,
                previous_experience_id,
                proxy, 
                limit_ids, 
                request_tags,
                experience_name,
                experience_id,
                user_id)
            return await func(*args, **kwargs)

    def _call_func(
        self,
        func: Any,
        proxy: bool,
        limit_ids: Optional["list[str]"],
        request_tags: Optional["list[str]"],
        experience_name: Optional[str],
        experience_id: Optional[str],
        user_id: Optional[str],
        *args: Any,
        **kwargs: Any,
    ) -> Any:
        context, previous_experience_name, previous_experience_id = self._setup_call_func()

        with self:
            self._init_context(
                context,
                previous_experience_name,
                previous_experience_id,
                proxy, 
                limit_ids, 
                request_tags,
                experience_name,
                experience_id,
                user_id)
            return func(*args, **kwargs)

    def __enter__(self) -> Any:
        # Push a new context dictionary onto the stack
        self._context_stack.append({})
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        # Pop the current context off the stack
        if self._context_stack:
            self._context_stack.pop()

    def set_context(self, context: Context) -> None:
        # Update the current top of the stack with the provided context
        if self._context_stack:
            self._context_stack[-1].update(context)

    def get_context(self) -> Optional[Context]:
        # Return the current top of the stack
        return self._context_stack[-1] if self._context_stack else None


    def _prepare_ingest(
        self,
        ingest: IngestUnitsParams,
        ingest_extra_headers: "dict[str, str]", # do not coflict potential kwargs["extra_headers"]
        **kwargs: Any,
    ) -> None:
        limit_ids = ingest_extra_headers.pop(PayiHeaderNames.limit_ids, None)
        request_tags = ingest_extra_headers.pop(PayiHeaderNames.request_tags, None)
        experience_name = ingest_extra_headers.pop(PayiHeaderNames.experience_name, None)
        experience_id = ingest_extra_headers.pop(PayiHeaderNames.experience_id, None)
        user_id = ingest_extra_headers.pop(PayiHeaderNames.user_id, None)

        if limit_ids:
            ingest["limit_ids"] = limit_ids.split(",")
        if request_tags:
            ingest["request_tags"] = request_tags.split(",")
        if experience_name:
            ingest["experience_name"] = experience_name
        if experience_id:
            ingest["experience_id"] = experience_id
        if user_id:
            ingest["user_id"] = user_id

        if len(ingest_extra_headers) > 0:
            ingest["provider_request_headers"] = [PayICommonModelsAPIRouterHeaderInfoParam(name=k, value=v) for k, v in ingest_extra_headers.items()]

        provider_prompt: "dict[str, Any]" = {}
        for k, v in kwargs.items():
            if k == "messages":
                provider_prompt[k] = [m.model_dump() if hasattr(m, "model_dump") else m for m in v]
            elif k in ["extra_headers", "extra_query"]:
                pass
            else:
                try:
                    json.dumps(v)
                    provider_prompt[k] = v
                except (TypeError, ValueError):
                    pass

        if self._log_prompt_and_response:
            ingest["provider_request_json"] = json.dumps(provider_prompt)

    async def achat_wrapper(
        self,
        category: str,
        process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]],
        process_request: Optional[Callable[[IngestUnitsParams, Any, Any], None]],
        process_synchronous_response: Any,
        is_streaming: IsStreaming,
        wrapped: Any,
        instance: Any,
        args: Any,
        kwargs: Any,
    ) -> Any:
        context = self.get_context()

        # Bedrock client does not have an async method

        if not context:   
            # wrapped function invoked outside of decorator scope
            return await wrapped(*args, **kwargs)

        # after _udpate_headers, all metadata to add to ingest is in extra_headers, keyed by the xproxy-xxx header name
        extra_headers = kwargs.get("extra_headers", {})
        self._update_headers(context, extra_headers)

        if context.get("proxy", True):
            if "extra_headers" not in kwargs:
                kwargs["extra_headers"] = extra_headers

            return await wrapped(*args, **kwargs)

        ingest: IngestUnitsParams = {"category": category, "units": {}} # type: ignore
        ingest["resource"] = kwargs.get("model", "")

        if category == PayiCategories.openai and instance and hasattr(instance, "_client"):
            from .OpenAIInstrumentor import OpenAiInstrumentor # noqa: I001

            if OpenAiInstrumentor.is_azure(instance):
                route_as_resource = extra_headers.pop(PayiHeaderNames.route_as_resource, None)
                resource_scope = extra_headers.pop(PayiHeaderNames.resource_scope, None)

                if not route_as_resource:
                    logging.error("Azure OpenAI route as resource not found, not ingesting")
                    return await wrapped(*args, **kwargs)

                if resource_scope:
                    if not(resource_scope in ["global", "datazone"] or resource_scope.startswith("region")):
                        logging.error("Azure OpenAI invalid resource scope, not ingesting")
                        return wrapped(*args, **kwargs)

                    ingest["resource_scope"] = resource_scope

                category = PayiCategories.azure_openai

                ingest["category"] = category
                ingest["resource"] = route_as_resource

        current_frame = inspect.currentframe()
        # f_back excludes the current frame, strip() cleans up whitespace and newlines
        stack = [frame.strip() for frame in traceback.format_stack(current_frame.f_back)]  # type: ignore

        ingest['properties'] = { 'system.stack_trace': json.dumps(stack) }

        if process_request:
            process_request(ingest, (), instance)

        sw = Stopwatch()
        stream: bool = False
        
        if is_streaming == IsStreaming.kwargs:
            stream = kwargs.get("stream", False)
        elif is_streaming == IsStreaming.true:
            stream = True
        else:
            stream = False

        try:
            self._prepare_ingest(ingest, extra_headers, **kwargs)
            sw.start()
            response = await wrapped(*args, **kwargs)

        except Exception as e:  # pylint: disable=broad-except
            sw.stop()
            duration = sw.elapsed_ms_int()

            # TODO ingest error

            raise e

        if stream:
            stream_result = ChatStreamWrapper(
                response=response,
                instance=instance,
                instrumentor=self,
                log_prompt_and_response=self._log_prompt_and_response,
                ingest=ingest,
                stopwatch=sw,
                process_chunk=process_chunk,
                is_bedrock=False,
            )

            return stream_result

        sw.stop()
        duration = sw.elapsed_ms_int()
        ingest["end_to_end_latency_ms"] = duration
        ingest["http_status_code"] = 200

        if process_synchronous_response:
            return_result: Any = process_synchronous_response(
                response=response,
                ingest=ingest,
                log_prompt_and_response=self._log_prompt_and_response,
                instrumentor=self)
            if return_result:
                return return_result

        await self._aingest_units(ingest)

        return response

    def chat_wrapper(
        self,
        category: str,
        process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]],
        process_request: Optional[Callable[[IngestUnitsParams, Any, Any], None]],
        process_synchronous_response: Any,
        is_streaming: IsStreaming,
        wrapped: Any,
        instance: Any,
        args: Any,
        kwargs: Any,
    ) -> Any:
        context = self.get_context()

        is_bedrock:bool = category == PayiCategories.aws_bedrock

        if not context:
            if is_bedrock:
                # boto3 doesn't allow extra_headers
                kwargs.pop("extra_headers", None)
    
            # wrapped function invoked outside of decorator scope
            return wrapped(*args, **kwargs)

        # after _udpate_headers, all metadata to add to ingest is in extra_headers, keyed by the xproxy-xxx header name
        extra_headers = kwargs.get("extra_headers", {})
        self._update_headers(context, extra_headers)

        if context.get("proxy", True):
            if "extra_headers" not in kwargs:
                kwargs["extra_headers"] = extra_headers

            return wrapped(*args, **kwargs)
        
        ingest: IngestUnitsParams = {"category": category, "units": {}} # type: ignore
        if is_bedrock:
            # boto3 doesn't allow extra_headers
            kwargs.pop("extra_headers", None)
            ingest["resource"] = kwargs.get("modelId", "")
        else:
            ingest["resource"] = kwargs.get("model", "")

        if category == PayiCategories.openai and instance and hasattr(instance, "_client"):
            from .OpenAIInstrumentor import OpenAiInstrumentor # noqa: I001

            if OpenAiInstrumentor.is_azure(instance):
                route_as_resource:str = extra_headers.pop(PayiHeaderNames.route_as_resource, None)
                resource_scope:str = extra_headers.pop(PayiHeaderNames.resource_scope, None)

                if not route_as_resource:
                    logging.error("Azure OpenAI route as resource not found, not ingesting")
                    return wrapped(*args, **kwargs)

                if resource_scope:
                    if not(resource_scope in ["global", "datazone"] or resource_scope.startswith("region")):
                        logging.error("Azure OpenAI invalid resource scope, not ingesting")
                        return wrapped(*args, **kwargs)

                    ingest["resource_scope"] = resource_scope

                category = PayiCategories.azure_openai

                ingest["category"] = category
                ingest["resource"] = route_as_resource

        current_frame = inspect.currentframe()
        # f_back excludes the current frame, strip() cleans up whitespace and newlines
        stack = [frame.strip() for frame in traceback.format_stack(current_frame.f_back)]  # type: ignore

        ingest['properties'] = { 'system.stack_trace': json.dumps(stack) }

        if process_request:
            process_request(ingest, (), kwargs)

        sw = Stopwatch()
        stream: bool = False
        
        if is_streaming == IsStreaming.kwargs:
            stream = kwargs.get("stream", False)
        elif is_streaming == IsStreaming.true:
            stream = True
        else:
            stream = False

        try:
            self._prepare_ingest(ingest, extra_headers, **kwargs)
            sw.start()
            response = wrapped(*args, **kwargs)

        except Exception as e:  # pylint: disable=broad-except
            sw.stop()
            duration = sw.elapsed_ms_int()

            # TODO ingest error

            raise e

        if stream:
            stream_result = ChatStreamWrapper(
                response=response,
                instance=instance,
                instrumentor=self,
                log_prompt_and_response=self._log_prompt_and_response,
                ingest=ingest,
                stopwatch=sw,
                process_chunk=process_chunk,
                is_bedrock=is_bedrock,
            )

            if is_bedrock:
                if "body" in response:
                    response["body"] = stream_result
                else:
                    response["stream"] = stream_result
                return response
            
            return stream_result

        sw.stop()
        duration = sw.elapsed_ms_int()
        ingest["end_to_end_latency_ms"] = duration
        ingest["http_status_code"] = 200

        if process_synchronous_response:
            return_result: Any = process_synchronous_response(
                response=response,
                ingest=ingest,
                log_prompt_and_response=self._log_prompt_and_response,
                instrumentor=self)
            if return_result:
                return return_result

        self._ingest_units(ingest)

        return response

    @staticmethod
    def _update_headers(
        context: Context,
        extra_headers: "dict[str, str]",
    ) -> None:
        limit_ids: Optional[list[str]] = context.get("limit_ids")
        request_tags: Optional[list[str]] = context.get("request_tags")
        experience_name: Optional[str] = context.get("experience_name")
        experience_id: Optional[str] = context.get("experience_id")
        user_id: Optional[str] = context.get("user_id")

        # Merge limits from the decorator and extra headers
        if limit_ids is not None:
            existing_limit_ids = extra_headers.get(PayiHeaderNames.limit_ids, None)
            
            if not existing_limit_ids:
                extra_headers[PayiHeaderNames.limit_ids] = ",".join(limit_ids)
            else:
                existing_ids = existing_limit_ids.split(',')
                combined_ids = list(set(existing_ids + limit_ids))
                extra_headers[PayiHeaderNames.limit_ids] = ",".join(combined_ids)

        # Merge request from the decorator and extra headers
        if request_tags is not None:
            existing_request_tags = extra_headers.get(PayiHeaderNames.request_tags, None)

            if not existing_request_tags:
                extra_headers[PayiHeaderNames.request_tags] = ",".join(request_tags)
            else:
                existing_tags = existing_request_tags.split(',')
                combined_tags = list(set(existing_tags + request_tags))
                extra_headers[PayiHeaderNames.request_tags] = ",".join(combined_tags)

        # inner extra_headers user_id takes precedence over outer decorator user_id
        if user_id is not None and extra_headers.get(PayiHeaderNames.user_id, None) is None:
            extra_headers[PayiHeaderNames.user_id] = user_id   

        # inner extra_headers experience_name and experience_id take precedence over outer decorator experience_name and experience_id
        # if either inner value is specified, ignore outer decorator values
        if PayiHeaderNames.experience_name not in extra_headers and PayiHeaderNames.experience_id not in extra_headers:

            # use both decorator values
            if experience_name is not None:
                extra_headers[PayiHeaderNames.experience_name] = experience_name
            if experience_id is not None:
                extra_headers[PayiHeaderNames.experience_id] = experience_id
        
        elif PayiHeaderNames.experience_id in extra_headers and PayiHeaderNames.experience_name not in extra_headers:
            # use the decorator experience name and the inner experience id
            if experience_name is not None:
                extra_headers[PayiHeaderNames.experience_name] = experience_name
        
        else:
            # use the inner experience name and id as-is
            ...

    @staticmethod
    def update_for_vision(input: int, units: 'dict[str, Units]') -> int:
        if PayiInstrumentor.estimated_prompt_tokens in units:
            prompt_token_estimate: int = units.pop(PayiInstrumentor.estimated_prompt_tokens)["input"] # type: ignore
            vision = input - prompt_token_estimate
            if (vision > 0):
                units["vision"] = Units(input=vision, output=0)
                input = prompt_token_estimate
        
        return input

    @staticmethod
    def payi_wrapper(func: Any) -> Any:
        def _payi_wrapper(o: Any) -> Any:
            def wrapper(wrapped: Any, instance: Any, args: Any, kwargs: Any) -> Any:
                return func(
                    o,
                    wrapped,
                    instance,
                    *args,
                    **kwargs,
                )

            return wrapper

        return _payi_wrapper

    @staticmethod
    def payi_awrapper(func: Any) -> Any:
        def _payi_awrapper(o: Any) -> Any:
            async def wrapper(wrapped: Any, instance: Any, args: Any, kwargs: Any) -> Any:
                return await func(
                    o,
                    wrapped,
                    instance,
                    *args,
                    **kwargs,
                )

            return wrapper

        return _payi_awrapper

class ChatStreamWrapper(ObjectProxy):  # type: ignore
    def __init__(
        self,
        response: Any,
        instance: Any,
        instrumentor: PayiInstrumentor,
        ingest: IngestUnitsParams,
        stopwatch: Stopwatch,
        process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]] = None,
        log_prompt_and_response: bool = True,
        is_bedrock: bool = False,
    ) -> None:

        bedrock_from_stream: bool = False
        if is_bedrock:
            ingest["provider_response_id"] = response["ResponseMetadata"]["RequestId"]
            stream = response.get("stream", None)

            if stream:
                response = stream
                bedrock_from_stream = True
            else:
                response = response.get("body")
                bedrock_from_stream = False

        super().__init__(response)  # type: ignore

        self._response = response
        self._instance = instance

        self._instrumentor = instrumentor
        self._stopwatch: Stopwatch = stopwatch
        self._ingest: IngestUnitsParams = ingest
        self._log_prompt_and_response: bool = log_prompt_and_response
        self._responses: list[str] = []

        self._process_chunk: Optional[Callable[[Any, IngestUnitsParams], None]] = process_chunk

        self._first_token: bool = True
        self._is_bedrock: bool = is_bedrock
        self._bedrock_from_stream: bool = bedrock_from_stream

    def __enter__(self) -> Any:
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: 
        self.__wrapped__.__exit__(exc_type, exc_val, exc_tb)  # type: ignore

    async def __aenter__(self) -> Any:
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.__wrapped__.__aexit__(exc_type, exc_val, exc_tb)  # type: ignore

    def __iter__(self) -> Any:  
        if self._is_bedrock:
            # MUST be reside in a separate function so that the yield statement doesn't implicitly return its own iterator and overriding self
            return self._iter_bedrock()
        return self

    def _iter_bedrock(self) -> Any:
        # botocore EventStream doesn't have a __next__ method so iterate over the wrapped object in place
        for event in self.__wrapped__: # type: ignore
            if (self._bedrock_from_stream):
                self._evaluate_chunk(event)
            else:
                chunk = event.get('chunk') # type: ignore
                if chunk:
                    decode = chunk.get('bytes').decode() # type: ignore
                    self._evaluate_chunk(decode)
            yield event

        self._stop_iteration()

    def __aiter__(self) -> Any:
        return self

    def __next__(self) -> Any:
        try:
            chunk: Any = self.__wrapped__.__next__()  # type: ignore
        except Exception as e:
            if isinstance(e, StopIteration):
                self._stop_iteration()
            raise e
        else:
            self._evaluate_chunk(chunk)
            return chunk

    async def __anext__(self) -> Any:
        try:
            chunk: Any = await self.__wrapped__.__anext__()  # type: ignore
        except Exception as e:
            if isinstance(e, StopAsyncIteration):
                await self._astop_iteration()
            raise e
        else:
            self._evaluate_chunk(chunk)
            return chunk

    def _evaluate_chunk(self, chunk: Any) -> None:
        if self._first_token:
            self._ingest["time_to_first_token_ms"] = self._stopwatch.elapsed_ms_int()
            self._first_token = False

        if self._log_prompt_and_response:
            self._responses.append(self.chunk_to_json(chunk))

        if self._process_chunk:
            self._process_chunk(chunk, self._ingest)

    def _process_stop_iteration(self) -> None:
        self._stopwatch.stop()
        self._ingest["end_to_end_latency_ms"] = self._stopwatch.elapsed_ms_int()
        self._ingest["http_status_code"] = 200

        if self._log_prompt_and_response:
            self._ingest["provider_response_json"] = self._responses

    async def _astop_iteration(self) -> None:
        self._process_stop_iteration()
        await self._instrumentor._aingest_units(self._ingest)

    def _stop_iteration(self) -> None:
        self._process_stop_iteration()
        self._instrumentor._ingest_units(self._ingest)

    @staticmethod
    def chunk_to_json(chunk: Any) -> str:
        if hasattr(chunk, "to_json"):
            return str(chunk.to_json())
        elif isinstance(chunk, bytes):
            return chunk.decode()
        elif isinstance(chunk, str):
            return chunk
        else:
            # assume dict
            return json.dumps(chunk)

global _instrumentor
_instrumentor: Optional[PayiInstrumentor] = None

def payi_instrument(
    payi: Optional[Union[Payi, AsyncPayi, 'list[Union[Payi, AsyncPayi]]']] = None,
    instruments: Optional[Set[str]] = None,
    log_prompt_and_response: bool = True,
    prompt_and_response_logger: Optional[Callable[[str, "dict[str, str]"], None]] = None,
) -> None:
    global _instrumentor
    if _instrumentor:
        return
    
    payi_param: Optional[Payi] = None
    apayi_param: Optional[AsyncPayi] = None

    if isinstance(payi, Payi):
        payi_param = payi
    elif isinstance(payi, AsyncPayi):
        apayi_param = payi
    elif isinstance(payi, list):
        for p in payi:
            if isinstance(p, Payi):
                payi_param = p
            elif isinstance(p, AsyncPayi): # type: ignore
                apayi_param = p

    # allow for both payi and apayi to be None for the @proxy case
    
    _instrumentor = PayiInstrumentor(
        payi=payi_param,
        apayi=apayi_param,
        instruments=instruments,
        log_prompt_and_response=log_prompt_and_response,
        prompt_and_response_logger=prompt_and_response_logger,
    )

def ingest(
    limit_ids: Optional["list[str]"] = None,
    request_tags: Optional["list[str]"] = None,
    experience_name: Optional[str] = None,
    experience_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Any:
    def _ingest(func: Any) -> Any:
        import asyncio
        if asyncio.iscoroutinefunction(func):
            async def awrapper(*args: Any, **kwargs: Any) -> Any:
                if not _instrumentor:
                    return await func(*args, **kwargs)
                # Call the instrumentor's _call_func for async functions
                return await _instrumentor._acall_func(
                    func,
                    False,
                    limit_ids,
                    request_tags,
                    experience_name,
                    experience_id,
                    user_id,
                    *args,
                    **kwargs,
                )
            return awrapper
        else:
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                if not _instrumentor:
                    return func(*args, **kwargs)
                return _instrumentor._call_func(
                    func,
                    False,
                    limit_ids,
                    request_tags,
                    experience_name,
                    experience_id,
                    user_id,
                    *args,
                    **kwargs,
                )
            return wrapper
    return _ingest

def proxy(
    limit_ids: Optional["list[str]"] = None,
    request_tags: Optional["list[str]"] = None,
    experience_name: Optional[str] = None,
    experience_id: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Any:
    def _proxy(func: Any) -> Any:
        import asyncio
        if asyncio.iscoroutinefunction(func):
            async def _proxy_awrapper(*args: Any, **kwargs: Any) -> Any:
                if not _instrumentor:
                    return await func(*args, **kwargs)
                return await _instrumentor._call_func(
                    func,
                    True,
                    limit_ids,
                    request_tags,
                    experience_name,
                    experience_id,
                    user_id,
                    *args,
                    **kwargs
                )

            return _proxy_awrapper
        else:
            def _proxy_wrapper(*args: Any, **kwargs: Any) -> Any:
                if not _instrumentor:
                    return func(*args, **kwargs)
                return _instrumentor._call_func(
                    func,
                    True,
                    limit_ids,
                    request_tags,
                    experience_name,
                    experience_id,
                    user_id,
                    *args,
                    **kwargs
                )

            return _proxy_wrapper

    return _proxy
