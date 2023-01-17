# PokerHand Class

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/53ae48d1931949baa8e1dd1855ea364e)](https://app.codacy.com/gh/jonathanza/poker_hands?utm_source=github.com&utm_medium=referral&utm_content=jonathanza/poker_hands&utm_campaign=Badge_Grade_Settings)

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

### Programmatic

This module defines a `PokerHand` class that represents a hand of poker cards and various methods to classify and represent the cards in the hand.

To use the module, you need to first import it. Then you can create an instance of the `PokerHand` class by providing a list of cards represented as tuples of rank and suit.

For example:

```python
from poker import PokerHand
cards = [("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]
hand = PokerHand(cards)
```

You can use the `classify()` method on the hand object to classify the hand into one of the following categories: 'Royal Flush', 'Straight Flush', 'Four of a Kind', 'Full House', 'Flush', 'Straight', 'Three of a Kind', 'Two Pair', 'One Pair', 'High Card'

For example:

```python
print(hand.classify())
```

You can also use the `__str__()` method to get the string representation of the cards in the hand:

```python
print(hand)
```

You can also access the following attributes of the hand object:

- `cards`: a list of cards represented as tuples of rank and suit
- `ranks`: a list of integers representing the ranks of the cards
- `suits`: a list of strings representing the suits of the cards
- `is_flush`: a boolean indicating if the hand is a flush
- `is_straight`: a boolean indicating if the hand is a straight

For example:

```python
print(hand.cards)
print(hand.ranks)
print(hand.suits)
print(hand.is_flush)
print(hand.is_straight)
```

Note that the cards are represented as a tuple of rank and suit, where the rank is represented as a string (with possible values T, J, Q, K, A) and the suit is represented as a single character string (with possible values H, D, S, C).

### CLI

This script is a command-line interface (CLI) that allows you to classify a poker hand by inputting cards into the terminal.

To use the script, you will need to have python3 and the rich library installed in your system.

You can run the script by navigating to the directory where the script is located in your terminal and typing:

```bash
python3 poker_cli.py
```

The script will prompt you to enter 5 cards in the format "rank suit" (e.g. "ace hearts").
You can enter the cards one at a time and press enter after each card.
The script will check if the cards are valid, and if not will prompt you to enter the card again.

Once you have entered 5 valid cards, it will classify the hand and display the result on the console, including the string representation of the cards in the hand and the classification of the hand.

For example:

```bash
Enter a card in the format 'rank suit': ace hearts
Enter a card in the format 'rank suit': king hearts
Enter a card in the format 'rank suit': queen hearts
Enter a card in the format 'rank suit': jack hearts
Enter a card in the format 'rank suit': 10 hearts
Hand: Ace of Hearts King of Hearts Queen of Hearts Jack of Hearts 10 of Hearts
Classification: Royal Flush
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

Here is a step by step explanation of what the method does:

- The method starts by creating a `collections.Counter` object, `counter`, of the `self.ranks` attribute, which contains a list of integers representing the ranks of the cards in the hand.
- Next, a dictionary, `conditions`, is defined that maps a tuple of conditions to the corresponding hand classification.
- Then, the method uses a for loop to iterate over the items in the `conditions` dictionary. Each item is a tuple of conditions and a hand classification.
- In the for loop, the method uses the `all()` function to check if all the conditions in the tuple of the current item are met. If the conditions are met, the corresponding hand classification is returned by the method.
- If none of the conditions are met, the method return "High Card" as the default classification for any hand that does not match any other classification.
- This way, the method goes through all the items in the conditions dictionary, checks if all the conditions in the tuple are met and returns the corresponding hand classification.

#### `__str__() -> str`

Returns the cards in the hand as a string.

The `__str__` method of the `PokerHand` class returns a string representation of the cards in the hand. This method performs the following steps:

- It uses a list comprehension to create a list of strings, where each string is a combination of the rank and suit of a card in the format of "rank suit".
- It uses the `join` method to join the list of strings created in step 1 with a space separator, creating a single string containing all the cards in the hand.
- It returns this final string.

This method allows to represent the cards in the hand in a human readable format.

## Development Environment

### Initialise Python Virtual Environment

```bash
pipenv --python /usr/bin/python3
cd /srv/poker_hands/
rm -rf /srv/poker_hands/.venv
mkdir /srv/poker_hands/.venv
pipenv install --skip-lock --dev --pre
pipenv shell
```

### Lint Code

#### [Black](https://pypi.org/project/black/)

```bash
cd /srv/poker_hands/
pipenv shell
black -v *.py
```

#### [isort](https://pypi.org/project/isort/)

```bash
cd /srv/poker_hands/
pipenv shell
isort *.py
```

#### [Pylint](https://pypi.org/project/pylint/)

```bash
cd /srv/poker_hands/
pipenv shell
pylint *.py
```

## Contributing

If you have any suggestions or find any bugs, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Thanks to OpenAI for providing the AI model that assisted in writing the documentation.

## Meta

### GitHub Description

**Prompt**

```text
Suggest 10 short descriptions for the GitHub repo containing this code
```

**Response**

```text
A Python implementation of a Poker Hand classifier
Classify poker hands with this Python module
A poker hand classification tool written in Python
Classify and represent poker hands in Python
Python library for classifying and representing poker hands
A comprehensive Python poker hand classifier
Poker hand classification and representation in Python
Python implementation of poker hand classification and representation
A powerful tool for classifying poker hands using Python
Python module for classifying and representing poker hands with ease
```
