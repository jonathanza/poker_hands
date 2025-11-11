# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-11-11

### Added

#### Core Library Refactoring (Phase 4)
- **Modular architecture** with `core/` package
  - `core/enums.py`: Type-safe Rank, Suit, HandType enumerations
  - `core/models.py`: Pydantic models for Card and Hand with validation
  - `core/classifier.py`: HandClassifier for poker hand classification
  - `core/validators.py`: Input validation utility functions
- **Enhanced CLI** in `cli/cli.py` with rich formatting
  - Color-coded output based on hand strength
  - Better error messages and input validation
  - Unicode suit symbols (♥ ♦ ♣ ♠)
- **Comprehensive test suite** (71 total tests)
  - `tests/test_core.py`: 37 unit tests for core library (91% coverage)
  - `tests/test_properties.py`: 23 property-based tests using Hypothesis
  - Legacy `unit_tests.py`: 11 tests still passing (backward compatibility)
- **Type hints everywhere** for mypy strict mode compatibility
- **Property-based testing** with Hypothesis for robust validation

#### Developer Experience
- **Pydantic validation** for automatic input checking
  - Frozen models (immutable cards and hands)
  - Custom validators for ranks and suits
  - Duplicate card detection
- **Hypothesis integration** for property-based testing
  - Tests invariants across all possible inputs
  - Discovers edge cases automatically

### Changed

#### Architecture (NON-BREAKING)
- **Refactored core logic** into modular components
  - Separation of concerns: models, enums, logic, validation
  - Pydantic models replace manual validation
  - IntEnum for comparable types (Rank, HandType)
- **Backward-compatible wrapper** in `poker_hand.py`
  - Legacy API maintained for existing code
  - All existing tests pass without modification
  - Internally delegates to new core library

#### Code Quality
- **100% type hints** throughout codebase
- **91% test coverage** for core library
- **Immutable data structures** (Pydantic frozen models)
- **Better error messages** with Pydantic validation

#### Documentation
- **Updated CLAUDE.md** with new architecture
  - Core library structure documented
  - Usage examples for both new and legacy APIs
  - Updated test commands
- **Updated coverage configuration** in `pyproject.toml`
  - Source tracking for core/, cli/ modules
  - Proper omit patterns for test files

### Performance
- **Pydantic validation** provides fast input checking
- **No performance regression** in classification logic
- **Efficient immutable models** with frozen dataclasses

### Developer Impact
- **Non-breaking change**: Existing code continues to work via backward-compatible wrapper
- **New API available**: Developers can opt-in to core library for better type safety
- **Enhanced validation**: Pydantic catches errors earlier with better messages
- **Property-based tests**: Hypothesis ensures correctness across all inputs

### Migration Notes (Optional)
Developers can optionally migrate to the new core API for better type safety:

**Old (still supported)**:
```python
from poker_hand import PokerHand
hand = PokerHand([("A", "H"), ("K", "H"), ("Q", "H"), ("J", "H"), ("T", "H")])
print(hand.classify())  # "Royal Flush"
```

**New (recommended)**:
```python
from core import Card, Hand, HandClassifier
cards = [Card(rank=r, suit=s) for r, s in [("A", "H"), ...]]
hand = Hand(cards=cards)
print(HandClassifier.classify(hand))  # HandType.ROYAL_FLUSH
```

## [2.0.0-beta.2] - 2025-11-11

### Added
- **Project roadmap** (ROADMAP.md) documenting vision through Phase 9
  - FastAPI backend (v3.0.0)
  - Web interface (v3.1.0)
  - Terminal UI with Textual (v3.2.0)
  - Advanced features roadmap (v4.0.0+)
- **Updated TODO.md** with Phase 3 focus and migration guide
- **uv.lock** file for reproducible builds

### Changed

#### Dependency Management (BREAKING CHANGE)
- **Migrated from pipenv to uv** (10-100x faster)
  - Removed Pipfile and Pipfile.lock
  - All dependencies now managed via pyproject.toml
  - Lock file: uv.lock (committed for reproducibility)
  - Virtual environment: .venv (auto-created by uv)

#### CI/CD Updates
- **Updated GitHub Actions workflows** to use uv
  - Install uv via official installer script
  - Use `uv sync` for dependency installation
  - Use `uv run` for all command execution
  - Updated caching strategy for uv packages
  - Faster CI execution (seconds vs minutes)

#### Documentation
- **Updated CLAUDE.md** with uv workflow
  - New commands for dependency management
  - Updated testing and linting workflows
  - Added tooling overview section
- **Added placeholder dependency groups** in pyproject.toml
  - api: FastAPI, uvicorn, pydantic (Phase 5)
  - tui: textual, rich (Phase 7)

### Removed
- **Pipfile** and **Pipfile.lock** (replaced by uv.lock)
- Pipenv dependency and all pipenv commands

### Developer Impact
- **Breaking Change**: Must use uv instead of pipenv
  - Install: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Setup: `uv sync --dev` (replaces `pipenv install --dev`)
  - Run: `uv run <command>` (replaces `pipenv run <command>`)
- **Faster workflow**: 10-100x faster dependency installation
- **No shell activation needed**: Use `uv run` directly

### Migration Notes
Completed Phase 3 of modernization plan:
- ✅ Migrated to uv for dependency management
- ✅ Updated all CI/CD workflows
- ✅ Updated documentation
- ✅ Removed pipenv dependencies

## [2.0.0-beta.1] - 2025-11-11

### Added

#### CI/CD Infrastructure
- **Comprehensive GitHub Actions workflows** for automated testing and quality assurance
  - `ci.yml`: Multi-job workflow with linting, testing, and coverage reporting
  - `autoformat.yml`: Automatic code formatting on pull requests
- **Multi-version Python testing** across Python 3.10, 3.11, 3.12, and 3.13 (current supported versions)
- **Coverage enforcement** with 90% minimum threshold
- **CLI smoke tests** to validate basic functionality in CI
- **Codacy integration** for automated code quality and coverage reporting
- **CI status badge** to README.md for build status visibility

#### Developer Experience
- **Pre-commit hooks** configuration (`.pre-commit-config.yaml`)
  - Automatic code formatting with ruff
  - Common file checks (trailing whitespace, EOF, YAML validation, etc.)
- **Project metadata** in `pyproject.toml`
  - Centralized project configuration
  - Proper Python package metadata
  - Dependency management structure
- **Modernization roadmap** documented in `TODO.md`

#### Documentation
- **CHANGELOG.md** for tracking version history (this file)
- **Comprehensive PR workflow documentation** in CI configuration

### Changed

#### Tooling Modernization (BREAKING CHANGE)
- **Migrated from black + isort + pylint → ruff**
  - 10-100x faster linting and formatting
  - Single unified tool replaces three separate tools
  - Compatible with black/isort formatting standards
- **Centralized configuration** in `pyproject.toml`
  - Moved coverage configuration from `.coveragerc` to `pyproject.toml`
  - Ruff configuration (line-length: 88, target: py310)
  - Tool settings now in standard location

#### Python Version Support (BREAKING CHANGE)
- **Dropped support for Python 3.8 and 3.9** (both reached end-of-life)
  - Minimum Python version: 3.10
  - Supported versions: 3.10, 3.11, 3.12, 3.13
  - Aligns with active Python maintenance schedule
  - Ensures security updates and modern language features

#### Code Quality
- **Reformatted all Python files** to comply with ruff standards
  - Module-level docstrings wrapped to 88 characters
  - Consistent formatting across entire codebase
  - Added blank lines after module docstrings per PEP 8

#### Configuration Updates
- **Fixed Pipfile** for CI compatibility
  - Removed restrictive Python version constraint
  - Configured to use system Python in CI environments
  - Maintained pipenv support for existing workflows

### Fixed
- **Line length violations** in docstrings (E501)
  - `poker_hand.py`: Module, Rank, and PokerHand docstrings
  - `poker_hand_cli.py`: Module docstring
- **CI pipenv compatibility** issues
  - Resolved "Python X.X was not found" errors
  - Fixed version constraint conflicts

### Performance
- **CI pipeline execution time** reduced significantly
  - Lint job: ~10-100x faster (ruff vs black+isort+pylint)
  - Parallel execution of independent jobs
  - Cached dependencies for faster subsequent runs

### Developer Impact
- **Breaking Change**: Requires Python 3.10 or higher
  - Python 3.8 and 3.9 are no longer supported (both EOL)
  - Upgrade to Python 3.10+ before using this version
- **Breaking Change**: Development workflow now uses ruff instead of black/isort/pylint
  - Old: `black *.py && isort *.py && pylint *.py`
  - New: `ruff format *.py && ruff check --fix *.py`
- **Pre-commit hooks** available for local development
  - Install: `pre-commit install`
  - Run: `pre-commit run --all-files`

### Migration Notes
This release implements Phase 1 & 2 of the modernization plan:
- ✅ Migrated to ruff for linting and formatting
- ✅ Created `pyproject.toml` with centralized config
- ✅ Established comprehensive CI/CD pipelines
- ✅ Added auto-format workflow for PRs
- ⏳ Still using pipenv for dependency management (future: migrate to uv)

See `TODO.md` for the complete modernization roadmap.

## [1.x] - Legacy

### Summary
Previous versions used traditional Python tooling:
- **Formatting**: Black 23.1a1 (pre-release)
- **Import sorting**: isort 5.12.0
- **Linting**: Pylint 3.0.0a5 (pre-release)
- **Dependency management**: Pipenv
- **No CI/CD**: Manual testing and quality checks

### Known Issues in 1.x
- Pre-release versions of tooling (black, pylint)
- No automated testing in CI
- Scattered configuration across multiple files
- Slow linting and formatting checks
- No automatic code formatting on PRs

---

## Version History

- **2.0.0-beta.1** (2025-11-11) - Modern tooling, CI/CD, ruff migration
- **1.x** (Legacy) - Original implementation with black/isort/pylint

[2.0.0-beta.1]: https://github.com/jonathanza/poker_hands/compare/v1.0.0...v2.0.0-beta.1
