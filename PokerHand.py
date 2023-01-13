import collections


class PokerHand:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = [r for r, s in cards]
        self.ranks.sort(reverse=True)
        self.suits = [s for r, s in cards]
        self.is_flush = len(set(self.suits)) == 1
        self.is_straight = (max(self.ranks) - min(self.ranks) == 4) and len(
            set(self.ranks)
        ) == 5

    def classify(self):
        if self.is_flush and self.is_straight:
            if min(self.ranks) == 10:
                return "Royal Flush"
            else:
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
