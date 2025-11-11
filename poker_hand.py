"""
A class representing a hand of poker cards. It includes methods for
initializing the hand, classifying the hand, and returning a string
representation of the cards in the hand.

This module provides backward-compatible wrapper around the new core library.
"""

from enum import Enum
from typing import List, Tuple

from core import Card, Hand, HandClassifier, HandType


class Rank(Enum):
    """
    An enumeration class representing the ranks of cards in a poker hand.
    The ranks are T, J, Q, K, and A, with corresponding values of
    10, 11, 12, 13, and 14.

    This is a backward-compatible wrapper around core.enums.Rank.
    """

    T = 10
    TEN = 10
    J = 11
    JACK = 11
    Q = 12
    QUEEN = 12
    K = 13
    KING = 13
    A = 14
    ACE = 14

    def __init__(self, value: int) -> None:
        """
        Initializes a Rank instance with a value.
        :param value: the value of the rank
        :type value: int
        """
        self._value_ = value


class PokerHand:
    """
    A class representing a hand of poker cards. It includes methods for
    initializing the hand, classifying the hand, and returning a string
    representation of the cards in the hand.

    This is a backward-compatible wrapper around the new core library.
    """

    def __init__(self, cards: List[Tuple[str, str]]) -> None:
        """
        Initializes a PokerHand instance with a list of cards represented as
        tuples of rank and suit.
        :param cards: List of cards represented as tuples of rank and suit.
        :type cards: List[Tuple[str, str]]
        """
        self.cards: List[Tuple[str, str]] = cards

        # Convert to core Card objects
        core_cards = [Card(rank=r, suit=s) for r, s in cards]

        # Create core Hand object
        self._hand = Hand(cards=core_cards)

        # Expose properties for backward compatibility
        self.ranks: List[int] = sorted(
            [card.rank.value for card in self._hand.cards], reverse=True
        )
        self.suits: List[str] = [card.suit.value for card in self._hand.cards]
        self.is_flush: bool = self._hand.is_flush
        self.is_straight: bool = self._hand.is_straight

    def classify(self) -> str:
        """
        Classifies the PokerHand instance into one of the following categories:
        'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush',
        'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card'

        :return: the classification of the PokerHand instance
        :rtype: str
        """
        hand_type = HandClassifier.classify(self._hand)

        # Map HandType enum to string names for backward compatibility
        hand_type_names = {
            HandType.ROYAL_FLUSH: "Royal Flush",
            HandType.STRAIGHT_FLUSH: "Straight Flush",
            HandType.FOUR_OF_A_KIND: "Four of a Kind",
            HandType.FULL_HOUSE: "Full House",
            HandType.FLUSH: "Flush",
            HandType.STRAIGHT: "Straight",
            HandType.THREE_OF_A_KIND: "Three of a Kind",
            HandType.TWO_PAIR: "Two Pair",
            HandType.ONE_PAIR: "One Pair",
            HandType.HIGH_CARD: "High Card",
        }

        return hand_type_names[hand_type]

    def __str__(self) -> str:
        """
        Return the string representation of the cards in the hand
        :return: the string representation of the cards in the hand
        :rtype: str
        """
        return " ".join(f"{r} {s}" for r, s in self.cards)
