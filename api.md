# Shared Types

```python
from payi.types import (
    PayICommonModelsBudgetManagementCostDetailsBase,
    PayICommonModelsBudgetManagementCreateLimitBase,
    PropertiesResponse,
)
```

# Limits

Types:

```python
from payi.types import (
    CostData,
    CostDetails,
    DefaultResponse,
    LimitHistoryResponse,
    LimitResponse,
    PagedLimitList,
    RequestsData,
    TotalCostData,
)
```

Methods:

- <code title="post /api/v1/limits">client.limits.<a href="./src/payi/resources/limits/limits.py">create</a>(\*\*<a href="src/payi/types/limit_create_params.py">params</a>) -> <a href="./src/payi/types/limit_response.py">LimitResponse</a></code>
- <code title="get /api/v1/limits/{limit_id}">client.limits.<a href="./src/payi/resources/limits/limits.py">retrieve</a>(limit_id) -> <a href="./src/payi/types/limit_response.py">LimitResponse</a></code>
- <code title="put /api/v1/limits/{limit_id}">client.limits.<a href="./src/payi/resources/limits/limits.py">update</a>(limit_id, \*\*<a href="src/payi/types/limit_update_params.py">params</a>) -> <a href="./src/payi/types/limit_response.py">LimitResponse</a></code>
- <code title="get /api/v1/limits">client.limits.<a href="./src/payi/resources/limits/limits.py">list</a>(\*\*<a href="src/payi/types/limit_list_params.py">params</a>) -> <a href="./src/payi/types/paged_limit_list.py">PagedLimitList</a></code>
- <code title="delete /api/v1/limits/{limit_id}">client.limits.<a href="./src/payi/resources/limits/limits.py">delete</a>(limit_id) -> <a href="./src/payi/types/default_response.py">DefaultResponse</a></code>
- <code title="post /api/v1/limits/{limit_id}/reset">client.limits.<a href="./src/payi/resources/limits/limits.py">reset</a>(limit_id, \*\*<a href="src/payi/types/limit_reset_params.py">params</a>) -> <a href="./src/payi/types/limit_history_response.py">LimitHistoryResponse</a></code>

## Tags

Types:

```python
from payi.types.limits import (
    LimitTags,
    TagCreateResponse,
    TagUpdateResponse,
    TagListResponse,
    TagDeleteResponse,
    TagRemoveResponse,
)
```

Methods:

- <code title="post /api/v1/limits/{limit_id}/tags">client.limits.tags.<a href="./src/payi/resources/limits/tags.py">create</a>(limit_id, \*\*<a href="src/payi/types/limits/tag_create_params.py">params</a>) -> <a href="./src/payi/types/limits/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /api/v1/limits/{limit_id}/tags">client.limits.tags.<a href="./src/payi/resources/limits/tags.py">update</a>(limit_id, \*\*<a href="src/payi/types/limits/tag_update_params.py">params</a>) -> <a href="./src/payi/types/limits/tag_update_response.py">TagUpdateResponse</a></code>
- <code title="get /api/v1/limits/{limit_id}/tags">client.limits.tags.<a href="./src/payi/resources/limits/tags.py">list</a>(limit_id) -> <a href="./src/payi/types/limits/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /api/v1/limits/{limit_id}/tags">client.limits.tags.<a href="./src/payi/resources/limits/tags.py">delete</a>(limit_id) -> <a href="./src/payi/types/limits/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="patch /api/v1/limits/{limit_id}/tags/remove">client.limits.tags.<a href="./src/payi/resources/limits/tags.py">remove</a>(limit_id, \*\*<a href="src/payi/types/limits/tag_remove_params.py">params</a>) -> <a href="./src/payi/types/limits/tag_remove_response.py">TagRemoveResponse</a></code>

# Ingest

Types:

```python
from payi.types import (
    BulkIngestResponse,
    IngestEvent,
    IngestResponse,
    IngestUnits,
    PayICommonModelsAPIRouterHeaderInfo,
)
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
from payi.types import ExperienceInstanceResponse
```

Methods:

- <code title="post /api/v1/experiences/instances/{experience_name}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">create</a>(experience_name) -> <a href="./src/payi/types/experience_instance_response.py">ExperienceInstanceResponse</a></code>
- <code title="get /api/v1/experiences/instances/{experience_id}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">retrieve</a>(experience_id) -> <a href="./src/payi/types/experience_instance_response.py">ExperienceInstanceResponse</a></code>
- <code title="delete /api/v1/experiences/instances/{experience_id}">client.experiences.<a href="./src/payi/resources/experiences/experiences.py">delete</a>(experience_id) -> <a href="./src/payi/types/experience_instance_response.py">ExperienceInstanceResponse</a></code>

## Types

Types:

```python
from payi.types.experiences import ExperienceType, TypeListResponse
```

Methods:

- <code title="post /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types/types.py">create</a>(\*\*<a href="src/payi/types/experiences/type_create_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types/types.py">retrieve</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="patch /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types/types.py">update</a>(experience_name, \*\*<a href="src/payi/types/experiences/type_update_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types/types.py">list</a>(\*\*<a href="src/payi/types/experiences/type_list_params.py">params</a>) -> <a href="./src/payi/types/experiences/type_list_response.py">TypeListResponse</a></code>
- <code title="delete /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types/types.py">delete</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>

### LimitConfig

Methods:

- <code title="post /api/v1/experiences/types/{experience_name}/limit_config">client.experiences.types.limit_config.<a href="./src/payi/resources/experiences/types/limit_config.py">create</a>(experience_name, \*\*<a href="src/payi/types/experiences/types/limit_config_create_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="delete /api/v1/experiences/types/{experience_name}/limit_config">client.experiences.types.limit_config.<a href="./src/payi/resources/experiences/types/limit_config.py">delete</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>

## Properties

Methods:

- <code title="post /api/v1/experiences/instances/{experience_id}/properties">client.experiences.properties.<a href="./src/payi/resources/experiences/properties.py">create</a>(experience_id, \*\*<a href="src/payi/types/experiences/property_create_params.py">params</a>) -> <a href="./src/payi/types/experience_instance_response.py">ExperienceInstanceResponse</a></code>

# UseCases

Types:

```python
from payi.types import UseCaseInstanceResponse
```

Methods:

- <code title="post /api/v1/use_cases/instances/{use_case_name}">client.use_cases.<a href="./src/payi/resources/use_cases/use_cases.py">create</a>(use_case_name) -> <a href="./src/payi/types/use_case_instance_response.py">UseCaseInstanceResponse</a></code>
- <code title="get /api/v1/use_cases/instances/{use_case_id}">client.use_cases.<a href="./src/payi/resources/use_cases/use_cases.py">retrieve</a>(use_case_id) -> <a href="./src/payi/types/use_case_instance_response.py">UseCaseInstanceResponse</a></code>
- <code title="delete /api/v1/use_cases/instances/{use_case_id}">client.use_cases.<a href="./src/payi/resources/use_cases/use_cases.py">delete</a>(use_case_id) -> <a href="./src/payi/types/use_case_instance_response.py">UseCaseInstanceResponse</a></code>

## Definitions

Types:

```python
from payi.types.use_cases import UseCaseDefinition, DefinitionListResponse
```

Methods:

- <code title="post /api/v1/use_cases/definitions">client.use_cases.definitions.<a href="./src/payi/resources/use_cases/definitions/definitions.py">create</a>(\*\*<a href="src/payi/types/use_cases/definition_create_params.py">params</a>) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>
- <code title="get /api/v1/use_cases/definitions/{use_case_name}">client.use_cases.definitions.<a href="./src/payi/resources/use_cases/definitions/definitions.py">retrieve</a>(use_case_name) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>
- <code title="patch /api/v1/use_cases/definitions/{use_case_name}">client.use_cases.definitions.<a href="./src/payi/resources/use_cases/definitions/definitions.py">update</a>(use_case_name, \*\*<a href="src/payi/types/use_cases/definition_update_params.py">params</a>) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>
- <code title="get /api/v1/use_cases/definitions">client.use_cases.definitions.<a href="./src/payi/resources/use_cases/definitions/definitions.py">list</a>(\*\*<a href="src/payi/types/use_cases/definition_list_params.py">params</a>) -> <a href="./src/payi/types/use_cases/definition_list_response.py">DefinitionListResponse</a></code>
- <code title="delete /api/v1/use_cases/definitions/{use_case_name}">client.use_cases.definitions.<a href="./src/payi/resources/use_cases/definitions/definitions.py">delete</a>(use_case_name) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>

### LimitConfig

Methods:

- <code title="post /api/v1/use_cases/definitions/{use_case_name}/limit_config">client.use_cases.definitions.limit_config.<a href="./src/payi/resources/use_cases/definitions/limit_config.py">create</a>(use_case_name, \*\*<a href="src/payi/types/use_cases/definitions/limit_config_create_params.py">params</a>) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>
- <code title="delete /api/v1/use_cases/definitions/{use_case_name}/limit_config">client.use_cases.definitions.limit_config.<a href="./src/payi/resources/use_cases/definitions/limit_config.py">delete</a>(use_case_name) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>

### Version

Methods:

- <code title="post /api/v1/use_cases/definitions/{use_case_name}/increment_version">client.use_cases.definitions.version.<a href="./src/payi/resources/use_cases/definitions/version.py">increment</a>(use_case_name) -> <a href="./src/payi/types/use_cases/use_case_definition.py">UseCaseDefinition</a></code>

## Properties

Methods:

- <code title="post /api/v1/use_cases/instances/{use_case_id}/properties">client.use_cases.properties.<a href="./src/payi/resources/use_cases/properties.py">create</a>(use_case_id, \*\*<a href="src/payi/types/use_cases/property_create_params.py">params</a>) -> <a href="./src/payi/types/use_case_instance_response.py">UseCaseInstanceResponse</a></code>

# Requests

## Properties

Methods:

- <code title="post /api/v1/requests/{request_id}/properties">client.requests.properties.<a href="./src/payi/resources/requests/properties.py">create</a>(request_id, \*\*<a href="src/payi/types/requests/property_create_params.py">params</a>) -> <a href="./src/payi/types/shared/properties_response.py">PropertiesResponse</a></code>

## Result

Types:

```python
from payi.types.requests import RequestResult
```

Methods:

- <code title="get /api/v1/requests/result/{category}/{request_id}">client.requests.result.<a href="./src/payi/resources/requests/result.py">retrieve</a>(request_id, \*, category) -> <a href="./src/payi/types/requests/request_result.py">RequestResult</a></code>
