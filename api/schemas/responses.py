"""
Response models for the poker hands API.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response."""

    status: str = Field(..., description="Service status", examples=["healthy"])
    version: str = Field(..., description="API version", examples=["3.0.0"])


class ClassifyResponse(BaseModel):
    """
    Response model for hand classification.

    Attributes:
        hand_type: The classification result (e.g., "Royal Flush")
        strength: Numeric strength value (1-10, higher is better)
        cards: The cards that were classified
    """

    hand_type: str = Field(
        ..., description="Classification result", examples=["Royal Flush"]
    )
    strength: int = Field(
        ...,
        ge=1,
        le=10,
        description="Hand strength (1=High Card, 10=Royal Flush)",
        examples=[10],
    )
    cards: List[str] = Field(
        ..., description="Cards in the hand", examples=[["A♥", "K♥", "Q♥", "J♥", "T♥"]]
    )


class CompareResponse(BaseModel):
    """
    Response model for comparing two hands.

    Attributes:
        winner: Which hand won ("hand1", "hand2", or "tie")
        hand1: Classification of first hand
        hand2: Classification of second hand
    """

    winner: str = Field(
        ..., description="Winner of comparison", examples=["hand1", "hand2", "tie"]
    )
    hand1: ClassifyResponse = Field(..., description="First hand classification")
    hand2: ClassifyResponse = Field(..., description="Second hand classification")


class ErrorResponse(BaseModel):
    """
    Error response model.

    Attributes:
        detail: Error message
        error_type: Type of error (optional)
    """

    detail: str = Field(..., description="Error message")
    error_type: Optional[str] = Field(None, description="Type of error")
