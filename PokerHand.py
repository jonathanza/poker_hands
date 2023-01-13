import collections
from typing import List, Tuple


class PokerHand:
    def __init__(self, cards: List[Tuple[str, str]]):
        self.cards: List[Tuple[str, str]] = cards
        self.ranks: List[int] = [
            int(r) if r.isdigit() else {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}[r]
            for r, s in cards
        ]
        self.ranks.sort(reverse=True)
        self.suits: List[str] = [s for r, s in cards]
        self.is_flush: bool = len(set(self.suits)) == 1
        self.is_straight: bool = (max(self.ranks) - min(self.ranks) == 4) and len(
            set(self.ranks)
        ) == 5

    def classify(self) -> str:
        if min(self.ranks) == 10 and self.is_flush and self.is_straight:
            return "Royal Flush"
        elif self.is_flush and self.is_straight:
            return "Straight Flush"
        elif collections.Counter(self.ranks).most_common(1)[0][1] == 4:
            return "Four of a Kind"
        elif collections.Counter(self.ranks).most_common(2)[0][1] == 3:
            if collections.Counter(self.ranks).most_common(2)[1][1] == 2:
                return "Full House"
            else:
                return "Three of a Kind"
        elif self.is_flush:
            return "Flush"
        elif self.is_straight:
            return "Straight"
        elif collections.Counter(self.ranks).most_common(2)[0][1] == 2:
            if collections.Counter(self.ranks).most_common(2)[1][1] == 2:
                return "Two Pair"
            else:
                return "One Pair"
        else:
            return "High Card"


cards = [
    ("A", "spades"),
    ("K", "spades"),
    ("Q", "spades"),
    ("J", "spades"),
    ("10", "spades"),
]
hand = PokerHand(cards)
print(hand.classify())  # Output: "Royal Flush"
