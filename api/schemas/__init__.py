"""
API schemas for request and response models.
"""

from api.schemas.requests import ClassifyRequest, CompareRequest
from api.schemas.responses import (
    ClassifyResponse,
    CompareResponse,
    ErrorResponse,
    HealthResponse,
)

__all__ = [
    "ClassifyRequest",
    "CompareRequest",
    "ClassifyResponse",
    "CompareResponse",
    "ErrorResponse",
    "HealthResponse",
]
