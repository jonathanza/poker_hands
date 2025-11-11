# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python poker hand classifier that can classify poker hands into categories (Royal Flush, Straight Flush, Four of a Kind, Full House, Flush, Straight, Three of a Kind, Two Pair, One Pair, High Card). The project includes both a programmatic API (`PokerHand` class) and a CLI interface.

## Development Commands

### Environment Setup

```bash
# Install uv (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh
# Or via pip: pip install uv

# Install dependencies (creates .venv automatically)
uv sync --dev
```

### Running Tests

```bash
# Run all tests (legacy + new)
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python -m unittest unit_tests.py

# Run specific test suites
uv run python -m unittest tests.test_core        # Core library tests
uv run python -m unittest tests.test_properties  # Property-based tests (Hypothesis)
uv run python -m unittest unit_tests.py          # Legacy compatibility tests

# Run tests with coverage (core library)
uv run --with coverage coverage run --source=core -m unittest tests.test_core
uv run --with coverage coverage report

# Check coverage threshold (90% minimum for core)
uv run --with coverage coverage report --fail-under=90
```

### Linting & Formatting

```bash
# Format code with ruff
uv run ruff format *.py

# Lint and auto-fix with ruff
uv run ruff check --fix *.py

# Lint only (no fixes)
uv run ruff check *.py

# Combined workflow (format + lint)
uv run ruff format *.py && uv run ruff check --fix *.py
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks (one-time setup)
pip install pre-commit
pre-commit install

# Run hooks manually
pre-commit run --all-files
```

### Running the CLI

```bash
uv run python poker_hand_cli.py
```

### Dependency Management

```bash
# Add a new dependency
uv add <package>

# Add a development dependency
uv add --dev <package>

# Remove a dependency
uv remove <package>

# Update dependencies
uv lock --upgrade

# Show installed packages
uv pip list
```

## Code Architecture

### Project Structure (v2.1.0+)

```
poker_hands/
├── core/                  # Core library (Phase 4 refactoring)
│   ├── __init__.py       # Public API exports
│   ├── enums.py          # Rank, Suit, HandType enums
│   ├── models.py         # Pydantic Card and Hand models
│   ├── classifier.py     # HandClassifier logic
│   └── validators.py     # Input validation helpers
├── cli/                   # CLI interface
│   ├── __init__.py
│   └── cli.py            # Enhanced interactive CLI
├── tests/                 # Comprehensive test suite
│   ├── __init__.py
│   ├── test_core.py      # Core library tests (37 tests)
│   └── test_properties.py # Hypothesis property tests (23 tests)
├── poker_hand.py          # Backward-compatible wrapper
├── poker_hand_cli.py      # Legacy CLI (maintained)
├── poker_hand_legacy.py   # Original implementation (backup)
└── unit_tests.py          # Legacy tests (11 tests, still passing)
```

### Core Components

#### New Core Library (`core/`)

- **`core/enums.py`**: Type-safe enumerations
  - `Rank` (IntEnum): Card ranks 2-14 with comparison support
  - `Suit` (Enum): H, D, C, S with full name support
  - `HandType` (IntEnum): Hand classifications 1-10 (strength-ordered)
  - `from_string()` methods for flexible input parsing

- **`core/models.py`**: Validated Pydantic models
  - `Card`: Immutable card with automatic rank/suit validation
  - `Hand`: 5-card hand with duplicate detection
  - Properties: `ranks`, `suits`, `is_flush`, `is_straight`
  - Unicode suit symbols (♥ ♦ ♣ ♠) in string representation

- **`core/classifier.py`**: Hand classification engine
  - `HandClassifier.classify(hand)`: Returns HandType enum
  - Uses pattern matching with Counter for efficiency
  - Fully type-hinted for static analysis

- **`core/validators.py`**: Input validation utilities
  - `is_valid_rank()`, `is_valid_suit()`, `is_valid_card_tuple()`
  - `has_duplicates()` for duplicate detection

#### Backward Compatibility Layer

- **`poker_hand.py`**: Wrapper maintaining legacy API
  - Same interface as v1.x (tuples input, string output)
  - Internally uses new core library
  - All legacy tests pass without modification

- **`poker_hand_cli.py`**: Original CLI (still functional)

#### New CLI

- **`cli/cli.py`**: Enhanced interactive experience
  - Rich formatting with colors and panels
  - Better error messages and input validation
  - Uses Pydantic models directly

### Usage Examples

#### New Core API (Recommended)
```python
from core import Card, Hand, HandClassifier

# Create cards with validation
cards = [Card(rank="A", suit="H") for ...]
hand = Hand(cards=cards)

# Classify
hand_type = HandClassifier.classify(hand)
print(hand_type)  # HandType.ROYAL_FLUSH
```

#### Legacy API (Backward Compatible)
```python
from poker_hand import PokerHand

# Old API still works
hand = PokerHand([("A", "H"), ("K", "H"), ...])
print(hand.classify())  # "Royal Flush"
```

### Card Representation

Cards are represented as tuples of `(rank, suit)`:
- Ranks: "2"-"9" (digits), "T"/"10", "J"/"Jack", "Q"/"Queen", "K"/"King", "A"/"Ace" (case-insensitive)
- Suits: Single character strings ("H", "D", "S", "C")

Example: `[("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]`

## Test Coverage Requirements

- Minimum 80% coverage per file
- Minimum 90% coverage overall

Coverage configuration in `pyproject.toml` (`[tool.coverage]` section) includes only `poker_*.py` files and excludes `__init__.py`, tests, and venv directories.

## Tooling

This project uses modern Python tooling:
- **uv**: Fast Python package installer and resolver (replaces pipenv)
- **ruff**: Extremely fast Python linter and formatter (replaces black, isort, pylint)
- **pre-commit**: Git hooks for automatic code quality checks
- **coverage**: Code coverage measurement
- **GitHub Actions**: CI/CD for automated testing

See [ROADMAP.md](./ROADMAP.md) for the project vision and future plans.
