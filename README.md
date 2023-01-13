# PokerHand Class

The PokerHand class is a Python class that can be used to classify a poker hand into one of the following categories:

- 'Royal Flush'
- 'Straight Flush'
- 'Four of a Kind'
- 'Full House'
- 'Flush'
- 'Straight'
- 'Three of a Kind'
- 'Two Pair'
- 'One Pair'
- 'High Card'

## Installation

To use the PokerHand class, you'll need to have Python installed on your machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Usage

To use the PokerHand class, you'll first need to import it:

```python
from PokerHand import PokerHand
```

Then you can create a new instance of the class and classify a poker hand by calling the classify() method on an instance of the class, passing in a list of cards represented as tuples of rank and suit.

```python
cards = [("A", "C"), ("K", "C"), ("Q", "C"), ("J", "C"), ("T", "C")]
poker_hand = PokerHand(cards)
print(poker_hand.classify()) # "Royal Flush"
print(poker_hand) # "AC KC QC JC TC"
```

## Class Methods

### `__init__(cards: List[Tuple[str, str]])`

Initializes a PokerHand instance with a list of cards represented as tuples of rank and suit.

The **init** method in the PokerHand class is used to initialize an instance of the PokerHand class when it is created. It is called automatically when a new instance of the class is created and is used to set up the initial state of the object.

The method takes one argument, cards, which is a list of tuples representing the cards in the hand. Each tuple contains a string representing the rank of the card and a string representing the suit of the card.

The method assigns the cards argument to the self.cards attribute of the instance. It then uses a list comprehension to create a new list self.ranks which contains the integer value of the rank of each card, or the value in the RANK_MAP dictionary if the rank is not a digit. The list comprehension sorts the ranks in descending order.

The method then creates another list comprehension, self.suits which contains the suits of each card.

It then checks if the length of the set of suits is 1, if it is, then it assigns the value True to self.is_flush attribute. If not, it assigns False. It also checks if the max(self.ranks) - min(self.ranks) == 4) and the length of set(self.ranks) == 5, if it is true, it assigns the value True to self.is_straight attribute, otherwise False.

In summary, the **init** method sets up the initial state of the PokerHand instance by assigning the cards argument to the self.cards attribute, creating the self.ranks and self.suits attributes, and setting the self.is_flush and self.is_straight attributes based on the cards in the hand.

### `classify() -> str`

Classifies the PokerHand instance into one of the following categories: 'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card'

The classify method in the PokerHand class is used to classify a hand of poker based on the cards it contains. The method first checks if the hand is a "Royal Flush" by checking if the minimum rank is 10, the hand is a flush, and the hand is a straight. If this is true, it returns the string "Royal Flush". If not, it then checks if the hand is a "Straight Flush" by checking if the hand is both a flush and a straight. If this is true, it returns the string "Straight Flush".

The method then uses the collections.Counter method to check the number of occurrences of each rank in the hand and uses this information to determine if the hand is a "Four of a Kind", "Full House", "Three of a Kind", "Two Pair", "One Pair", or "High Card".

If the most common rank has a count of 4, the method returns "Four of a Kind". If the most common rank has a count of 3 and the second most common rank has a count of 2, the method returns "Full House". If the most common rank has a count of 3 and the second most common rank does not have a count of 2, the method returns "Three of a Kind".

If the hand is a flush and not a straight, the method returns "Flush". If the hand is a straight and not a flush, the method returns "Straight". If the most common rank has a count of 2 and the second most common rank also has a count of 2, the method returns "Two Pair". If the most common rank has a count of 2 and the second most common rank does not have a count of 2, the method returns "One Pair".

If none of these conditions are met, the method returns "High Card".

### `__str__() -> str`

Returns the cards in the hand as a string.

The **str** method in the PokerHand class is used to provide a string representation of the hand. This method is called when the print() function is called on an instance of the PokerHand class.

The method first creates a list comprehension that iterates over the self.cards attribute of the PokerHand instance and formats each card as a string in the format "RankSuit" (e.g. "AH" for an Ace of Hearts).

It then uses the join() method to concatenate all of the formatted card strings in the list comprehension with a space as the separator. Finally, the method returns the concatenated string.

In summary, this method converts the cards attribute of the class into a string representation of the card in the format "RankSuit" with space as separator and return that string representation.

## Contributing

If you have any suggestions or find any bugs, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to OpenAI for providing the AI model that assisted in writing the documentation.
