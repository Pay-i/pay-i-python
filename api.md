# Budgets

Types:

```python
from payi.types import (
    BudgetHistoryResponse,
    BudgetResponse,
    CostData,
    CostDetails,
    DefaultResponse,
    PagedBudgetList,
    RequestsData,
)
```

Methods:

- <code title="post /api/v1/budgets">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">create</a>(\*\*<a href="src/payi/types/budget_create_params.py">params</a>) -> <a href="./src/payi/types/budget_response.py">BudgetResponse</a></code>
- <code title="get /api/v1/budgets/{budget_id}">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">retrieve</a>(budget_id) -> <a href="./src/payi/types/budget_response.py">BudgetResponse</a></code>
- <code title="put /api/v1/budgets/{budget_id}">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">update</a>(budget_id, \*\*<a href="src/payi/types/budget_update_params.py">params</a>) -> <a href="./src/payi/types/budget_response.py">BudgetResponse</a></code>
- <code title="get /api/v1/budgets">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">list</a>(\*\*<a href="src/payi/types/budget_list_params.py">params</a>) -> <a href="./src/payi/types/paged_budget_list.py">PagedBudgetList</a></code>
- <code title="delete /api/v1/budgets/{budget_id}">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">delete</a>(budget_id) -> <a href="./src/payi/types/default_response.py">DefaultResponse</a></code>
- <code title="post /api/v1/budgets/{budget_id}/reset">client.budgets.<a href="./src/payi/resources/budgets/budgets.py">reset</a>(budget_id) -> <a href="./src/payi/types/budget_history_response.py">BudgetHistoryResponse</a></code>

## Tags

Types:

```python
from payi.types.budgets import (
    BudgetTags,
    TagCreateResponse,
    TagUpdateResponse,
    TagListResponse,
    TagDeleteResponse,
    TagRemoveResponse,
)
```

Methods:

- <code title="post /api/v1/budgets/{budget_id}/tags">client.budgets.tags.<a href="./src/payi/resources/budgets/tags.py">create</a>(budget_id, \*\*<a href="src/payi/types/budgets/tag_create_params.py">params</a>) -> <a href="./src/payi/types/budgets/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /api/v1/budgets/{budget_id}/tags">client.budgets.tags.<a href="./src/payi/resources/budgets/tags.py">update</a>(budget_id, \*\*<a href="src/payi/types/budgets/tag_update_params.py">params</a>) -> <a href="./src/payi/types/budgets/tag_update_response.py">TagUpdateResponse</a></code>
- <code title="get /api/v1/budgets/{budget_id}/tags">client.budgets.tags.<a href="./src/payi/resources/budgets/tags.py">list</a>(budget_id) -> <a href="./src/payi/types/budgets/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /api/v1/budgets/{budget_id}/tags">client.budgets.tags.<a href="./src/payi/resources/budgets/tags.py">delete</a>(budget_id) -> <a href="./src/payi/types/budgets/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="patch /api/v1/budgets/{budget_id}/tags/remove">client.budgets.tags.<a href="./src/payi/resources/budgets/tags.py">remove</a>(budget_id, \*\*<a href="src/payi/types/budgets/tag_remove_params.py">params</a>) -> <a href="./src/payi/types/budgets/tag_remove_response.py">TagRemoveResponse</a></code>

# Ingest

Types:

```python
from payi.types import ProxyResult
```

Methods:

- <code title="post /api/v1/ingest">client.ingest.<a href="./src/payi/resources/ingest.py">units</a>(\*\*<a href="src/payi/types/ingest_units_params.py">params</a>) -> <a href="./src/payi/types/proxy_result.py">ProxyResult</a></code>
