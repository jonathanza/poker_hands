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
# Run unit tests
uv run python -m unittest unit_tests.py

# Run tests with coverage
uv run coverage run -m unittest unit_tests.py

# Generate coverage report
uv run coverage report

# Generate coverage XML report (for Codacy)
uv run coverage xml -o coverage.xml

# Check coverage threshold (90% minimum)
uv run coverage report --fail-under=90
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
