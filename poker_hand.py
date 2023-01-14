"""
A class representing a hand of poker cards. It includes methods for initializing the hand,
classifying the hand, and returning a string representation of the cards in the hand.
"""

import collections
from enum import Enum
from typing import List, Tuple


class Rank(Enum):
    """
    An enumeration class representing the ranks of cards in a poker hand.
    The ranks are T, J, Q, K, and A, with corresponding values of 10, 11, 12, 13, and 14.
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
    A class representing a hand of poker cards. It includes methods for initializing the hand,
    classifying the hand, and returning a string representation of the cards in the hand.
    """

    def __init__(self, cards: List[Tuple[str, str]]) -> None:
        """
        Initializes a PokerHand instance with a list of cards represented as
        tuples of rank and suit.
        :param cards: List of cards represented as tuples of rank and suit.
        :type cards: List[Tuple[str, str]]
        """
        self.cards: List[Tuple[str, str]] = cards
        self.ranks: List[int] = [
            int(r) if r.isdigit() else Rank[r.upper()].value for r, s in cards
        ]
        self.ranks.sort(reverse=True)
        self.suits: List[str] = [s for r, s in cards]
        self.is_flush: bool = len(set(self.suits)) == 1
        self.is_straight: bool = (max(self.ranks) - min(self.ranks) == 4) and len(
            set(self.ranks)
        ) == 5

    def classify(self) -> str:
        """
        Classifies the PokerHand instance into one of the following categories:
        'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush',
        'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card'

        :return: the classification of the PokerHand instance
        :rtype: str
        """
        counter = collections.Counter(self.ranks)
        conditions = {
            (self.is_flush, self.is_straight, min(self.ranks) == 10): "Royal Flush",
            (self.is_flush, self.is_straight): "Straight Flush",
            (counter.most_common(1)[0][1] == 4,): "Four of a Kind",
            (
                counter.most_common(2)[0][1] == 3,
                counter.most_common(2)[1][1] == 2,
            ): "Full House",
            (counter.most_common(2)[0][1] == 3,): "Three of a Kind",
            (self.is_flush,): "Flush",
            (self.is_straight,): "Straight",
            (
                counter.most_common(2)[0][1] == 2,
                counter.most_common(2)[1][1] == 2,
            ): "Two Pair",
            (counter.most_common(2)[0][1] == 2,): "One Pair",
        }
        for condition, hand in conditions.items():
            if all(condition):
                return hand
        return "High Card"

    def __str__(self) -> str:
        """
        Return the string representation of the cards in the hand
        :return: the string representation of the cards in the hand
        :rtype: str
        """
        return " ".join(f"{r} {s}" for r, s in self.cards)
