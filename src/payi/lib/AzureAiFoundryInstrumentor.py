import json
from typing import Any, Sequence
from typing_extensions import override

from wrapt import wrap_function_wrapper  # type: ignore

from payi.lib.helpers import PayiHeaderNames
from payi.types.ingest_units_params import Units

from .instrument import _ChunkResult, _IsStreaming, _StreamingType, _ProviderRequest, _PayiInstrumentor
from .version_helper import get_version_helper

AZURE_AI_FOUNDRY_CATEGORY = "azure.ai.foundry.agent"
AZURE_AI_FOUNDRY_RESOURCE = "builder"

UNIT_AGENT_CREATE = "agent_create"
UNIT_MESSAGE_CREATE = "message_create"
UNIT_TOOL_CALL = "tool_call"
UNIT_TOOL_CALL_OUTPUT = "tool_call_output"
UNIT_MESSAGE_RESPONSE = "message_response"

class AzureAiFoundryInstrumentor:
    _module_name: str = "azure-ai-projects"
    _module_version: str = ""

    @staticmethod
    def instrument(instrumentor: _PayiInstrumentor) -> None:
        try:
            AzureAiFoundryInstrumentor._module_version = get_version_helper(AzureAiFoundryInstrumentor._module_name)

            # Instrument agent operations
            wrap_function_wrapper(
                "azure.ai.agents",
                "AgentsClient.create_agent",
                agent_create_wrapper(instrumentor),
            )

            # Instrument thread operations
            # wrap_function_wrapper(
            #     "azure.ai.agents.operations",
            #     "ThreadsOperations.create",
            #     thread_create_wrapper(instrumentor),
            # )

            wrap_function_wrapper(
                "azure.ai.agents.operations",
                "MessagesOperations.create",
                message_create_wrapper(instrumentor),
            )

            wrap_function_wrapper(
                "azure.ai.agents.models",
                "ThreadMessage.__init__",
                thread_message_init_wrapper(instrumentor),
            )

            # Instrument run operations - this is where the main AI interaction happens
            wrap_function_wrapper(
                "azure.ai.agents.models",
                "ThreadRun.__init__",
                run_init_wrapper(instrumentor),
            )

            # wrap_function_wrapper(
            #     "azure.ai.agents.operations",
            #     "RunsOperations.create",
            #     run_create_wrapper(instrumentor),
            # )

            # wrap_function_wrapper(
            #     "azure.ai.agents.operations",
            #     "RunsOperations.create_and_process",
            #     run_create_and_process_wrapper(instrumentor),
            # )

            # TODO
            wrap_function_wrapper(
                "azure.ai.agents.operations",
                "RunsOperations.submit_tool_outputs",
                tool_outputs_wrapper(instrumentor),
            )

            # TODO
            # Stream operations
            # wrap_function_wrapper(
            #     "azure.ai.agents",
            #     "AgentsClient.create_run_stream",
            #     run_stream_wrapper(instrumentor),
            # )

            # Instrument agent operations
            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.create_agent",
            #     agent_create_wrapper(instrumentor),
            # )

            # # Instrument thread operations
            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.create_thread",
            #     thread_create_wrapper(instrumentor),
            # )

            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.create_message",
            #     message_create_wrapper(instrumentor),
            # )

            # # Instrument run operations - this is where the main AI interaction happens
            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.create_run",
            #     run_create_wrapper(instrumentor),
            # )

            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.submit_tool_outputs_to_run",
            #     tool_outputs_wrapper(instrumentor),
            # )

            # # Stream operations
            # wrap_function_wrapper(
            #     "azure.ai.projects",
            #     "AIProjectsClient.agents.create_run_stream",
            #     run_stream_wrapper(instrumentor),
            # )

            # Async versions
            # wrap_function_wrapper(
            #     "azure.ai.projects.aio",
            #     "AIProjectsClient.agents.create_run",
            #     arun_create_wrapper(instrumentor),
            # )

            # wrap_function_wrapper(
            #     "azure.ai.projects.aio",
            #     "AIProjectsClient.agents.create_run_stream",
            #     arun_stream_wrapper(instrumentor),
            # )

            # wrap_function_wrapper(
            #     "azure.ai.projects.aio",
            #     "AIProjectsClient.agents.submit_tool_outputs_to_run",
            #     atool_outputs_wrapper(instrumentor),
            # )

        except Exception as e:
            instrumentor._logger.debug(f"Error instrumenting azure-ai-projects: {e}")


@_PayiInstrumentor.payi_wrapper
def agent_create_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Agent create wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryAgentProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_wrapper
def thread_create_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Thread create wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryThreadProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_wrapper
def message_create_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Message create wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryMessageProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def thread_message_init_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Thread Message init wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryThreadMessageInitProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def run_init_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Run create wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor, class_constructor=True),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def run_create_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Run create wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )

@_PayiInstrumentor.payi_wrapper
def run_create_and_process_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Run create and process wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_wrapper
def run_stream_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Run stream wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor),
        _IsStreaming.true,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_wrapper
def tool_outputs_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("Azure AI Foundry Tool outputs wrapper")
    return instrumentor.invoke_wrapper(
        _AzureAiFoundryToolOutputsProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_awrapper
async def arun_create_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("async Azure AI Foundry Run create wrapper")
    return await instrumentor.async_invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_awrapper
async def arun_stream_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("async Azure AI Foundry Run stream wrapper")
    return await instrumentor.async_invoke_wrapper(
        _AzureAiFoundryRunProviderRequest(instrumentor),
        _IsStreaming.true,
        wrapped,
        instance,
        args,
        kwargs,
    )


@_PayiInstrumentor.payi_awrapper
async def atool_outputs_wrapper(
    instrumentor: _PayiInstrumentor,
    wrapped: Any,
    instance: Any,
    *args: Any,
    **kwargs: Any,
) -> Any:
    instrumentor._logger.debug("async Azure AI Foundry Tool outputs wrapper")
    return await instrumentor.async_invoke_wrapper(
        _AzureAiFoundryToolOutputsProviderRequest(instrumentor),
        _IsStreaming.false,
        wrapped,
        instance,
        args,
        kwargs,
    )


class _AzureAiFoundryProviderRequest(_ProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor, streaming_type: _StreamingType = _StreamingType.iterator):
        super().__init__(
            instrumentor=instrumentor,
            category=AZURE_AI_FOUNDRY_CATEGORY,
            streaming_type=streaming_type,
            module_name=AzureAiFoundryInstrumentor._module_name,
            module_version=AzureAiFoundryInstrumentor._module_version,
        )

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        # # Extract model information from kwargs if available
        # model = kwargs.get("model", "")
        # if not model and hasattr(instance, "_model"):
        #     model = getattr(instance, "_model", "")
        
        # self._ingest["resource"] = model or "azure.ai.foundry.agent"
        return True

    @override
    def process_synchronous_response(self, response: Any, log_prompt_and_response: bool, kwargs: Any) -> Any:
        super().process_synchronous_response(response, log_prompt_and_response, kwargs)
        response_dict = self._model_to_dict(response)
        
        if "id" in response_dict:
            self._ingest["provider_response_id"] = response_dict["id"]

        if log_prompt_and_response:
            self._ingest["provider_response_json"] = json.dumps(response_dict)

        return None

    @override
    def process_exception(self, exception: Exception, kwargs: Any) -> bool:
        try:
            # Handle Azure AI Foundry specific exceptions
            if hasattr(exception, "status_code"):
                status_code = getattr(exception, "status_code", None)
                if isinstance(status_code, int):
                    self._ingest["http_status_code"] = status_code

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
            self._instrumentor._logger.debug(f"Error processing Azure AI Foundry exception: {e}")
            return False

        return True

    def _model_to_dict(self, model: Any) -> Any:
        """Convert Azure AI models to dictionary for processing"""
        return model.as_dict()


class _AzureAiFoundryAgentProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        super().process_request(instance, extra_headers, args, kwargs)
        self._ingest["resource"] = AZURE_AI_FOUNDRY_RESOURCE
        self.add_internal_request_property("system.use_case_step", "agent.create()")
        self._ingest["units"][UNIT_AGENT_CREATE] = Units(input=1, output=0)
        return True
    
    @override
    def process_request_prompt(self, prompt: 'dict[str, Any]', args: Sequence[Any], kwargs: 'dict[str, Any]') -> None:
        if not self._instrumentor._log_prompt_and_response:
            return

        tools = kwargs.get("tools", [])
        tools_prompt: list[dict[str, Any]] = []
        for tool in tools:
            if isinstance(tool, dict):
                tools_prompt.append(tool)  # type: ignore
            elif hasattr(tool, "as_dict"):
                tools_prompt.append(tool.as_dict())

        if tools_prompt:
            prompt["tools"] = tools_prompt

        tool_resources = kwargs.get("tool_resources", [])
        tool_resources_prompt: list[dict[str, Any]] = []
        for tool_resource in tool_resources:
            if isinstance(tool_resource, dict):
                tool_resources_prompt.append(tool_resource)  # type: ignore
            elif hasattr(tool_resource, "as_dict"):
                tool_resources_prompt.append(tool_resource.as_dict())

        if tool_resources_prompt:
            prompt["tool_resources"] = tool_resources_prompt

        toolset = kwargs.get("toolset", None)
        if toolset:
            if isinstance(toolset, dict):
                prompt["toolset"] = toolset
            elif hasattr(toolset, "as_dict"):
                prompt["toolset"] = toolset.as_dict()

class _AzureAiFoundryThreadProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)

    @override
    def process_synchronous_response(self, response: Any, log_prompt_and_response: bool, kwargs: Any) -> Any:
        return super().process_synchronous_response(response, log_prompt_and_response, kwargs)


class _AzureAiFoundryMessageProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        super().process_request(instance, extra_headers, args, kwargs)
        self._ingest["resource"] = AZURE_AI_FOUNDRY_RESOURCE
        self.add_internal_request_property("system.use_case_step", "agent.message()")
    
        self._ingest["units"][UNIT_MESSAGE_CREATE] = Units(input=1, output=0)

        # # Capture message content
        # content = kwargs.get("content", "")
        # if content:
        #     # This is user input we want to track
        #     self._instrumentor._logger.debug(f"Azure AI Foundry message content captured: {len(content)} characters")
            
        return True

class _AzureAiFoundryThreadMessageInitProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)
        self._class_constructor = True

    @override
    def process_synchronous_response(self, response: Any, log_prompt_and_response: bool, kwargs: Any) -> Any:
        response_dict = response.as_dict()
        run_id = response_dict.get("run_id", None)
        if not run_id:
            # client is constructing a message, do not ingest as it is not a message created post run
            return None

        id = response_dict.get("id", "")
        if id:
            self._ingest["provider_response_id"] = id

        if log_prompt_and_response:
            self._ingest["provider_response_json"] = json.dumps(response_dict)

        self.add_internal_request_property("system.use_case_step", "agent.get_message()")

        self._ingest["resource"] = AZURE_AI_FOUNDRY_RESOURCE
        self._ingest["units"][UNIT_MESSAGE_RESPONSE] = Units(input=0, output=1)

        return True

class _AzureAiFoundryRunProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor, class_constructor: bool = False):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)
        self._run_completed = False
        self._class_constructor = class_constructor

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        super().process_request(instance, extra_headers, args, kwargs)
        
        # Capture thread_id as this is where the conversation happens
        thread_id = kwargs.get("thread_id", "")
        agent_id = kwargs.get("agent_id", "")
        
        if thread_id:
            self.add_internal_request_property("thread_id", thread_id)
            
        if agent_id:
            self.add_internal_request_property("agent_id", agent_id)

        context = self._instrumentor.get_context_safe()
        price_as_category = extra_headers.get(PayiHeaderNames.price_as_category) or context.get("price_as_category")
        price_as_resource = extra_headers.get(PayiHeaderNames.price_as_resource) or context.get("price_as_resource")
        resource_scope = extra_headers.get(PayiHeaderNames.resource_scope) or context.get("resource_scope")

        if PayiHeaderNames.price_as_category in extra_headers:
            del extra_headers[PayiHeaderNames.price_as_category]
        if PayiHeaderNames.price_as_resource in extra_headers:
            del extra_headers[PayiHeaderNames.price_as_resource]
        if PayiHeaderNames.resource_scope in extra_headers:
            del extra_headers[PayiHeaderNames.resource_scope]
            
        if not price_as_resource and not price_as_category:
            self._instrumentor._logger.error("Azure Foundry AI requires price as resource and/or category to be specified, not ingesting")
            return False

        if resource_scope:
            if not(resource_scope in ["global", "datazone"] or resource_scope.startswith("region")):
                self._instrumentor._logger.error("Azure Foundry AI invalid resource scope, not ingesting")
                return False

            self._ingest["resource_scope"] = resource_scope

        if price_as_category:
            # price as category overrides default
            self._ingest["category"] = price_as_category
        if price_as_resource:
            self._ingest["resource"] = price_as_resource

        return True

    @override
    def process_chunk(self, chunk: Any) -> _ChunkResult:
        """Process streaming chunks from Azure AI Foundry runs"""
        ingest = False
        chunk_dict = self._model_to_dict(chunk)
        
        # Look for run completion events
        event = chunk_dict.get("event", "")
        data = chunk_dict.get("data", {})
        
        if event == "thread.run.completed":
            self._run_completed = True
            ingest = True
            
            # Extract usage information
            usage = data.get("usage", {})
            if usage:
                self._add_usage_units(usage)
                
            # Extract run ID
            run_id = data.get("id", "")
            if run_id:
                self._ingest["provider_response_id"] = run_id
                
        elif event == "thread.message.delta":
            # Capture message deltas for streaming responses
            delta = data.get("delta", {})
            content = delta.get("content", [])
            
            for content_item in content:
                if content_item.get("type") == "text":
                    # This is part of the assistant's response
                    pass  # We'll capture the full response at the end
                    
        elif event == "thread.run.requires_action":
            # Tool calls required
            required_action = data.get("required_action", {})
            tool_calls = required_action.get("submit_tool_outputs", {}).get("tool_calls", [])
            
            for tool_call in tool_calls:
                function = tool_call.get("function", {})
                name = function.get("name", "")
                arguments = function.get("arguments", "")
                
                if name:
                    self.add_synchronous_function_call(name=name, arguments=arguments)
        
        return _ChunkResult(send_chunk_to_caller=True, ingest=ingest)

    @override
    def process_synchronous_response(self, response: Any, log_prompt_and_response: bool, kwargs: Any) -> Any:
        response_dict = self._model_to_dict(response)

        status = response_dict.get("status", "").lower()

        if status == "requires_action":
            run_id = response_dict.get("id", "")
            if run_id:
                self._ingest["provider_response_id"] = run_id

            required_action = response_dict.get("required_action", {})
            tool_calls = required_action.get("submit_tool_outputs", {}).get("tool_calls", [])
            functionCallsAdded = 0
            for tool_call in tool_calls:
                toolType = tool_call.get("type", "")
                if toolType != "function":
                    continue

                function = tool_call.get("function", {})
                name = function.get("name", "")
                arguments = function.get("arguments", "")
                
                if name:
                    self.add_synchronous_function_call(name=name, arguments=arguments)
                    functionCallsAdded += 1

            if functionCallsAdded:
                if log_prompt_and_response:
                    self._ingest["provider_response_json"] = json.dumps(response_dict)

                self.add_internal_request_property("system.use_case_step", "agent.tool_call()")

                # Override the default configuration of the run telemetry to report on the completed response which incurs LLM cost
                self._ingest["category"] = AZURE_AI_FOUNDRY_CATEGORY
                self._ingest["resource"] = AZURE_AI_FOUNDRY_RESOURCE
                self._ingest["units"][UNIT_TOOL_CALL] = Units(input=0, output=functionCallsAdded)
                return True
            else:
                return None  # Do not ingest with no function calls

        if status != "completed":
            # by returning None we do not ingest this response
            return None

        started_at = response_dict.get("started_at", 0)
        completed_at = response_dict.get("completed_at", 0)

        # Since we are wrapping the constructor, the timestamp that the generic instrumentor computes will be zero so use the
        # reported timestamps from the agent service. Both values are expressed in seconds
        if started_at > 0 and completed_at > 0 and completed_at >= started_at:
            duration = (completed_at - started_at) * 1000  # Convert seconds to milliseconds
            self._ingest["end_to_end_latency_ms"] = duration

        thread_id = response_dict.get("thread_id", "")
        assistant_id = response_dict.get("assistant_id", "")

        self.add_internal_request_property("system.use_case_step", "agent.run()")

        if thread_id:
            self.add_internal_request_property("thread_id", thread_id)
            
        if assistant_id:
            self.add_internal_request_property("assistant_id", assistant_id)

        run_id = response_dict.get("id", "")
        if run_id:
            self._ingest["provider_response_id"] = run_id
            
        usage = response_dict.get("usage", {})
        if usage:
            self._add_usage_units(usage)
            
        if log_prompt_and_response:
            self._ingest["provider_response_json"] = json.dumps(response_dict)

        return True

    def _add_usage_units(self, usage: 'dict[str, Any]') -> None:
        units = self._ingest["units"]
        
        # Azure AI Foundry typically provides prompt_tokens, completion_tokens, total_tokens
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        
        # Some responses might use different field names
        if not prompt_tokens:
            prompt_tokens = usage.get("input_tokens", 0)
        if not completion_tokens:
            completion_tokens = usage.get("output_tokens", 0)

        units["text"] = Units(input=prompt_tokens, output=completion_tokens)

        completion_tokens = usage.get("prompt_token_details", {}).get("cached_tokens", 0)
        if completion_tokens > 0:
            units["text_cache_read"] = Units(input=completion_tokens, output=0)
        
        self._instrumentor._logger.debug(f"Azure AI Foundry usage captured: {prompt_tokens} input, {completion_tokens} output")


class _AzureAiFoundryToolOutputsProviderRequest(_AzureAiFoundryProviderRequest):
    def __init__(self, instrumentor: _PayiInstrumentor):
        super().__init__(instrumentor=instrumentor, streaming_type=_StreamingType.iterator)

    @override
    def process_request(self, instance: Any, extra_headers: 'dict[str, str]', args: Sequence[Any], kwargs: Any) -> bool:
        super().process_request(instance, extra_headers, args, kwargs)
        self._ingest["resource"] = AZURE_AI_FOUNDRY_RESOURCE        
        self.add_internal_request_property("system.use_case_step", "agent.tool_outputs()")
        
        # if self._instrumentor._log_prompt_and_response:
        # Capture tool outputs being submitted
        tool_outputs = kwargs.get("tool_outputs", [])
        
        if tool_outputs:
            self._ingest["units"][UNIT_TOOL_CALL_OUTPUT] = Units(input=len(tool_outputs), output=0)
            self.add_internal_request_property("tool_outputs_count", str(len(tool_outputs)))

        tool_approvals = kwargs.get("tool_approvals", [])
        if tool_approvals:
            self.add_internal_request_property("tool_approvals_count", str(len(tool_approvals)))
        return True
    
    @override
    def process_request_prompt(self, prompt: 'dict[str, Any]', args: Sequence[Any], kwargs: 'dict[str, Any]') -> None:
        super().process_request_prompt(prompt, args, kwargs)
        if not self._instrumentor._log_prompt_and_response:
            return

        tool_outputs = kwargs.get("tool_outputs", [])
        tool_outputs_list: list[dict[str, Any]] = []
        for output in tool_outputs:
            if isinstance(output, dict):
                tool_outputs_list.append(output)  # type: ignore
            elif hasattr(output, "as_dict"):
                tool_outputs_list.append(output.as_dict())

        if tool_outputs_list:
            prompt["tool_outputs"] = tool_outputs_list

        tool_approvals = kwargs.get("tool_approvals", [])
        tool_approvals_list: list[dict[str, Any]] = []
        for approval in tool_approvals:
            if isinstance(approval, dict):
                tool_approvals_list.append(approval)  # type: ignore
            elif hasattr(approval, "as_dict"):
                tool_approvals_list.append(approval.as_dict())

        if tool_approvals_list:
            prompt["tool_approvals"] = tool_approvals_list
