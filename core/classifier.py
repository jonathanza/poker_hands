"""
Poker hand classification logic.

This module contains the core logic for classifying poker hands
into their respective types (Royal Flush, Straight Flush, etc.).
"""

import collections
from typing import Dict, Tuple

from core.enums import HandType
from core.models import Hand


class HandClassifier:
    """
    Classifier for poker hands.

    This class provides methods to analyze and classify poker hands
    according to standard poker rules.
    """

    @staticmethod
    def classify(hand: Hand) -> HandType:
        """
        Classify a poker hand into its type.

        Args:
            hand: A Hand object containing 5 cards

        Returns:
            HandType enum representing the classification

        Example:
            >>> from core.models import Hand
            >>> hand = Hand.from_tuples([
            ...     ("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")
            ... ])
            >>> HandClassifier.classify(hand)
            HandType.ROYAL_FLUSH
        """
        ranks = hand.ranks
        is_flush = hand.is_flush
        is_straight = hand.is_straight

        # Count occurrences of each rank
        counter = collections.Counter(ranks)

        # Define conditions for each hand type
        # Each key is a tuple of conditions, value is the hand type
        conditions: Dict[Tuple[bool, ...], HandType] = {
            # Royal Flush: Flush + Straight + minimum rank is 10
            (is_flush, is_straight, min(ranks) == 10): HandType.ROYAL_FLUSH,
            # Straight Flush: Flush + Straight
            (is_flush, is_straight): HandType.STRAIGHT_FLUSH,
            # Four of a Kind: One rank appears 4 times
            (counter.most_common(1)[0][1] == 4,): HandType.FOUR_OF_A_KIND,
            # Full House: One rank 3 times, another 2 times
            (
                counter.most_common(2)[0][1] == 3,
                counter.most_common(2)[1][1] == 2,
            ): HandType.FULL_HOUSE,
            # Three of a Kind: One rank appears 3 times
            (counter.most_common(1)[0][1] == 3,): HandType.THREE_OF_A_KIND,
            # Flush: All same suit
            (is_flush,): HandType.FLUSH,
            # Straight: Consecutive ranks
            (is_straight,): HandType.STRAIGHT,
            # Two Pair: Two ranks appear 2 times each
            (
                counter.most_common(2)[0][1] == 2,
                counter.most_common(2)[1][1] == 2,
            ): HandType.TWO_PAIR,
            # One Pair: One rank appears 2 times
            (counter.most_common(1)[0][1] == 2,): HandType.ONE_PAIR,
        }

        # Check conditions in order and return first match
        for condition, hand_type in conditions.items():
            if all(condition):
                return hand_type

        # Default to High Card if no other hand is found
        return HandType.HIGH_CARD

    @classmethod
    def classify_string(cls, hand: Hand) -> str:
        """
        Classify a hand and return the string representation.

        Args:
            hand: A Hand object containing 5 cards

        Returns:
            String representation of the hand type

        Example:
            >>> from core.models import Hand
            >>> hand = Hand.from_tuples([
            ...     ("A", "H"), ("K", "D"), ("Q", "C"), ("J", "S"), ("9", "H")
            ... ])
            >>> HandClassifier.classify_string(hand)
            'High Card'
        """
        hand_type = cls.classify(hand)
        return str(hand_type)
