from typing import Dict, List, Union

PAYI_BASE_URL = "https://api.pay-i.com"

class PayiHeaderNames:
    limit_ids:str  = "xProxy-Limit-IDs"
    request_tags:str = "xProxy-Request-Tags"
    experience_id:str = "xProxy-Experience-ID"
    experience_name:str = "xProxy-Experience-Name"
    use_case_id:str = "xProxy-UseCase-ID"
    use_case_name:str = "xProxy-UseCase-Name"
    use_case_version:str = "xProxy-UseCase-Version"
    user_id:str = "xProxy-User-ID"
    route_as_resource:str = "xProxy-RouteAs-Resource"
    provider_base_uri = "xProxy-Provider-BaseUri"
    resource_scope:str = "xProxy-Resource-Scope"

class PayiCategories:
    anthropic:str  = "system.anthropic"
    openai:str = "system.openai"
    azure_openai:str = "system.azureopenai"
    aws_bedrock:str = "system.aws.bedrock"

def create_limit_header_from_ids(limit_ids: List[str]) -> Dict[str, str]:
    if not isinstance(limit_ids, list):  # type: ignore
        raise TypeError("limit_ids must be a list")

    valid_ids = [id.strip() for id in limit_ids if isinstance(id, str) and id.strip()]  # type: ignore

    return { PayiHeaderNames.limit_ids: ",".join(valid_ids) } if valid_ids else {}


def create_request_header_from_tags(request_tags: List[str]) -> Dict[str, str]:
    if not isinstance(request_tags, list):  # type: ignore
        raise TypeError("request_tags must be a list")

    valid_tags = [tag.strip() for tag in request_tags if isinstance(tag, str) and tag.strip()]  # type: ignore

    return { PayiHeaderNames.request_tags: ",".join(valid_tags) } if valid_tags else {}


def create_headers(
    limit_ids: Union[List[str], None] = None,
    request_tags: Union[List[str], None] = None,
    user_id: Union[str, None] = None,
    experience_id: Union[str, None] = None,
    experience_name: Union[str, None] = None,
    use_case_id: Union[str, None] = None,
    use_case_name: Union[str, None] = None,
    use_case_version: Union[int, None] = None,
) -> Dict[str, str]:
    headers: Dict[str, str] = {}

    if limit_ids:
        headers.update(create_limit_header_from_ids(limit_ids))
    if request_tags:
        headers.update(create_request_header_from_tags(request_tags))
    if user_id:
        headers.update({ PayiHeaderNames.user_id: user_id})
    if experience_id:
        headers.update({ PayiHeaderNames.experience_id: experience_id})
    if experience_name:
        headers.update({ PayiHeaderNames.experience_name: experience_name})
    if use_case_id:
        headers.update({ PayiHeaderNames.use_case_id: use_case_id})
    if use_case_name:
        headers.update({ PayiHeaderNames.use_case_name: use_case_name})
    if use_case_version:
        headers.update({ PayiHeaderNames.use_case_version: str(use_case_version)})
    return headers

def payi_anthropic_url(payi_base_url: Union[str, None] = None) -> str:
    if payi_base_url is None:
        payi_base_url = PAYI_BASE_URL
    return payi_base_url + "/api/v1/proxy/anthropic"

def payi_openai_url(payi_base_url: Union[str, None] = None) -> str:
    if payi_base_url is None:
        payi_base_url = PAYI_BASE_URL
    return payi_base_url +  "/api/v1/proxy/openai/v1"

def payi_azure_openai_url(payi_base_url: Union[str, None] = None) -> str:
    if payi_base_url is None:
        payi_base_url = PAYI_BASE_URL
    return payi_base_url + "/api/v1/proxy/azure.openai"

def payi_aws_bedrock_url(payi_base_url: Union[str, None] = None) -> str:
    if payi_base_url is None:
        payi_base_url = PAYI_BASE_URL
    return payi_base_url + "/api/v1/proxy/aws.bedrock"
