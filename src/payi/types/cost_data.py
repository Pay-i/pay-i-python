# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel
from .cost_details import CostDetails

__all__ = ["CostData"]


class CostData(BaseModel):
    input: CostDetails

    output: CostDetails

    total: CostDetails
