# PokerHand Class

The `PokerHand` class is a Python class that can be used to classify a poker hand into one of the following categories:

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

To use the `PokerHand` class, you'll need to have Python installed on your machine. You can download the latest version of Python from the official website: https://www.python.org/downloads/

## Usage

To use the `PokerHand` class, you'll first need to import it:

```python
from PokerHand import PokerHand
```

Then you can create a new instance of the class and classify a poker hand by calling the classify() method on an instance of the class, passing in a list of cards represented as tuples of rank and suit.

```python
cards = [("A", "Clubs"), ("K", "Clubs"), ("Q", "Clubs"), ("J", "Clubs"), ("T", "Clubs")]
poker_hand = PokerHand(cards)
print(poker_hand.classify()) # "Royal Flush"
print(poker_hand) # "A Clubs K Clubs Q Clubs J Clubs T Clubs"
```

## Class Methods

### PokerHand

#### `__init__(cards: List[Tuple[str, str]])`

Initializes a `PokerHand` instance with a list of cards represented as tuples of rank and suit.

The `__init__` method of the `PokerHand` class initializes an instance of the class with a list of cards represented as tuples of rank and suit. This method performs the following steps:

- It sets `self.cards` as the input list of cards represented as tuples of rank and suit.
- It creates a list `self.ranks` by converting the rank of each card to an integer if it is a digit, otherwise it uses the value of the corresponding enumeration defined in the `Rank` class.
- It sorts the `self.ranks` list in descending order.
- It creates a list `self.suits` by extracting the suit of each card.
- It sets `self.is_flush` as `True` if all the suits in `self.suits` are the same, otherwise `False`.
- It sets `self.is_straight` as `True` if the difference between the maximum and minimum rank in `self.ranks` is 4 and the length of the set of `self.ranks` is 5. It sets `self.is_straight` as `False` otherwise.

The above attributes and steps performed during the `__init__` method will be used to classify the hand of poker in the `classify` method.

#### `classify() -> str`

Classifies the `PokerHand` instance into one of the following categories: 'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card'

The classify method classifies the `PokerHand` instance into one of the following categories:

- It creates a counter object of the ranks of the hand using `collections.Counter(self.ranks)`
- It checks if the hand is both a flush and a straight, if so it checks if the minimum rank is 10, if so it returns "Royal Flush", otherwise it returns "Straight Flush"
- It checks if the most common rank in the hand has a count of 4 using `counter.most_common(1)[0][1] == 4`, if so it returns "Four of a Kind"
- It checks if the most common rank in the hand has a count of 3, if so it checks if the second most common rank has a count of 2, if so it returns "Full House", otherwise it returns "Three of a Kind"
- If the previous conditions are not met, it checks if the hand is a flush, if so it returns "Flush"
- If the previous conditions are not met, it checks if the hand is a straight, if so it returns "Straight"
- If the previous conditions are not met, it checks if the most common rank in the hand has a count of 2, if so it checks if the second most common rank has a count of 2, if so it returns "Two Pair", otherwise it returns "One Pair"
- If the previous conditions are not met, it returns "High Card"

Note: The method uses the attributes of the class to check for certain conditions such as `self.is_flush`, `self.is_straight` and `self.ranks`.

#### `__str__() -> str`

Returns the cards in the hand as a string.

The `__str__` method of the `PokerHand` class returns a string representation of the cards in the hand. This method performs the following steps:

- It uses a list comprehension to create a list of strings, where each string is a combination of the rank and suit of a card in the format of "rank suit".
- It uses the `join` method to join the list of strings created in step 1 with a space separator, creating a single string containing all the cards in the hand.
- It returns this final string.

This method allows to represent the cards in the hand in a human readable format.

## Contributing

If you have any suggestions or find any bugs, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to OpenAI for providing the AI model that assisted in writing the documentation.
