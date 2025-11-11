"""
Interactive CLI for poker hand classification using the core library.

Prompts user to input cards and classifies the resulting hand.
Uses Pydantic validation for robust input handling.
"""

from typing import List, Tuple

from pydantic import ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core import Card, Hand, HandClassifier, HandType, Rank, Suit
from core.validators import is_valid_rank, is_valid_suit

console: Console = Console()


def get_card_input(card_num: int) -> Tuple[str, str]:
    """
    Prompt user for a single card and validate it.

    Args:
        card_num: Card number (1-5) for display purposes

    Returns:
        Tuple of (rank, suit) strings

    Raises:
        ValueError: If input is invalid
    """
    while True:
        try:
            user_input = console.input(
                f"[bold cyan]Card {card_num}/5[/bold cyan] - "
                "Enter rank and suit (e.g., 'Ace Hearts' or 'A H'): "
            ).strip()

            parts = user_input.split()
            if len(parts) != 2:
                console.print(
                    "[bold red]Error:[/bold red] "
                    "Please enter both rank and suit separated by a space.",
                    style="red",
                )
                continue

            rank_str, suit_str = parts

            # Validate rank
            if not is_valid_rank(rank_str):
                console.print(
                    f"[bold red]Error:[/bold red] Invalid rank '{rank_str}'. "
                    f"Valid ranks: 2-10, J/Jack, Q/Queen, K/King, A/Ace",
                    style="red",
                )
                continue

            # Validate suit
            if not is_valid_suit(suit_str):
                console.print(
                    f"[bold red]Error:[/bold red] Invalid suit '{suit_str}'. "
                    f"Valid suits: H/Hearts, D/Diamonds, C/Clubs, S/Spades",
                    style="red",
                )
                continue

            # Normalize the input
            rank = Rank.from_string(rank_str)
            suit = Suit.from_string(suit_str)

            return (rank.name, suit.value)

        except (ValueError, KeyError) as error:
            console.print(f"[bold red]Error:[/bold red] {error}", style="red")


def get_cards() -> List[Tuple[str, str]]:
    """
    Prompt user to input 5 cards with validation.

    Returns:
        List of 5 (rank, suit) tuples
    """
    cards: List[Tuple[str, str]] = []
    entered_cards_display: List[str] = []

    console.print()
    console.print(
        Panel(
            "[bold]Enter 5 cards for your poker hand[/bold]\n"
            "Examples: 'A H', 'Ace Hearts', 'K S', 'King Spades'",
            title="Poker Hand Classifier",
            border_style="cyan",
        )
    )
    console.print()

    while len(cards) < 5:
        try:
            rank_str, suit_str = get_card_input(len(cards) + 1)

            # Create Card to validate (this will catch duplicates via Hand validator)
            card = Card(rank=rank_str, suit=suit_str)

            # Check for duplicates before adding
            if (rank_str, suit_str) in cards:
                console.print(
                    f"[bold red]Error:[/bold red] "
                    f"Card {card} already entered. Please enter a different card.",
                    style="red",
                )
                continue

            cards.append((rank_str, suit_str))
            entered_cards_display.append(str(card))

            # Show progress
            if len(cards) < 5:
                console.print(
                    f"[dim]Cards entered: {', '.join(entered_cards_display)}[/dim]\n"
                )

        except ValidationError as error:
            console.print(
                f"[bold red]Validation Error:[/bold red] {error}", style="red"
            )

    return cards


def display_result(hand: Hand, hand_type: HandType) -> None:
    """
    Display the classified hand in a nice format.

    Args:
        hand: The Hand object
        hand_type: The classification result
    """
    # Create a table for the cards
    table = Table(title="Your Hand", show_header=False, box=None)
    table.add_column("Cards", justify="center", style="bold cyan")

    card_display = " ".join(str(card) for card in hand.cards)
    table.add_row(card_display)

    # Map HandType to display names
    hand_names = {
        HandType.ROYAL_FLUSH: "Royal Flush",
        HandType.STRAIGHT_FLUSH: "Straight Flush",
        HandType.FOUR_OF_A_KIND: "Four of a Kind",
        HandType.FULL_HOUSE: "Full House",
        HandType.FLUSH: "Flush",
        HandType.STRAIGHT: "Straight",
        HandType.THREE_OF_A_KIND: "Three of a Kind",
        HandType.TWO_PAIR: "Two Pair",
        HandType.ONE_PAIR: "One Pair",
        HandType.HIGH_CARD: "High Card",
    }

    # Determine color based on hand strength
    strength = hand_type.value
    if strength >= 9:  # Royal Flush, Straight Flush
        color = "bold magenta"
    elif strength >= 7:  # Four of a Kind, Full House
        color = "bold yellow"
    elif strength >= 5:  # Flush, Straight
        color = "bold green"
    elif strength >= 3:  # Three of a Kind, Two Pair
        color = "bold cyan"
    else:  # One Pair, High Card
        color = "bold white"

    console.print()
    console.print(table)
    console.print()
    console.print(
        Panel(
            f"[{color}]{hand_names[hand_type]}[/{color}]",
            title="Classification",
            border_style=color.split()[1] if " " in color else color,
        )
    )


def main() -> None:
    """
    Main CLI entry point.

    Prompts for 5 cards, validates them, classifies the hand, and displays the result.
    """
    try:
        # Get cards from user
        cards_tuples = get_cards()

        # Create Card objects
        cards = [Card(rank=r, suit=s) for r, s in cards_tuples]

        # Create Hand (this validates no duplicates)
        hand = Hand(cards=cards)

        # Classify the hand
        hand_type = HandClassifier.classify(hand)

        # Display result
        display_result(hand, hand_type)

    except ValidationError as error:
        console.print(f"[bold red]Validation Error:[/bold red] {error}", style="red")
    except KeyboardInterrupt:
        console.print("\n[yellow]Goodbye![/yellow]")
    except Exception as error:
        console.print(f"[bold red]Unexpected Error:[/bold red] {error}", style="red")


if __name__ == "__main__":
    main()
