"""
Request models for the poker hands API.
"""

from typing import List, Tuple

from pydantic import BaseModel, Field, field_validator

from core.validators import is_valid_card_tuple, has_duplicates


class ClassifyRequest(BaseModel):
    """
    Request model for classifying a single poker hand.

    Attributes:
        cards: List of 5 card tuples in format [("rank", "suit"), ...]
    """

    cards: List[Tuple[str, str]] = Field(
        ...,
        min_length=5,
        max_length=5,
        description="List of 5 cards as (rank, suit) tuples",
        examples=[
            [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")],
        ],
    )

    @field_validator("cards")
    @classmethod
    def validate_cards(cls, v: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Validate that all cards are valid and no duplicates."""
        # Validate each card
        for card in v:
            if not is_valid_card_tuple(card):
                raise ValueError(f"Invalid card: {card}")

        # Check for duplicates
        if has_duplicates(v):
            raise ValueError("Hand cannot contain duplicate cards")

        return v


class CompareRequest(BaseModel):
    """
    Request model for comparing two poker hands.

    Attributes:
        hand1: First hand as list of 5 card tuples
        hand2: Second hand as list of 5 card tuples
    """

    hand1: List[Tuple[str, str]] = Field(
        ...,
        min_length=5,
        max_length=5,
        description="First hand - list of 5 cards as (rank, suit) tuples",
    )

    hand2: List[Tuple[str, str]] = Field(
        ...,
        min_length=5,
        max_length=5,
        description="Second hand - list of 5 cards as (rank, suit) tuples",
    )

    @field_validator("hand1", "hand2")
    @classmethod
    def validate_hand(cls, v: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
        """Validate that all cards are valid and no duplicates."""
        for card in v:
            if not is_valid_card_tuple(card):
                raise ValueError(f"Invalid card: {card}")

        if has_duplicates(v):
            raise ValueError("Hand cannot contain duplicate cards")

        return v
