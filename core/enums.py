"""
Enumerations for poker hands.

This module defines the enums used throughout the poker hand classification
system, including card ranks, suits, and hand types.
"""

from enum import Enum, IntEnum


class Rank(IntEnum):
    """
    Card rank enumeration with numeric values for comparison.

    Ranks are ordered from lowest (2) to highest (Ace).
    Numeric cards have their face value, while face cards and Ace
    have values 11-14.
    """

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    T = 10  # Alternate notation
    JACK = 11
    J = 11  # Alternate notation
    QUEEN = 12
    Q = 12  # Alternate notation
    KING = 13
    K = 13  # Alternate notation
    ACE = 14
    A = 14  # Alternate notation

    @classmethod
    def from_string(cls, value: str) -> "Rank":
        """
        Convert string representation to Rank enum.

        Args:
            value: String representation of rank (e.g., "A", "Ace", "10", "2")

        Returns:
            Corresponding Rank enum value

        Raises:
            ValueError: If value is not a valid rank
        """
        value_upper = value.upper()

        # Try direct enum lookup
        try:
            return cls[value_upper]
        except KeyError:
            pass

        # Try numeric value (only 2-10 allowed as digits)
        if value.isdigit():
            numeric = int(value)
            if 2 <= numeric <= 10:
                for rank in cls:
                    if rank.value == numeric:
                        return rank
            # 11, 12, 13, 14 are not valid digit inputs - use J, Q, K, A instead
            raise ValueError(
                f"Invalid numeric rank: {value}. Use 2-10 for numbers, "
                "or J/Q/K/A for face cards."
            )

        raise ValueError(f"Invalid rank: {value}")


class Suit(str, Enum):
    """
    Card suit enumeration.

    Supports both full names and single-letter abbreviations.
    """

    HEARTS = "H"
    H = "H"
    DIAMONDS = "D"
    D = "D"
    CLUBS = "C"
    C = "C"
    SPADES = "S"
    S = "S"

    @classmethod
    def from_string(cls, value: str) -> "Suit":
        """
        Convert string representation to Suit enum.

        Args:
            value: String representation of suit (e.g., "H", "Hearts", "hearts")

        Returns:
            Corresponding Suit enum value

        Raises:
            ValueError: If value is not a valid suit
        """
        value_upper = value.upper()

        # Try direct enum lookup
        try:
            return cls[value_upper]
        except KeyError:
            pass

        # Check if it's already a valid value
        for suit in cls:
            if suit.value == value_upper:
                return suit

        raise ValueError(f"Invalid suit: {value}")


class HandType(IntEnum):
    """
    Poker hand type enumeration ordered by strength.

    Higher values indicate stronger hands. This allows for easy
    comparison of hand strengths.
    """

    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10

    def __str__(self) -> str:
        """Return human-readable hand type name."""
        return self.name.replace("_", " ").title()
