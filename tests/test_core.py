"""
Comprehensive tests for the core poker hand library.

Tests all core modules: enums, models, classifier, and validators.
"""

import unittest
from typing import List, Tuple

from pydantic import ValidationError

from core import Card, Hand, HandClassifier, HandType, Rank, Suit
from core.validators import (
    has_duplicates,
    is_valid_card_tuple,
    is_valid_rank,
    is_valid_suit,
)


class TestRankEnum(unittest.TestCase):
    """Test cases for the Rank enum."""

    def test_rank_values(self):
        """Test that ranks have correct integer values."""
        self.assertEqual(Rank.TWO.value, 2)
        self.assertEqual(Rank.TEN.value, 10)
        self.assertEqual(Rank.JACK.value, 11)
        self.assertEqual(Rank.QUEEN.value, 12)
        self.assertEqual(Rank.KING.value, 13)
        self.assertEqual(Rank.ACE.value, 14)

    def test_rank_alternates(self):
        """Test alternate rank names."""
        self.assertEqual(Rank.T, Rank.TEN)
        self.assertEqual(Rank.J, Rank.JACK)
        self.assertEqual(Rank.Q, Rank.QUEEN)
        self.assertEqual(Rank.K, Rank.KING)
        self.assertEqual(Rank.A, Rank.ACE)

    def test_rank_from_string(self):
        """Test Rank.from_string() conversion."""
        test_cases = [
            ("2", Rank.TWO),
            ("10", Rank.TEN),
            ("T", Rank.TEN),
            ("t", Rank.TEN),
            ("ten", Rank.TEN),
            ("J", Rank.JACK),
            ("jack", Rank.JACK),
            ("Q", Rank.QUEEN),
            ("queen", Rank.QUEEN),
            ("K", Rank.KING),
            ("king", Rank.KING),
            ("A", Rank.ACE),
            ("ace", Rank.ACE),
        ]

        for input_str, expected_rank in test_cases:
            with self.subTest(input=input_str):
                self.assertEqual(Rank.from_string(input_str), expected_rank)

    def test_rank_from_string_invalid(self):
        """Test Rank.from_string() with invalid input."""
        invalid_inputs = ["X", "1", "11", "invalid", ""]

        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError):
                    Rank.from_string(invalid_input)

    def test_rank_comparison(self):
        """Test that ranks can be compared."""
        self.assertLess(Rank.TWO, Rank.THREE)
        self.assertLess(Rank.JACK, Rank.QUEEN)
        self.assertLess(Rank.KING, Rank.ACE)
        self.assertGreater(Rank.ACE, Rank.TWO)


class TestSuitEnum(unittest.TestCase):
    """Test cases for the Suit enum."""

    def test_suit_values(self):
        """Test that suits have correct values."""
        self.assertEqual(Suit.HEARTS.value, "H")
        self.assertEqual(Suit.DIAMONDS.value, "D")
        self.assertEqual(Suit.CLUBS.value, "C")
        self.assertEqual(Suit.SPADES.value, "S")

    def test_suit_from_string(self):
        """Test Suit.from_string() conversion."""
        test_cases = [
            ("H", Suit.HEARTS),
            ("h", Suit.HEARTS),
            ("hearts", Suit.HEARTS),
            ("Hearts", Suit.HEARTS),
            ("D", Suit.DIAMONDS),
            ("diamonds", Suit.DIAMONDS),
            ("C", Suit.CLUBS),
            ("clubs", Suit.CLUBS),
            ("S", Suit.SPADES),
            ("spades", Suit.SPADES),
        ]

        for input_str, expected_suit in test_cases:
            with self.subTest(input=input_str):
                self.assertEqual(Suit.from_string(input_str), expected_suit)

    def test_suit_from_string_invalid(self):
        """Test Suit.from_string() with invalid input."""
        invalid_inputs = ["X", "heart", "invalid", ""]

        for invalid_input in invalid_inputs:
            with self.subTest(input=invalid_input):
                with self.assertRaises(ValueError):
                    Suit.from_string(invalid_input)


class TestHandTypeEnum(unittest.TestCase):
    """Test cases for the HandType enum."""

    def test_hand_type_values(self):
        """Test that hand types have correct values."""
        self.assertEqual(HandType.HIGH_CARD.value, 1)
        self.assertEqual(HandType.ONE_PAIR.value, 2)
        self.assertEqual(HandType.TWO_PAIR.value, 3)
        self.assertEqual(HandType.THREE_OF_A_KIND.value, 4)
        self.assertEqual(HandType.STRAIGHT.value, 5)
        self.assertEqual(HandType.FLUSH.value, 6)
        self.assertEqual(HandType.FULL_HOUSE.value, 7)
        self.assertEqual(HandType.FOUR_OF_A_KIND.value, 8)
        self.assertEqual(HandType.STRAIGHT_FLUSH.value, 9)
        self.assertEqual(HandType.ROYAL_FLUSH.value, 10)

    def test_hand_type_ordering(self):
        """Test that hand types are ordered by strength."""
        self.assertLess(HandType.HIGH_CARD, HandType.ONE_PAIR)
        self.assertLess(HandType.TWO_PAIR, HandType.STRAIGHT)
        self.assertLess(HandType.FLUSH, HandType.FULL_HOUSE)
        self.assertLess(HandType.STRAIGHT_FLUSH, HandType.ROYAL_FLUSH)


class TestCard(unittest.TestCase):
    """Test cases for the Card model."""

    def test_card_creation(self):
        """Test creating valid cards."""
        card = Card(rank="A", suit="H")
        self.assertEqual(card.rank, Rank.ACE)
        self.assertEqual(card.suit, Suit.HEARTS)

    def test_card_creation_various_formats(self):
        """Test card creation with various input formats."""
        test_cases = [
            (("A", "H"), Rank.ACE, Suit.HEARTS),
            (("ace", "hearts"), Rank.ACE, Suit.HEARTS),
            (("K", "S"), Rank.KING, Suit.SPADES),
            (("10", "D"), Rank.TEN, Suit.DIAMONDS),
            (("T", "C"), Rank.TEN, Suit.CLUBS),
        ]

        for (rank_input, suit_input), expected_rank, expected_suit in test_cases:
            with self.subTest(rank=rank_input, suit=suit_input):
                card = Card(rank=rank_input, suit=suit_input)
                self.assertEqual(card.rank, expected_rank)
                self.assertEqual(card.suit, expected_suit)

    def test_card_immutability(self):
        """Test that cards are immutable (frozen)."""
        card = Card(rank="A", suit="H")
        with self.assertRaises(ValidationError):
            card.rank = Rank.KING  # type: ignore

    def test_card_invalid_rank(self):
        """Test card creation with invalid rank."""
        with self.assertRaises(ValidationError):
            Card(rank="X", suit="H")

    def test_card_invalid_suit(self):
        """Test card creation with invalid suit."""
        with self.assertRaises(ValidationError):
            Card(rank="A", suit="X")

    def test_card_string_representation(self):
        """Test card string representation."""
        card = Card(rank="A", suit="H")
        self.assertEqual(str(card), "A♥")

        card2 = Card(rank="K", suit="S")
        self.assertEqual(str(card2), "K♠")

    def test_card_equality(self):
        """Test card equality."""
        card1 = Card(rank="A", suit="H")
        card2 = Card(rank="A", suit="H")
        card3 = Card(rank="K", suit="H")

        self.assertEqual(card1, card2)
        self.assertNotEqual(card1, card3)


class TestHand(unittest.TestCase):
    """Test cases for the Hand model."""

    def test_hand_creation(self):
        """Test creating a valid hand."""
        cards = [
            Card(rank="A", suit="H"),
            Card(rank="K", suit="H"),
            Card(rank="Q", suit="H"),
            Card(rank="J", suit="H"),
            Card(rank="T", suit="H"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(len(hand.cards), 5)

    def test_hand_requires_5_cards(self):
        """Test that hand requires exactly 5 cards."""
        # Too few cards
        with self.assertRaises(ValidationError):
            Hand(cards=[Card(rank="A", suit="H")])

        # Too many cards
        with self.assertRaises(ValidationError):
            Hand(
                cards=[
                    Card(rank="A", suit="H"),
                    Card(rank="K", suit="H"),
                    Card(rank="Q", suit="H"),
                    Card(rank="J", suit="H"),
                    Card(rank="T", suit="H"),
                    Card(rank="9", suit="H"),
                ]
            )

    def test_hand_no_duplicates(self):
        """Test that hand cannot contain duplicate cards."""
        with self.assertRaises(ValidationError):
            Hand(
                cards=[
                    Card(rank="A", suit="H"),
                    Card(rank="A", suit="H"),  # Duplicate
                    Card(rank="K", suit="H"),
                    Card(rank="Q", suit="H"),
                    Card(rank="J", suit="H"),
                ]
            )

    def test_hand_is_flush(self):
        """Test is_flush property."""
        # Flush
        flush_hand = Hand(
            cards=[
                Card(rank="A", suit="H"),
                Card(rank="K", suit="H"),
                Card(rank="9", suit="H"),
                Card(rank="5", suit="H"),
                Card(rank="2", suit="H"),
            ]
        )
        self.assertTrue(flush_hand.is_flush)

        # Not flush
        non_flush_hand = Hand(
            cards=[
                Card(rank="A", suit="H"),
                Card(rank="K", suit="S"),  # Different suit
                Card(rank="Q", suit="H"),
                Card(rank="J", suit="H"),
                Card(rank="T", suit="H"),
            ]
        )
        self.assertFalse(non_flush_hand.is_flush)

    def test_hand_is_straight(self):
        """Test is_straight property."""
        # Straight
        straight_hand = Hand(
            cards=[
                Card(rank="9", suit="H"),
                Card(rank="8", suit="S"),
                Card(rank="7", suit="D"),
                Card(rank="6", suit="C"),
                Card(rank="5", suit="H"),
            ]
        )
        self.assertTrue(straight_hand.is_straight)

        # Not straight
        non_straight_hand = Hand(
            cards=[
                Card(rank="A", suit="H"),
                Card(rank="K", suit="S"),
                Card(rank="9", suit="D"),
                Card(rank="5", suit="C"),
                Card(rank="2", suit="H"),
            ]
        )
        self.assertFalse(non_straight_hand.is_straight)

    def test_hand_ranks(self):
        """Test ranks property returns sorted values."""
        hand = Hand(
            cards=[
                Card(rank="5", suit="H"),
                Card(rank="A", suit="S"),
                Card(rank="K", suit="D"),
                Card(rank="2", suit="C"),
                Card(rank="9", suit="H"),
            ]
        )
        # Should be sorted descending
        self.assertEqual(hand.ranks, [14, 13, 9, 5, 2])


class TestHandClassifier(unittest.TestCase):
    """Test cases for the HandClassifier."""

    def _create_hand(self, cards: List[Tuple[str, str]]) -> Hand:
        """Helper to create a Hand from tuples."""
        return Hand(cards=[Card(rank=r, suit=s) for r, s in cards])

    def test_royal_flush(self):
        """Test royal flush classification."""
        test_cases = [
            [("A", "S"), ("K", "S"), ("Q", "S"), ("J", "S"), ("10", "S")],
            [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("10", "H")],
            [("A", "C"), ("K", "C"), ("Q", "C"), ("J", "C"), ("10", "C")],
            [("A", "D"), ("K", "D"), ("Q", "D"), ("J", "D"), ("10", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.ROYAL_FLUSH)

    def test_straight_flush(self):
        """Test straight flush classification."""
        test_cases = [
            [("9", "S"), ("8", "S"), ("7", "S"), ("6", "S"), ("5", "S")],
            [("10", "H"), ("9", "H"), ("8", "H"), ("7", "H"), ("6", "H")],
            [("Q", "D"), ("J", "D"), ("10", "D"), ("9", "D"), ("8", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.STRAIGHT_FLUSH)

    def test_four_of_a_kind(self):
        """Test four of a kind classification."""
        test_cases = [
            [("9", "S"), ("9", "H"), ("9", "D"), ("9", "C"), ("5", "S")],
            [("J", "S"), ("J", "H"), ("J", "D"), ("J", "C"), ("3", "S")],
            [("Q", "D"), ("Q", "H"), ("Q", "S"), ("Q", "C"), ("K", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.FOUR_OF_A_KIND)

    def test_full_house(self):
        """Test full house classification."""
        test_cases = [
            [("9", "S"), ("9", "H"), ("9", "D"), ("5", "S"), ("5", "H")],
            [("J", "S"), ("J", "H"), ("J", "D"), ("4", "S"), ("4", "H")],
            [("Q", "D"), ("Q", "H"), ("Q", "S"), ("K", "D"), ("K", "S")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.FULL_HOUSE)

    def test_flush(self):
        """Test flush classification."""
        test_cases = [
            [("9", "S"), ("7", "S"), ("6", "S"), ("4", "S"), ("2", "S")],
            [("J", "H"), ("10", "H"), ("9", "H"), ("8", "H"), ("3", "H")],
            [("Q", "D"), ("J", "D"), ("10", "D"), ("7", "D"), ("6", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.FLUSH)

    def test_straight(self):
        """Test straight classification."""
        test_cases = [
            [("9", "S"), ("8", "H"), ("7", "D"), ("6", "C"), ("5", "S")],
            [("10", "H"), ("9", "S"), ("8", "C"), ("7", "D"), ("6", "H")],
            [("Q", "D"), ("J", "H"), ("10", "S"), ("9", "C"), ("8", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.STRAIGHT)

    def test_three_of_a_kind(self):
        """Test three of a kind classification."""
        test_cases = [
            [("9", "S"), ("9", "H"), ("9", "D"), ("7", "C"), ("5", "S")],
            [("J", "H"), ("J", "S"), ("J", "C"), ("10", "D"), ("3", "H")],
            [("Q", "D"), ("Q", "H"), ("Q", "S"), ("J", "C"), ("2", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(
                    HandClassifier.classify(hand), HandType.THREE_OF_A_KIND
                )

    def test_two_pair(self):
        """Test two pair classification."""
        test_cases = [
            [("9", "S"), ("9", "H"), ("7", "D"), ("7", "C"), ("5", "S")],
            [("J", "H"), ("J", "S"), ("10", "C"), ("10", "D"), ("3", "H")],
            [("Q", "D"), ("Q", "H"), ("J", "S"), ("J", "C"), ("2", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.TWO_PAIR)

    def test_one_pair(self):
        """Test one pair classification."""
        test_cases = [
            [("9", "S"), ("9", "H"), ("7", "D"), ("4", "C"), ("5", "S")],
            [("J", "H"), ("J", "S"), ("10", "C"), ("6", "D"), ("3", "H")],
            [("Q", "D"), ("Q", "H"), ("J", "S"), ("3", "C"), ("4", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.ONE_PAIR)

    def test_high_card(self):
        """Test high card classification."""
        test_cases = [
            [("9", "S"), ("5", "H"), ("7", "D"), ("4", "C"), ("3", "S")],
            [("J", "H"), ("10", "S"), ("8", "C"), ("6", "D"), ("2", "H")],
            [("Q", "D"), ("K", "H"), ("J", "H"), ("8", "C"), ("2", "D")],
        ]

        for cards in test_cases:
            with self.subTest(cards=cards):
                hand = self._create_hand(cards)
                self.assertEqual(HandClassifier.classify(hand), HandType.HIGH_CARD)


class TestValidators(unittest.TestCase):
    """Test cases for validator functions."""

    def test_is_valid_rank(self):
        """Test is_valid_rank function."""
        valid_ranks = ["2", "10", "T", "J", "Q", "K", "A", "ace", "king"]
        for rank in valid_ranks:
            with self.subTest(rank=rank):
                self.assertTrue(is_valid_rank(rank))

        invalid_ranks = ["X", "1", "11", "invalid"]
        for rank in invalid_ranks:
            with self.subTest(rank=rank):
                self.assertFalse(is_valid_rank(rank))

    def test_is_valid_suit(self):
        """Test is_valid_suit function."""
        valid_suits = ["H", "D", "C", "S", "hearts", "diamonds", "clubs", "spades"]
        for suit in valid_suits:
            with self.subTest(suit=suit):
                self.assertTrue(is_valid_suit(suit))

        invalid_suits = ["X", "heart", "invalid"]
        for suit in invalid_suits:
            with self.subTest(suit=suit):
                self.assertFalse(is_valid_suit(suit))

    def test_is_valid_card_tuple(self):
        """Test is_valid_card_tuple function."""
        valid_tuples = [("A", "H"), ("K", "S"), ("10", "D"), ("2", "C")]
        for card_tuple in valid_tuples:
            with self.subTest(card=card_tuple):
                self.assertTrue(is_valid_card_tuple(card_tuple))

        invalid_tuples = [
            ("X", "H"),  # Invalid rank
            ("A", "X"),  # Invalid suit
            ("A",),  # Too few elements
            ("A", "H", "extra"),  # Too many elements
        ]
        for card_tuple in invalid_tuples:
            with self.subTest(card=card_tuple):
                self.assertFalse(is_valid_card_tuple(card_tuple))

    def test_has_duplicates(self):
        """Test has_duplicates function."""
        # No duplicates
        self.assertFalse(has_duplicates([("A", "H"), ("K", "S"), ("Q", "D")]))

        # Has duplicates
        self.assertTrue(has_duplicates([("A", "H"), ("A", "H"), ("K", "S")]))


if __name__ == "__main__":
    unittest.main()
