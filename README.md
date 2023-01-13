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

```python3
cards = [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]
hand = PokerHand(cards)
print(hand.classify())  # "Royal Flush"
```

## Class Methods

### `__init__(cards: List[Tuple[str, str]])`

Initializes a PokerHand instance with a list of cards represented as tuples of rank and suit.

### `classify() -> str`

Classifies the PokerHand instance into one of the following categories:
'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind',
'Two Pair', 'One Pair', 'High Card'

## Contributing

If you have any suggestions or find any bugs, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to OpenAI for providing the AI model that assisted in writing the documentation.
