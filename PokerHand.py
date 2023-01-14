import collections
from typing import List, Tuple
from enum import Enum


class Rank(Enum):
    """
    An enumeration class representing the ranks of cards in a poker hand.
    The ranks are T, J, Q, K, and A, with corresponding values of 10, 11, 12, 13, and 14.
    """

    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14

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
        Initializes a PokerHand instance with a list of cards represented as tuples of rank and suit.
        :param cards: List of cards represented as tuples of rank and suit.
        :type cards: List[Tuple[str, str]]
        """
        self.cards: List[Tuple[str, str]] = cards
        self.ranks: List[int] = [
            int(r) if r.isdigit() else Rank[r].value for r, s in cards
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
        'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind',
        'Two Pair', 'One Pair', 'High Card'

        :return: the classification of the PokerHand instance
        :rtype: str
        """
        counter = collections.Counter(self.ranks)
        if self.is_flush and self.is_straight:
            if min(self.ranks) == 10:
                return "Royal Flush"
            else:
                return "Straight Flush"
        elif counter.most_common(1)[0][1] == 4:
            return "Four of a Kind"
        elif counter.most_common(2)[0][1] == 3:
            if counter.most_common(2)[1][1] == 2:
                return "Full House"
            else:
                return "Three of a Kind"
        elif self.is_flush:
            return "Flush"
        elif self.is_straight:
            return "Straight"
        elif counter.most_common(2)[0][1] == 2:
            if counter.most_common(2)[1][1] == 2:
                return "Two Pair"
            else:
                return "One Pair"
        else:
            return "High Card"

    def __str__(self) -> str:
        """
        Return the string representation of the cards in the hand
        :return: the string representation of the cards in the hand
        :rtype: str
        """
        return " ".join(f"{r} {s}" for r, s in self.cards)
