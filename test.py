import unittest

class TestPokerHand(unittest.TestCase):
    def test_royal_flush(self):
        cards = [("A", "spades"), ("K", "spades"), ("Q", "spades"), ("J", "spades"), ("10", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Royal Flush")

    def test_straight_flush(self):
        cards = [("9", "spades"), ("8", "spades"), ("7", "spades"), ("6", "spades"), ("5", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Straight Flush")

    def test_four_of_a_kind(self):
        cards = [("A", "spades"), ("A", "hearts"), ("A", "diamonds"), ("A", "clubs"), ("K", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Four of a Kind")

    def test_full_house(self):
        cards = [("A", "spades"), ("A", "hearts"), ("A", "diamonds"), ("K", "spades"), ("K", "hearts")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Full House")

    def test_flush(self):
        cards = [("A", "spades"), ("K", "spades"), ("Q", "spades"), ("J", "spades"), ("10", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Flush")

    def test_straight(self):
        cards = [("9", "spades"), ("8", "hearts"), ("7", "diamonds"), ("6", "clubs"), ("5", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Straight")

    def test_three_of_a_kind(self):
        cards = [("A", "spades"), ("A", "hearts"), ("A", "diamonds"), ("K", "spades"), ("Q", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Three of a Kind")

    def test_two_pair(self):
        cards = [("A", "spades"), ("A", "hearts"), ("K", "diamonds"), ("K", "spades"), ("Q", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "Two Pair")

    def test_one_pair(self):
        cards = [("A", "spades"), ("A", "hearts"), ("K", "diamonds"), ("Q", "spades"), ("J", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "One Pair")

    def test_high_card(self):
        cards = [("A", "spades"), ("K", "hearts"), ("Q", "diamonds"), ("J", "clubs"), ("8", "spades")]
        hand = PokerHand(cards)
        self.assertEqual(hand.classify(), "High Card")
