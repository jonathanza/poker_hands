# Poker Hands Classifier 🃏

[![CI](https://github.com/jonathanza/poker_hands/actions/workflows/ci.yml/badge.svg)](https://github.com/jonathanza/poker_hands/actions/workflows/ci.yml) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ec8a9ce37ca748f9b4226da7dd5efff9)](https://www.codacy.com/gh/jonathanza/poker_hands/dashboard?utm_source=github.com&utm_medium=referral&utm_content=jonathanza/poker_hands&utm_campaign=Badge_Grade) [![Codacy Badge](https://app.codacy.com/project/badge/Coverage/ec8a9ce37ca748f9b4226da7dd5efff9)](https://www.codacy.com/gh/jonathanza/poker_hands/dashboard?utm_source=github.com&utm_medium=referral&utm_content=jonathanza/poker_hands&utm_campaign=Badge_Coverage)

A modern, production-ready Python library for classifying poker hands with **three interfaces**: a type-safe library, an interactive CLI, and a REST API.

## ✨ Features

- 🎯 **Type-Safe Core Library** - Pydantic models with automatic validation
- 🌐 **FastAPI REST API** - Production-ready with OpenAPI documentation
- 💻 **Interactive CLI** - Rich terminal interface with Unicode card symbols (♥ ♦ ♣ ♠)
- 🔒 **100% Test Coverage** - 85 tests including property-based testing
- ⚡ **Modern Tooling** - Built with `uv` and `ruff` for maximum performance
- 📦 **Zero Breaking Changes** - Backward-compatible with v1.x API

## 🚀 Quick Start

### Installation

```bash
# Install with uv (recommended)
uv sync --extra api

# Or with pip
pip install -e .
```

### Usage Examples

#### 1. REST API (FastAPI)

Start the API server:
```bash
uvicorn api.main:app --reload
```

Access interactive documentation at **http://localhost:8000/api/docs**

**Classify a hand:**
```bash
curl -X POST "http://localhost:8000/api/v1/classify" \
  -H "Content-Type: application/json" \
  -d '{"cards": [["A", "H"], ["K", "H"], ["Q", "H"], ["J", "H"], ["T", "H"]]}'
```

**Response:**
```json
{
  "hand_type": "Royal Flush",
  "strength": 10,
  "cards": ["A♥", "K♥", "Q♥", "J♥", "T♥"]
}
```

#### 2. Core Library (Recommended)

```python
from core import Card, Hand, HandClassifier

# Create cards with automatic validation
cards = [
    Card(rank="A", suit="H"),
    Card(rank="K", suit="H"),
    Card(rank="Q", suit="H"),
    Card(rank="J", suit="H"),
    Card(rank="T", suit="H"),
]

# Create hand (validates duplicates automatically)
hand = Hand(cards=cards)

# Classify
hand_type = HandClassifier.classify(hand)
print(hand_type)  # HandType.ROYAL_FLUSH
print(hand)       # A♥ K♥ Q♥ J♥ T♥
```

#### 3. Legacy API (Backward Compatible)

```python
from poker_hand import PokerHand

# Old v1.x API still works
hand = PokerHand([("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")])
print(hand.classify())  # "Royal Flush"
```

#### 4. Interactive CLI

```bash
uv run python poker_hand_cli.py
```

Or use the enhanced CLI:
```bash
uv run python -m cli.cli
```

## 🎴 Hand Classifications

The library classifies hands into 10 categories (from strongest to weakest):

| Rank | Hand Type | Example |
|------|-----------|---------|
| 10 | Royal Flush | A♥ K♥ Q♥ J♥ T♥ |
| 9 | Straight Flush | 9♠ 8♠ 7♠ 6♠ 5♠ |
| 8 | Four of a Kind | A♦ A♥ A♠ A♣ K♥ |
| 7 | Full House | K♠ K♥ K♦ Q♣ Q♠ |
| 6 | Flush | A♥ J♥ 8♥ 5♥ 3♥ |
| 5 | Straight | 9♥ 8♦ 7♣ 6♠ 5♥ |
| 4 | Three of a Kind | Q♦ Q♥ Q♠ 7♣ 4♠ |
| 3 | Two Pair | J♥ J♦ 8♣ 8♠ 3♥ |
| 2 | One Pair | T♠ T♥ 9♦ 5♣ 2♠ |
| 1 | High Card | A♦ K♥ Q♣ J♠ 9♥ |

## 📡 API Endpoints

The FastAPI server provides the following endpoints:

### Classify Single Hand
```
POST /api/v1/classify
```
Classify a single 5-card poker hand.

**Request:**
```json
{
  "cards": [["A", "H"], ["K", "H"], ["Q", "H"], ["J", "H"], ["T", "H"]]
}
```

**Response:**
```json
{
  "hand_type": "Royal Flush",
  "strength": 10,
  "cards": ["A♥", "K♥", "Q♥", "J♥", "T♥"]
}
```

### Batch Classify
```
POST /api/v1/classify/batch
```
Classify up to 100 hands in a single request.

**Request:**
```json
[
  {"cards": [["A", "H"], ["K", "H"], ["Q", "H"], ["J", "H"], ["T", "H"]]},
  {"cards": [["2", "S"], ["3", "D"], ["4", "C"], ["5", "H"], ["7", "S"]]}
]
```

### Compare Hands
```
POST /api/v1/compare
```
Compare two hands and determine the winner.

**Request:**
```json
{
  "hand1": [["A", "H"], ["K", "H"], ["Q", "H"], ["J", "H"], ["T", "H"]],
  "hand2": [["2", "S"], ["3", "D"], ["4", "C"], ["5", "H"], ["7", "S"]]
}
```

**Response:**
```json
{
  "winner": "hand1",
  "hand1": {"hand_type": "Royal Flush", "strength": 10, "cards": ["A♥", "K♥", "Q♥", "J♥", "T♥"]},
  "hand2": {"hand_type": "High Card", "strength": 1, "cards": ["2♠", "3♦", "4♣", "5♥", "7♠"]}
}
```

### Health Check
```
GET /health
```
Check API health and version.

**Response:**
```json
{
  "status": "healthy",
  "version": "3.0.0"
}
```

## 🏗️ Architecture

```
poker_hands/
├── api/                   # FastAPI REST API
│   ├── main.py           # FastAPI application
│   ├── routes/           # Endpoint handlers
│   │   ├── hands.py      # Classification endpoints
│   │   └── health.py     # Health check
│   └── schemas/          # Pydantic request/response models
│       ├── requests.py
│       └── responses.py
├── core/                  # Type-safe core library
│   ├── enums.py          # Rank, Suit, HandType enums
│   ├── models.py         # Pydantic Card and Hand models
│   ├── classifier.py     # Hand classification logic
│   └── validators.py     # Input validation
├── cli/                   # CLI interfaces
│   └── cli.py            # Enhanced interactive CLI
├── tests/                 # Comprehensive test suite
│   ├── test_api.py       # API tests (14 tests)
│   ├── test_core.py      # Core library tests (37 tests)
│   └── test_properties.py # Property-based tests (23 tests)
├── poker_hand.py          # Backward-compatible wrapper
├── poker_hand_cli.py      # Legacy CLI
└── unit_tests.py          # Legacy tests (11 tests)
```

## 🧪 Testing

The project has **85 comprehensive tests** with multiple testing strategies:

```bash
# Run all tests
uv run python -m unittest discover -s tests -p "test_*.py"
uv run python -m unittest unit_tests.py

# Run specific test suites
uv run python -m unittest tests.test_api          # API tests
uv run python -m unittest tests.test_core         # Core library tests
uv run python -m unittest tests.test_properties   # Property-based tests
uv run python -m unittest unit_tests              # Legacy tests

# Run with coverage
uv run --with coverage coverage run --source=core,api -m unittest discover -s tests
uv run --with coverage coverage report
```

**Test Coverage:**
- Core library: 91%
- API: 100%
- Overall: 94%

## 🛠️ Development

### Setup

```bash
# Install uv (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --dev --extra api
```

### Linting & Formatting

```bash
# Format code
uv run ruff format .

# Lint code
uv run ruff check .

# Auto-fix issues
uv run ruff check --fix .
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

## 🎯 Card Notation

Cards are represented as tuples of `(rank, suit)`:

### Ranks
- Numbers: `"2"`, `"3"`, `"4"`, `"5"`, `"6"`, `"7"`, `"8"`, `"9"`
- Ten: `"10"` or `"T"`
- Face cards: `"J"` (Jack), `"Q"` (Queen), `"K"` (King), `"A"` (Ace)
- Case-insensitive: `"ace"`, `"Ace"`, `"ACE"` all work

### Suits
- `"H"` - Hearts (♥)
- `"D"` - Diamonds (♦)
- `"C"` - Clubs (♣)
- `"S"` - Spades (♠)
- Full names also work: `"hearts"`, `"diamonds"`, etc.

**Example:**
```python
[("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")]
```

## 📚 Documentation

- **API Documentation**: http://localhost:8000/api/docs (when server is running)
- **ReDoc**: http://localhost:8000/api/redoc
- **OpenAPI Spec**: http://localhost:8000/api/openapi.json
- **Development Guide**: See [CLAUDE.md](./CLAUDE.md)
- **Project Roadmap**: See [ROADMAP.md](./ROADMAP.md)
- **Changelog**: See [CHANGELOG.md](./CHANGELOG.md)

## 🔄 Version History

### v3.0.0 (Current) - FastAPI REST API
- ✨ Production-ready REST API with OpenAPI documentation
- 🚀 Async endpoints for better performance
- 📦 Batch processing support (up to 100 hands)
- 🔍 Hand comparison endpoint
- 🧪 14 comprehensive API tests

### v2.1.0 - Core Library Refactoring
- 🏗️ Modular architecture with `core/` package
- 🔒 Type-safe Pydantic models
- ✅ Property-based testing with Hypothesis
- 💎 Enhanced CLI with rich formatting
- 🎯 91% test coverage

### v2.0.0-beta.2 - Modern Tooling
- ⚡ Migrated from pipenv to uv (10-100x faster)
- 🔧 Replaced black/isort/pylint with ruff
- 🤖 GitHub Actions CI/CD
- 📝 Comprehensive documentation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`uv run python -m unittest discover`)
4. Commit your changes (`git commit -m 'feat: add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) for the REST API
- [Pydantic](https://pydantic.dev/) for data validation
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- [Hypothesis](https://hypothesis.readthedocs.io/) for property-based testing
- [uv](https://github.com/astral-sh/uv) for blazing-fast package management
- [Ruff](https://github.com/astral-sh/ruff) for ultra-fast linting

## 📊 Project Status

**Current Phase**: ✅ Phase 5 Complete (v3.0.0)

**Coming Next**:
- Phase 6: Web interface with React/Vue
- Phase 7: Terminal UI with Textual
- Phase 8: Enhanced documentation
- Phase 9: Advanced features (game simulation, odds calculation)

See [ROADMAP.md](./ROADMAP.md) for the complete vision.

---

Made with ❤️ and modern Python tooling
