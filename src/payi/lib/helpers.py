# Step 1: Define the new methods outside of the Payi class definition
from typing import Dict, List, Union


def create_budget_header_from_ids(budget_ids: List[str]) -> Dict[str, str]:
    if not isinstance(budget_ids, list): # type: ignore
        raise TypeError("budget_ids must be a list")

    valid_ids = [id.strip() for id in budget_ids if isinstance(id, str) and id.strip()] # type: ignore

    return {"xProxy-Budget-IDs": ",".join(valid_ids)} if valid_ids else {}

def create_request_header_from_tags(request_tags: List[str]) -> Dict[str, str]:
    if not isinstance(request_tags, list): # type: ignore
        raise TypeError("request_tags must be a list")

    valid_tags = [tag.strip() for tag in request_tags if isinstance(tag, str) and tag.strip()] # type: ignore
    
    return {"xProxy-Request-Tags": ",".join(valid_tags)} if valid_tags else {}

def create_headers(
    budget_ids: Union[List[str], None] = None, 
    request_tags: Union[List[str], None] = None 
    ) -> Dict[str, str]:
    headers: Dict[str, str] = {}

    if budget_ids:
        headers.update(create_budget_header_from_ids(budget_ids))
    if request_tags:
        headers.update(create_request_header_from_tags(request_tags))

    return headers