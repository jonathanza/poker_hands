import sys
from typing import List, Tuple

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from poker_hand import PokerHand

VALID_RANKS = {
    "ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "jack",
    "queen",
    "king",
}
VALID_SUITS = {"hearts", "diamonds", "clubs", "spades"}

console = Console()


def get_cards():
    cards = []
    while len(cards) < 5:
        try:
            card = tuple(
                input("Enter a card in the format 'rank suit': ").lower().split()
            )
            if len(card) != 2:
                raise ValueError(
                    "Invalid input. Please enter a card in the format 'rank suit'."
                )
            if card[0] not in VALID_RANKS:
                raise ValueError(f"Invalid rank value. Valid values are: {VALID_RANKS}")
            if card[1] not in VALID_SUITS:
                raise ValueError(f"Invalid suit value. Valid values are: {VALID_SUITS}")
            cards.append(card)
        except ValueError as e:
            console.print(e)
    return cards


def main():
    cards = get_cards()
    hand = PokerHand(cards)
    classification = hand.classify()
    console.print(f"Hand: {hand}\nClassification: {classification}")


if __name__ == "__main__":
    main()
