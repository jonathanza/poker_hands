"""
A class that contains test cases for the PokerHand class.
It will test the classify method of the PokerHand class by providing test cases
for various types of hands.
"""

import unittest

from poker_hand import PokerHand


class TestPokerHand(unittest.TestCase):
    """
    A class that contains test cases for the PokerHand class.
    It will test the classify method of the PokerHand class by providing test
    cases for various types of hands.
    """

    def test_royal_flush(self):
        """
        Test case that asserts that the classify method returns 'Royal Flush'
        when provided with a list of cards that make a royal flush hand.
        """
        test_cases = [
            [
                ("A", "spades"),
                ("K", "spades"),
                ("Q", "spades"),
                ("J", "spades"),
                ("10", "spades"),
            ],
            [
                ("A", "hearts"),
                ("K", "hearts"),
                ("Q", "hearts"),
                ("J", "hearts"),
                ("10", "hearts"),
            ],
            [
                ("A", "clubs"),
                ("K", "clubs"),
                ("Q", "clubs"),
                ("J", "clubs"),
                ("10", "clubs"),
            ],
            [
                ("A", "diamonds"),
                ("K", "diamonds"),
                ("Q", "diamonds"),
                ("J", "diamonds"),
                ("10", "diamonds"),
            ],
        ]

        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Royal Flush")

    def test_straight_flush(self):
        """
        Test case that asserts that the classify method returns 'Straight Flush'
        when provided with a list of cards that make a straight flush hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("8", "spades"),
                ("7", "spades"),
                ("6", "spades"),
                ("5", "spades"),
            ],
            [
                ("10", "hearts"),
                ("9", "hearts"),
                ("8", "hearts"),
                ("7", "hearts"),
                ("6", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("J", "diamonds"),
                ("10", "diamonds"),
                ("9", "diamonds"),
                ("8", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Straight Flush")

    def test_four_of_a_kind(self):
        """
        Test case that asserts that the classify method returns 'Four of a Kind'
        when provided with a list of cards that make a four of a kind hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("9", "hearts"),
                ("9", "diamonds"),
                ("9", "clubs"),
                ("5", "spades"),
            ],
            [
                ("J", "spades"),
                ("J", "hearts"),
                ("J", "diamonds"),
                ("J", "clubs"),
                ("3", "spades"),
            ],
            [
                ("Q", "diamonds"),
                ("Q", "hearts"),
                ("Q", "spades"),
                ("Q", "clubs"),
                ("K", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Four of a Kind")

    def test_full_house(self):
        """
        Test case that asserts that the classify method returns 'Full House'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("9", "hearts"),
                ("9", "diamonds"),
                ("5", "spades"),
                ("5", "hearts"),
            ],
            [
                ("J", "spades"),
                ("J", "hearts"),
                ("J", "diamonds"),
                ("4", "spades"),
                ("4", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("Q", "hearts"),
                ("Q", "spades"),
                ("K", "diamonds"),
                ("K", "spades"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Full House")

    def test_flush(self):
        """
        Test case that asserts that the classify method returns 'Flush'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("7", "spades"),
                ("6", "spades"),
                ("4", "spades"),
                ("2", "spades"),
            ],
            [
                ("J", "hearts"),
                ("10", "hearts"),
                ("9", "hearts"),
                ("8", "hearts"),
                ("3", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("J", "diamonds"),
                ("10", "diamonds"),
                ("7", "diamonds"),
                ("6", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Flush")

    def test_straight(self):
        """
        Test case that asserts that the classify method returns 'Straight'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("8", "hearts"),
                ("7", "diamonds"),
                ("6", "clubs"),
                ("5", "spades"),
            ],
            [
                ("10", "hearts"),
                ("9", "spades"),
                ("8", "clubs"),
                ("7", "diamonds"),
                ("6", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("J", "hearts"),
                ("10", "spades"),
                ("9", "clubs"),
                ("8", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Straight")

    def test_three_of_a_kind(self):
        """
        Test case that asserts that the classify method returns 'Three of a Kind'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("9", "hearts"),
                ("9", "diamonds"),
                ("7", "clubs"),
                ("5", "spades"),
            ],
            [
                ("J", "hearts"),
                ("J", "spades"),
                ("J", "clubs"),
                ("10", "diamonds"),
                ("3", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("Q", "hearts"),
                ("Q", "spades"),
                ("J", "clubs"),
                ("2", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Three of a Kind")

    def test_two_pair(self):
        """
        Test case that asserts that the classify method returns 'Two Pair'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("9", "hearts"),
                ("7", "diamonds"),
                ("7", "clubs"),
                ("5", "spades"),
            ],
            [
                ("J", "hearts"),
                ("J", "spades"),
                ("10", "clubs"),
                ("10", "diamonds"),
                ("3", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("Q", "hearts"),
                ("J", "spades"),
                ("J", "clubs"),
                ("2", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "Two Pair")

    def test_one_pair(self):
        """
        Test case that asserts that the classify method returns 'One Pair'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("9", "hearts"),
                ("7", "diamonds"),
                ("4", "clubs"),
                ("5", "spades"),
            ],
            [
                ("J", "hearts"),
                ("J", "spades"),
                ("10", "clubs"),
                ("6", "diamonds"),
                ("3", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("Q", "hearts"),
                ("J", "spades"),
                ("3", "clubs"),
                ("4", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "One Pair")

    def test_high_card(self):
        """
        Test case that asserts that the classify method returns 'High Card'
        when provided with a list of cards that make a full house hand.
        """
        test_cases = [
            [
                ("9", "spades"),
                ("5", "hearts"),
                ("7", "diamonds"),
                ("4", "clubs"),
                ("3", "spades"),
            ],
            [
                ("J", "hearts"),
                ("10", "spades"),
                ("8", "clubs"),
                ("6", "diamonds"),
                ("2", "hearts"),
            ],
            [
                ("Q", "diamonds"),
                ("K", "hearts"),
                ("J", "hearts"),
                ("8", "clubs"),
                ("2", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "High Card")

    def test_string_representation(self):
        """
        Test case that asserts that the __str__ method of the PokerHand class
        returns the correct string representation of the cards in the hand.
        """
        test_cases = [
            [
                ("A", "spades"),
                ("K", "hearts"),
                ("Q", "diamonds"),
                ("J", "clubs"),
                ("10", "spades"),
                "A spades K hearts Q diamonds J clubs 10 spades",
            ],
            [
                ("5", "hearts"),
                ("9", "diamonds"),
                ("2", "spades"),
                ("6", "clubs"),
                ("10", "hearts"),
                "5 hearts 9 diamonds 2 spades 6 clubs 10 hearts",
            ],
            [
                ("Q", "diamonds"),
                ("J", "hearts"),
                ("10", "spades"),
                ("9", "clubs"),
                ("8", "diamonds"),
                "Q diamonds J hearts 10 spades 9 clubs 8 diamonds",
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards[0:5])
                self.assertEqual(str(hand), cards[5])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokerHand)
    unittest.TextTestRunner(verbosity=2).run(suite)
