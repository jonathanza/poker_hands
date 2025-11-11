"""
Pydantic models for poker cards and hands.

This module defines validated models for cards and hands using Pydantic,
providing automatic validation, serialization, and type checking.
"""

from typing import List, Tuple

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from core.enums import Rank, Suit


class Card(BaseModel):
    """
    A playing card with rank and suit.

    Attributes:
        rank: The card's rank (2-Ace)
        suit: The card's suit (Hearts, Diamonds, Clubs, Spades)
    """

    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    rank: Rank
    suit: Suit

    @field_validator("rank", mode="before")
    @classmethod
    def validate_rank(cls, v: str | int | Rank) -> Rank:
        """Validate and convert rank to Rank enum."""
        if isinstance(v, Rank):
            return v
        if isinstance(v, (str, int)):
            return Rank.from_string(str(v))
        raise ValueError(f"Invalid rank type: {type(v)}")

    @field_validator("suit", mode="before")
    @classmethod
    def validate_suit(cls, v: str | Suit) -> Suit:
        """Validate and convert suit to Suit enum."""
        if isinstance(v, Suit):
            return v
        if isinstance(v, str):
            return Suit.from_string(v)
        raise ValueError(f"Invalid suit type: {type(v)}")

    def __str__(self) -> str:
        """Return string representation of card with Unicode suit symbols."""
        # Map ranks to display strings
        if self.rank.value >= 11:
            rank_display = {11: "J", 12: "Q", 13: "K", 14: "A"}[self.rank.value]
        elif self.rank.value == 10:
            rank_display = "T"
        else:
            rank_display = str(self.rank.value)

        # Map suits to Unicode symbols
        suit_symbols = {"H": "♥", "D": "♦", "C": "♣", "S": "♠"}
        suit_display = suit_symbols[self.suit.value]

        return f"{rank_display}{suit_display}"

    def __hash__(self) -> int:
        """Make Card hashable for use in sets and as dict keys."""
        return hash((self.rank, self.suit))

    @classmethod
    def from_tuple(cls, card_tuple: Tuple[str, str]) -> "Card":
        """
        Create Card from a tuple of (rank, suit).

        Args:
            card_tuple: Tuple of (rank_str, suit_str)

        Returns:
            Card instance

        Example:
            >>> Card.from_tuple(("A", "H"))
            Card(rank=Rank.ACE, suit=Suit.HEARTS)
        """
        rank_str, suit_str = card_tuple
        return cls(rank=rank_str, suit=suit_str)


class Hand(BaseModel):
    """
    A poker hand containing exactly 5 cards.

    Attributes:
        cards: List of 5 Card objects

    The hand automatically validates that:
    - Exactly 5 cards are provided
    - No duplicate cards exist
    """

    model_config = ConfigDict(frozen=True)

    cards: List[Card] = Field(..., min_length=5, max_length=5)

    @model_validator(mode="after")
    def check_no_duplicates(self) -> "Hand":
        """Ensure no duplicate cards in the hand."""
        if len(self.cards) != len(set(self.cards)):
            raise ValueError("Hand cannot contain duplicate cards")
        return self

    @property
    def ranks(self) -> List[int]:
        """Get sorted list of rank values (descending)."""
        return sorted([card.rank.value for card in self.cards], reverse=True)

    @property
    def suits(self) -> List[str]:
        """Get list of suit values."""
        return [card.suit.value for card in self.cards]

    @property
    def is_flush(self) -> bool:
        """Check if all cards have the same suit."""
        return len(set(self.suits)) == 1

    @property
    def is_straight(self) -> bool:
        """Check if cards form a consecutive sequence."""
        sorted_ranks = sorted(self.ranks)
        return (max(sorted_ranks) - min(sorted_ranks) == 4) and len(
            set(sorted_ranks)
        ) == 5

    def __str__(self) -> str:
        """Return string representation of hand."""
        return " ".join(str(card) for card in self.cards)

    @classmethod
    def from_tuples(cls, card_tuples: List[Tuple[str, str]]) -> "Hand":
        """
        Create Hand from a list of (rank, suit) tuples.

        Args:
            card_tuples: List of tuples like [("A", "H"), ("K", "H"), ...]

        Returns:
            Hand instance

        Example:
            >>> Hand.from_tuples([("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")])
            Hand(cards=[...])
        """
        cards = [Card.from_tuple(t) for t in card_tuples]
        return cls(cards=cards)
