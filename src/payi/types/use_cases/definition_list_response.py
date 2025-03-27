# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .use_case_definition import UseCaseDefinition

__all__ = ["DefinitionListResponse"]

DefinitionListResponse: TypeAlias = List[UseCaseDefinition]
