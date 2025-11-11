"""
Property-based tests for the poker hand library using Hypothesis.

These tests verify that certain properties hold true for all inputs,
rather than testing specific examples.
"""

import unittest
from typing import List, Tuple

from hypothesis import given, strategies as st

from core import Card, Hand, HandClassifier, HandType, Rank, Suit


# Strategies for generating test data
@st.composite
def rank_strategy(draw):
    """Generate a valid rank string."""
    return draw(
        st.sampled_from(
            [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "J",
                "Q",
                "K",
                "A",
            ]
        )
    )


@st.composite
def suit_strategy(draw):
    """Generate a valid suit string."""
    return draw(st.sampled_from(["H", "D", "C", "S"]))


@st.composite
def card_strategy(draw):
    """Generate a valid Card."""
    rank = draw(rank_strategy())
    suit = draw(suit_strategy())
    return Card(rank=rank, suit=suit)


@st.composite
def hand_strategy(draw):
    """Generate a valid 5-card Hand (no duplicates)."""
    # Generate all 52 possible cards
    all_cards = [
        (r, s)
        for r in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for s in ["H", "D", "C", "S"]
    ]

    # Sample 5 unique cards
    sampled = draw(st.sampled_from(all_cards))
    remaining = [c for c in all_cards if c != sampled]

    cards = [sampled]
    for _ in range(4):
        next_card = draw(st.sampled_from(remaining))
        cards.append(next_card)
        remaining = [c for c in remaining if c != next_card]

    return Hand(cards=[Card(rank=r, suit=s) for r, s in cards])


class TestCardProperties(unittest.TestCase):
    """Property-based tests for Card model."""

    @given(rank_strategy(), suit_strategy())
    def test_card_creation_always_succeeds(self, rank: str, suit: str):
        """Valid rank and suit should always create a Card."""
        card = Card(rank=rank, suit=suit)
        self.assertIsInstance(card, Card)

    @given(rank_strategy(), suit_strategy())
    def test_card_rank_in_valid_range(self, rank: str, suit: str):
        """Card rank value should always be in range 2-14."""
        card = Card(rank=rank, suit=suit)
        self.assertGreaterEqual(card.rank.value, 2)
        self.assertLessEqual(card.rank.value, 14)

    @given(rank_strategy(), suit_strategy())
    def test_card_suit_is_valid(self, rank: str, suit: str):
        """Card suit should always be H, D, C, or S."""
        card = Card(rank=rank, suit=suit)
        self.assertIn(card.suit.value, ["H", "D", "C", "S"])

    @given(rank_strategy(), suit_strategy())
    def test_card_immutable(self, rank: str, suit: str):
        """Cards should be immutable."""
        card = Card(rank=rank, suit=suit)
        original_rank = card.rank
        # Trying to modify should fail (frozen model)
        try:
            card.rank = Rank.ACE  # type: ignore
            self.fail("Card should be immutable")
        except Exception:
            # Expected to fail
            pass
        # Rank should remain unchanged
        self.assertEqual(card.rank, original_rank)

    @given(rank_strategy(), suit_strategy())
    def test_card_equality_reflexive(self, rank: str, suit: str):
        """A card should always equal itself."""
        card = Card(rank=rank, suit=suit)
        self.assertEqual(card, card)

    @given(rank_strategy(), suit_strategy())
    def test_card_equality_symmetric(self, rank: str, suit: str):
        """If card1 == card2, then card2 == card1."""
        card1 = Card(rank=rank, suit=suit)
        card2 = Card(rank=rank, suit=suit)
        self.assertEqual(card1, card2)
        self.assertEqual(card2, card1)

    @given(rank_strategy(), suit_strategy())
    def test_card_string_representation_not_empty(self, rank: str, suit: str):
        """Card string representation should never be empty."""
        card = Card(rank=rank, suit=suit)
        self.assertGreater(len(str(card)), 0)


class TestHandProperties(unittest.TestCase):
    """Property-based tests for Hand model."""

    @given(hand_strategy())
    def test_hand_always_has_5_cards(self, hand: Hand):
        """Hands should always have exactly 5 cards."""
        self.assertEqual(len(hand.cards), 5)

    @given(hand_strategy())
    def test_hand_has_no_duplicates(self, hand: Hand):
        """Hands should never have duplicate cards."""
        self.assertEqual(len(hand.cards), len(set(hand.cards)))

    @given(hand_strategy())
    def test_hand_ranks_sorted_descending(self, hand: Hand):
        """Hand ranks property should be sorted descending."""
        ranks = hand.ranks
        self.assertEqual(ranks, sorted(ranks, reverse=True))

    @given(hand_strategy())
    def test_hand_is_flush_consistent(self, hand: Hand):
        """is_flush property should match actual suit distribution."""
        suits = hand.suits
        all_same = len(set(suits)) == 1
        self.assertEqual(hand.is_flush, all_same)

    @given(hand_strategy())
    def test_hand_is_straight_consistent(self, hand: Hand):
        """is_straight property should match actual rank distribution."""
        sorted_ranks = sorted(hand.ranks)
        is_consecutive = (max(sorted_ranks) - min(sorted_ranks) == 4) and len(
            set(sorted_ranks)
        ) == 5
        self.assertEqual(hand.is_straight, is_consecutive)


class TestClassifierProperties(unittest.TestCase):
    """Property-based tests for HandClassifier."""

    @given(hand_strategy())
    def test_classification_is_deterministic(self, hand: Hand):
        """Same hand should always classify to the same type."""
        result1 = HandClassifier.classify(hand)
        result2 = HandClassifier.classify(hand)
        self.assertEqual(result1, result2)

    @given(hand_strategy())
    def test_classification_returns_valid_hand_type(self, hand: Hand):
        """Classification should always return a valid HandType."""
        result = HandClassifier.classify(hand)
        self.assertIsInstance(result, HandType)
        self.assertIn(result, list(HandType))

    @given(hand_strategy())
    def test_classification_in_valid_range(self, hand: Hand):
        """Hand type value should be in range 1-10."""
        result = HandClassifier.classify(hand)
        self.assertGreaterEqual(result.value, 1)
        self.assertLessEqual(result.value, 10)

    @given(hand_strategy())
    def test_royal_flush_is_strongest(self, hand: Hand):
        """Royal flush should have the highest value."""
        result = HandClassifier.classify(hand)
        if result == HandType.ROYAL_FLUSH:
            self.assertEqual(result.value, 10)

    @given(hand_strategy())
    def test_high_card_is_weakest(self, hand: Hand):
        """High card should have the lowest value."""
        result = HandClassifier.classify(hand)
        if result == HandType.HIGH_CARD:
            self.assertEqual(result.value, 1)

    @given(hand_strategy())
    def test_flush_requires_all_same_suit(self, hand: Hand):
        """Flush/Straight Flush/Royal Flush require all cards same suit."""
        result = HandClassifier.classify(hand)
        if result in {
            HandType.FLUSH,
            HandType.STRAIGHT_FLUSH,
            HandType.ROYAL_FLUSH,
        }:
            self.assertTrue(hand.is_flush)

    @given(hand_strategy())
    def test_straight_requires_consecutive_ranks(self, hand: Hand):
        """Straight/Straight Flush/Royal Flush require consecutive ranks."""
        result = HandClassifier.classify(hand)
        if result in {
            HandType.STRAIGHT,
            HandType.STRAIGHT_FLUSH,
            HandType.ROYAL_FLUSH,
        }:
            self.assertTrue(hand.is_straight)


class TestRankProperties(unittest.TestCase):
    """Property-based tests for Rank enum."""

    @given(
        st.sampled_from(
            [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "T",
                "J",
                "Q",
                "K",
                "A",
                "ace",
                "king",
            ]
        )
    )
    def test_from_string_is_idempotent(self, rank_str: str):
        """Converting to Rank and back should preserve meaning."""
        rank = Rank.from_string(rank_str)
        # Converting again should give same result
        rank2 = Rank.from_string(str(rank.value) if rank.value <= 10 else rank.name[0])
        self.assertEqual(rank, rank2)

    @given(st.integers(min_value=2, max_value=14))
    def test_rank_comparison_matches_value(self, value: int):
        """Rank comparison should match integer value comparison."""
        # Find the rank with this value
        rank = None
        for r in Rank:
            if r.value == value:
                rank = r
                break

        if rank:
            # Rank should be less than any rank with higher value
            for r in Rank:
                if r.value > value:
                    self.assertLess(rank, r)
                elif r.value < value:
                    self.assertGreater(rank, r)


class TestHandTypeProperties(unittest.TestCase):
    """Property-based tests for HandType enum."""

    @given(st.sampled_from(list(HandType)), st.sampled_from(list(HandType)))
    def test_hand_type_comparison_transitive(self, type1: HandType, type2: HandType):
        """If A < B and B < C, then A < C."""
        if type1 < type2:
            for type3 in HandType:
                if type2 < type3:
                    self.assertLess(type1, type3)

    @given(st.sampled_from(list(HandType)))
    def test_hand_type_string_representation(self, hand_type: HandType):
        """HandType string should be readable."""
        string_repr = str(hand_type)
        self.assertIsInstance(string_repr, str)
        self.assertGreater(len(string_repr), 0)


if __name__ == "__main__":
    unittest.main()
