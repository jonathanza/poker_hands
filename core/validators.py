"""
Custom validators for poker hands.

This module provides additional validation functions beyond
what Pydantic offers out of the box.
"""

from typing import List, Tuple

from core.enums import Rank, Suit


def is_valid_rank(rank_str: str) -> bool:
    """
    Check if a string represents a valid card rank.

    Args:
        rank_str: String to validate

    Returns:
        True if valid, False otherwise

    Example:
        >>> is_valid_rank("A")
        True
        >>> is_valid_rank("11")
        False
    """
    try:
        Rank.from_string(rank_str)
        return True
    except ValueError:
        return False


def is_valid_suit(suit_str: str) -> bool:
    """
    Check if a string represents a valid card suit.

    Args:
        suit_str: String to validate

    Returns:
        True if valid, False otherwise

    Example:
        >>> is_valid_suit("H")
        True
        >>> is_valid_suit("X")
        False
    """
    try:
        Suit.from_string(suit_str)
        return True
    except ValueError:
        return False


def is_valid_card_tuple(card_tuple: Tuple[str, str]) -> bool:
    """
    Check if a tuple represents a valid card.

    Args:
        card_tuple: Tuple of (rank, suit) strings

    Returns:
        True if valid, False otherwise

    Example:
        >>> is_valid_card_tuple(("A", "H"))
        True
        >>> is_valid_card_tuple(("X", "Y"))
        False
    """
    if len(card_tuple) != 2:
        return False
    rank_str, suit_str = card_tuple
    return is_valid_rank(rank_str) and is_valid_suit(suit_str)


def has_duplicates(cards: List[Tuple[str, str]]) -> bool:
    """
    Check if a list of card tuples contains duplicates.

    Args:
        cards: List of (rank, suit) tuples

    Returns:
        True if duplicates exist, False otherwise

    Example:
        >>> has_duplicates([("A", "H"), ("A", "H")])
        True
        >>> has_duplicates([("A", "H"), ("K", "H")])
        False
    """
    return len(cards) != len(set(cards))
