# Shared Types

```python
from payi.types import EvaluationResponse
```

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
    TotalCostData,
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
from payi.types import BulkIngestResponse, IngestEvent, IngestResponse, IngestUnits
```

Methods:

- <code title="post /api/v1/ingest/bulk">client.ingest.<a href="./src/payi/resources/ingest.py">bulk</a>(\*\*<a href="src/payi/types/ingest_bulk_params.py">params</a>) -> <a href="./src/payi/types/bulk_ingest_response.py">BulkIngestResponse</a></code>
- <code title="post /api/v1/ingest">client.ingest.<a href="./src/payi/resources/ingest.py">units</a>(\*\*<a href="src/payi/types/ingest_units_params.py">params</a>) -> <a href="./src/payi/types/ingest_response.py">IngestResponse</a></code>

# Categories

Types:

```python
from payi.types import (
    CategoryResourceResponse,
    CategoryResponse,
    CategoryListResponse,
    CategoryDeleteResponse,
    CategoryDeleteResourceResponse,
    CategoryListResourcesResponse,
)
```

Methods:

- <code title="get /api/v1/categories">client.categories.<a href="./src/payi/resources/categories/categories.py">list</a>() -> <a href="./src/payi/types/category_list_response.py">CategoryListResponse</a></code>
- <code title="delete /api/v1/categories/{category}">client.categories.<a href="./src/payi/resources/categories/categories.py">delete</a>(category) -> <a href="./src/payi/types/category_delete_response.py">CategoryDeleteResponse</a></code>
- <code title="delete /api/v1/categories/{category}/resources/{resource}">client.categories.<a href="./src/payi/resources/categories/categories.py">delete_resource</a>(resource, \*, category) -> <a href="./src/payi/types/category_delete_resource_response.py">CategoryDeleteResourceResponse</a></code>
- <code title="get /api/v1/categories/{category}/resources">client.categories.<a href="./src/payi/resources/categories/categories.py">list_resources</a>(category) -> <a href="./src/payi/types/category_list_resources_response.py">CategoryListResourcesResponse</a></code>

## Resources

Types:

```python
from payi.types.categories import ResourceListResponse
```

Methods:

- <code title="post /api/v1/categories/{category}/resources/{resource}">client.categories.resources.<a href="./src/payi/resources/categories/resources.py">create</a>(resource, \*, category, \*\*<a href="src/payi/types/categories/resource_create_params.py">params</a>) -> <a href="./src/payi/types/category_resource_response.py">CategoryResourceResponse</a></code>
- <code title="get /api/v1/categories/{category}/resources/{resource}/{resource_id}">client.categories.resources.<a href="./src/payi/resources/categories/resources.py">retrieve</a>(resource_id, \*, category, resource) -> <a href="./src/payi/types/category_resource_response.py">CategoryResourceResponse</a></code>
- <code title="get /api/v1/categories/{category}/resources/{resource}">client.categories.resources.<a href="./src/payi/resources/categories/resources.py">list</a>(resource, \*, category) -> <a href="./src/payi/types/categories/resource_list_response.py">ResourceListResponse</a></code>
- <code title="delete /api/v1/categories/{category}/resources/{resource}/{resource_id}">client.categories.resources.<a href="./src/payi/resources/categories/resources.py">delete</a>(resource_id, \*, category, resource) -> <a href="./src/payi/types/category_resource_response.py">CategoryResourceResponse</a></code>

# Experiences

Types:

```python
from payi.types import ExperienceInstance
```

Methods:

- <code title="post /api/v1/experiences/instances/{experience_name}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">create</a>(experience_name) -> <a href="./src/payi/types/experience_instance.py">ExperienceInstance</a></code>
- <code title="get /api/v1/experiences/instances/{experience_id}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">retrieve</a>(experience_id) -> <a href="./src/payi/types/experience_instance.py">ExperienceInstance</a></code>
- <code title="delete /api/v1/experiences/instances/{experience_id}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">delete</a>(experience_id) -> <a href="./src/payi/types/experience_instance.py">ExperienceInstance</a></code>

## Types

Types:

```python
from payi.types.experiences import ExperienceType, TypeListResponse
```

Methods:

- <code title="post /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">create</a>(\*\*<a href="src/payi/types/experiences/type_create_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">retrieve</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="patch /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">update</a>(experience_name, \*\*<a href="src/payi/types/experiences/type_update_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">list</a>(\*\*<a href="src/payi/types/experiences/type_list_params.py">params</a>) -> <a href="./src/payi/types/experiences/type_list_response.py">TypeListResponse</a></code>
- <code title="delete /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">delete</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>

# Evaluations

## Experiences

Methods:

- <code title="post /api/v1/evaluations/experiences/{experience_id}">client.evaluations.experiences.<a href="./src/payi/resources/evaluations/experiences.py">create</a>(experience_id, \*\*<a href="src/payi/types/evaluations/experience_create_params.py">params</a>) -> <a href="./src/payi/types/shared/evaluation_response.py">EvaluationResponse</a></code>

## Requests

Methods:

- <code title="post /api/v1/evaluations/requests/{request_id}">client.evaluations.requests.<a href="./src/payi/resources/evaluations/requests.py">create</a>(request_id, \*\*<a href="src/payi/types/evaluations/request_create_params.py">params</a>) -> <a href="./src/payi/types/shared/evaluation_response.py">EvaluationResponse</a></code>
