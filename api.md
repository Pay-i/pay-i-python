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

- <code title="post /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">create</a>(\*\*<a href="src/payi/types/experiences/type_create_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">retrieve</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="patch /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">update</a>(experience_name, \*\*<a href="src/payi/types/experiences/type_update_params.py">params</a>) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>
- <code title="get /api/v1/experiences/types">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">list</a>(\*\*<a href="src/payi/types/experiences/type_list_params.py">params</a>) -> <a href="./src/payi/types/experiences/type_list_response.py">TypeListResponse</a></code>
- <code title="delete /api/v1/experiences/types/{experience_name}">client.experiences.types.<a href="./src/payi/resources/experiences/types.py">delete</a>(experience_name) -> <a href="./src/payi/types/experiences/experience_type.py">ExperienceType</a></code>

## Properties

Types:

```python
from payi.types.experiences import PropertiesResponse
```

Methods:

- <code title="post /api/v1/experiences/instances/{experience_id}/properties">client.experiences.properties.<a href="./src/payi/resources/experiences/properties.py">create</a>(experience_id, \*\*<a href="src/payi/types/experiences/property_create_params.py">params</a>) -> <a href="./src/payi/types/experience_instance_response.py">ExperienceInstanceResponse</a></code>

# BillingModels

Types:

```python
from payi.types import BillingModel, BillingModelListResponse
```

Methods:

- <code title="post /api/v1/billing-model">client.billing_models.<a href="./src/payi/resources/billing_models.py">create</a>(\*\*<a href="src/payi/types/billing_model_create_params.py">params</a>) -> <a href="./src/payi/types/billing_model.py">BillingModel</a></code>
- <code title="get /api/v1/billing-model/{billing_model_id}">client.billing_models.<a href="./src/payi/resources/billing_models.py">retrieve</a>(billing_model_id) -> <a href="./src/payi/types/billing_model.py">BillingModel</a></code>
- <code title="put /api/v1/billing-model/{billing_model_id}">client.billing_models.<a href="./src/payi/resources/billing_models.py">update</a>(billing_model_id, \*\*<a href="src/payi/types/billing_model_update_params.py">params</a>) -> <a href="./src/payi/types/billing_model.py">BillingModel</a></code>
- <code title="get /api/v1/billing-model">client.billing_models.<a href="./src/payi/resources/billing_models.py">list</a>() -> <a href="./src/payi/types/billing_model_list_response.py">BillingModelListResponse</a></code>
- <code title="put /api/v1/billing-model/{billing_model_id}/default">client.billing_models.<a href="./src/payi/resources/billing_models.py">set_default</a>(billing_model_id) -> <a href="./src/payi/types/billing_model.py">BillingModel</a></code>

# PriceModifiers

Types:

```python
from payi.types import PriceModifier, PriceModifierRetrieveResponse
```

Methods:

- <code title="post /api/v1/price-modifier">client.price_modifiers.<a href="./src/payi/resources/price_modifiers.py">create</a>(\*\*<a href="src/payi/types/price_modifier_create_params.py">params</a>) -> <a href="./src/payi/types/price_modifier.py">PriceModifier</a></code>
- <code title="get /api/v1/price-modifier/{billing_model_id}">client.price_modifiers.<a href="./src/payi/resources/price_modifiers.py">retrieve</a>(billing_model_id) -> <a href="./src/payi/types/price_modifier_retrieve_response.py">PriceModifierRetrieveResponse</a></code>
- <code title="put /api/v1/price-modifier">client.price_modifiers.<a href="./src/payi/resources/price_modifiers.py">update</a>(\*\*<a href="src/payi/types/price_modifier_update_params.py">params</a>) -> <a href="./src/payi/types/price_modifier.py">PriceModifier</a></code>

# Requests

## Properties

Methods:

- <code title="post /api/v1/requests/{request_id}/properties">client.requests.properties.<a href="./src/payi/resources/requests/properties.py">create</a>(request_id, \*\*<a href="src/payi/types/requests/property_create_params.py">params</a>) -> <a href="./src/payi/types/experiences/properties_response.py">PropertiesResponse</a></code>