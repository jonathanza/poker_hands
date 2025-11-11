# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
