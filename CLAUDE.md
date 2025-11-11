# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python poker hand classifier that can classify poker hands into categories (Royal Flush, Straight Flush, Four of a Kind, Full House, Flush, Straight, Three of a Kind, Two Pair, One Pair, High Card). The project includes both a programmatic API (`PokerHand` class) and a CLI interface.

## Development Commands

### Environment Setup

```bash
# Initialize Python virtual environment with pipenv
pipenv --python /usr/bin/python3
pipenv install --skip-lock --dev --pre
pipenv shell
```

### Running Tests

```bash
# Run unit tests
python -m unittest unit_tests.py

# Run tests with coverage
coverage run -m unittest unit_tests.py

# Generate coverage XML report (for Codacy)
coverage xml -o coverage.xml
```

### Linting

```bash
# Format code with Black
black -v *.py

# Sort imports with isort
isort *.py

# Lint with Pylint
pylint *.py
```

### Running the CLI

```bash
python3 poker_hand_cli.py
```

## Code Architecture

### Core Components

- **`poker_hand.py`**: Contains the main `PokerHand` class and `Rank` enum
  - `Rank` enum maps card ranks (T, J, Q, K, A) to integer values (10-14)
  - `PokerHand` class takes a list of card tuples `[(rank, suit), ...]`
  - On initialization, converts ranks to integers, sorts them, checks for flush/straight
  - `classify()` method uses a conditions dictionary to match hand patterns via `collections.Counter`

- **`poker_hand_cli.py`**: Interactive CLI for inputting and classifying hands (requires `rich` library)

- **`unit_tests.py`**: Test suite for the `PokerHand` class

### Card Representation

Cards are represented as tuples of `(rank, suit)`:
- Ranks: "2"-"9" (digits), "T"/"10", "J"/"Jack", "Q"/"Queen", "K"/"King", "A"/"Ace" (case-insensitive)
- Suits: Single character strings ("H", "D", "S", "C")

Example: `[("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]`

## Test Coverage Requirements

Per global CLAUDE.md configuration:
- Minimum 80% coverage per file
- Minimum 90% coverage overall

Coverage configuration in `.coveragerc` includes only `poker_*.py` files and excludes `__init__.py`, tests, and venv directories.
