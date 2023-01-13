import unittest
from PokerHand import PokerHand


class TestPokerHand(unittest.TestCase):
    def test_royal_flush(self):
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
                ("8", "clubs"),
                ("2", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "One Pair")

    def test_high_card(self):
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
                ("J", "spades"),
                ("8", "clubs"),
                ("2", "diamonds"),
            ],
        ]
        for i, cards in enumerate(test_cases):
            with self.subTest(testcase=i):
                hand = PokerHand(cards)
                self.assertEqual(hand.classify(), "High Card")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPokerHand)
    unittest.TextTestRunner(verbosity=2).run(suite)
