# Modern Python Tooling Migration Plan

## Executive Summary

This plan outlines the migration of the poker_hands repository from **pipenv + black + isort + pylint** to **uv + ruff**, modernizing the development workflow with faster, more efficient tooling.

---

## 🎯 Current State Analysis

### Current Toolchain
- **Dependency Management**: Pipenv (Pipfile + Pipfile.lock)
- **Formatting**: Black 23.1a1 (pre-release)
- **Import Sorting**: isort 5.12.0
- **Linting**: Pylint 3.0.0a5 (pre-release)
- **Testing**: unittest + coverage 7.1.0
- **Configuration**: Scattered (`.editorconfig`, `.coveragerc`, defaults)

### Dependencies
- **Production**: `rich==13.3.1`
- **Development**: `black`, `isort`, `pylint`, `coverage`

---

## ✨ Proposed Modern Toolchain

### New Stack
- **Dependency Management**: **uv** (10-100x faster than pip/pipenv)
- **Formatting + Linting**: **ruff** (10-100x faster than black+isort+pylint combined)
- **Testing**: Keep unittest + coverage (no change needed)
- **Configuration**: Centralized `pyproject.toml`

### Why These Tools?

**uv Benefits:**
- ⚡ **10-100x faster** than pipenv for installation
- 🔒 **Compatible** with pip/PyPI ecosystem
- 📦 **Modern standards** - Uses `pyproject.toml`
- 🎯 **Simple CLI** - Intuitive commands
- 🔄 **Lock file support** - Reproducible builds

**ruff Benefits:**
- ⚡ **10-100x faster** than traditional Python tools (written in Rust)
- 🔧 **All-in-one** - Replaces black, isort, pylint, flake8, and more
- 📏 **700+ rules** - More comprehensive than pylint
- 🔄 **Auto-fix** - Automatic fixes for most issues
- ⚙️ **Drop-in replacement** - Compatible with existing configs

---

## 📋 Migration Plan

### Phase 1: Setup & Configuration

#### Step 1.1: Create `pyproject.toml`
Create a modern Python project configuration file that consolidates all tooling settings.

```toml
[project]
name = "poker-hands"
version = "1.0.0"
description = "A Python poker hand classifier"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
dependencies = [
    "rich>=13.3.1",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.8.0",
    "coverage>=7.1.0",
]

[tool.uv]
dev-dependencies = [
    "ruff>=0.8.0",
    "coverage>=7.1.0",
]

[tool.ruff]
# Same line length as black default
line-length = 88
target-version = "py38"

# Select rules: pycodestyle errors (E), Pyflakes (F), isort (I),
# pylint conventions (C), etc.
lint.select = [
    "E",    # pycodestyle errors
    "F",    # Pyflakes
    "I",    # isort
    "N",    # pep8-naming
    "UP",   # pyupgrade
    "B",    # flake8-bugbear
    "C4",   # flake8-comprehensions
    "C90",  # mccabe complexity
    "PL",   # pylint
    "SIM",  # flake8-simplify
]

lint.ignore = [
    "PLR0913",  # Too many arguments (common in poker hand logic)
    "C901",     # Too complex (keep unless problematic)
]

# isort-compatible settings
lint.isort.known-first-party = ["poker_hand", "poker_hand_cli"]

[tool.ruff.format]
# Use single quotes (or keep double - your preference)
quote-style = "double"
indent-style = "space"

[tool.coverage.run]
include = ["poker_*.py"]
omit = ["*/__init__.py", "*/tests/*", "*/venv/*"]

[tool.coverage.report]
exclude_lines = [
    "raise NotImplementedError",
    "return NotImplemented",
    "return None",
    "pass",
]
```

#### Step 1.2: Install uv
```bash
# Install uv (one-time setup)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

#### Step 1.3: Initialize uv project
```bash
# Create lock file from pyproject.toml
uv lock

# Install dependencies
uv sync --dev
```

---

### Phase 2: Migrate Linting Configuration

#### Step 2.1: Test ruff equivalence
Run ruff alongside existing tools to verify compatibility:

```bash
# Format check
ruff format --check *.py
black --check *.py

# Lint check
ruff check *.py
pylint *.py
```

#### Step 2.2: Fine-tune ruff rules
Adjust `pyproject.toml` based on any discrepancies or preferences.

---

### Phase 3: Update Documentation

#### Step 3.1: Update CLAUDE.md
Replace the "Development Commands" section:

**OLD:**
```bash
pipenv install --skip-lock --dev --pre
pipenv shell

black -v *.py
isort *.py
pylint *.py
```

**NEW:**
```bash
# Environment Setup
uv sync --dev

# Linting & Formatting
uv run ruff format *.py          # Format code
uv run ruff check --fix *.py     # Lint and auto-fix
uv run ruff check *.py           # Lint only (no fixes)

# Or use the combined workflow
uv run ruff format *.py && uv run ruff check --fix *.py
```

#### Step 3.2: Update README.md
Add modernization notes if applicable.

---

### Phase 4: Update CI/CD

Update GitHub Actions workflow (`.github/workflows/ci.yml`):

**Replace:**
```yaml
- name: Install dependencies
  run: |
    pip install pipenv
    pipenv install --dev --skip-lock

- name: Lint
  run: |
    pipenv run black --check *.py
    pipenv run isort --check *.py
    pipenv run pylint *.py
```

**With:**
```yaml
- name: Install uv
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv sync --dev

- name: Lint and format
  run: |
    uv run ruff format --check *.py
    uv run ruff check *.py
```

---

### Phase 5: Cleanup

#### Step 5.1: Remove old files
```bash
# After verifying everything works:
git rm Pipfile Pipfile.lock
```

#### Step 5.2: Update .gitignore
```
# Add uv cache
.uv/
uv.lock

# Keep these
.coverage
coverage.xml
__pycache__/
*.pyc
```

---

## 🔄 Command Migration Reference

| Task | Old Command | New Command |
|------|-------------|-------------|
| **Setup** | `pipenv install --dev` | `uv sync --dev` |
| **Add dependency** | `pipenv install <pkg>` | `uv add <pkg>` |
| **Add dev dependency** | `pipenv install --dev <pkg>` | `uv add --dev <pkg>` |
| **Remove dependency** | `pipenv uninstall <pkg>` | `uv remove <pkg>` |
| **Run command** | `pipenv run <cmd>` | `uv run <cmd>` |
| **Format** | `black -v *.py` | `uv run ruff format *.py` |
| **Sort imports** | `isort *.py` | `uv run ruff check --fix --select I *.py` |
| **Lint** | `pylint *.py` | `uv run ruff check *.py` |
| **Format + Lint** | (3 commands) | `uv run ruff format *.py && uv run ruff check --fix *.py` |
| **Tests** | `python -m unittest` | `uv run python -m unittest` |
| **Coverage** | `coverage run -m unittest` | `uv run coverage run -m unittest` |

---

## 📊 Expected Improvements

### Performance Gains
- **Dependency installation**: 10-100x faster (seconds vs minutes)
- **Linting**: 10-100x faster (instant feedback)
- **Formatting**: 10-100x faster

### Developer Experience
- ✅ **Single tool** for format + lint + import sort
- ✅ **Unified configuration** in `pyproject.toml`
- ✅ **Faster feedback loop** = more productive development
- ✅ **Modern standards** alignment with Python packaging ecosystem
- ✅ **Better error messages** from ruff

### Maintenance Benefits
- 🔧 Fewer dependencies to manage (1 tool vs 3)
- 📦 Smaller virtual environments
- 🎯 Cleaner, more maintainable configuration
- 🔄 Active development and community support

---

## ⚠️ Potential Challenges & Mitigations

### Challenge 1: Ruff rule differences
**Issue**: Ruff may flag issues that pylint didn't (or vice versa)

**Mitigation**:
- Start with a conservative ruleset (E, F, I)
- Gradually enable more rules (PL for pylint equivalents)
- Use `lint.ignore` in `pyproject.toml` for project-specific exceptions

### Challenge 2: Pre-commit hooks
**Issue**: If pre-commit hooks exist, they need updating

**Mitigation**:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

### Challenge 3: IDE integration
**Issue**: IDE may be configured for black/pylint

**Mitigation**:
- **VSCode**: Install "Ruff" extension, disable Black/Pylint extensions
- **PyCharm**: Use "Ruff" plugin from marketplace
- Most modern editors have ruff support

---

## 🧪 Testing Strategy

### Validation Checklist

#### Pre-Migration
- [ ] Run full test suite: `coverage run -m unittest unit_tests.py`
- [ ] Verify all tests pass
- [ ] Document current coverage percentage

#### During Migration
- [ ] Create `pyproject.toml` with equivalent settings
- [ ] Run `uv sync --dev` successfully
- [ ] Compare formatting: `ruff format *.py` vs `black *.py`
- [ ] Compare linting: Review ruff output vs pylint output
- [ ] Adjust ruff rules to match desired style

#### Post-Migration
- [ ] Run full test suite again: `uv run coverage run -m unittest unit_tests.py`
- [ ] Verify all tests still pass
- [ ] Verify coverage remains ≥80% per file, ≥90% overall
- [ ] Test CLI: `uv run python poker_hand_cli.py`
- [ ] Verify code formatting matches expectations
- [ ] Update all documentation

---

## 📅 Implementation Timeline

**Estimated time**: 1-2 hours

1. **Setup** (20 min): Create `pyproject.toml`, install uv
2. **Migration** (30 min): Test ruff, tune configuration
3. **Documentation** (20 min): Update CLAUDE.md, README
4. **Testing** (20 min): Full validation
5. **Cleanup** (10 min): Remove old files

---

## 🎯 Success Criteria

Migration is complete when:
- ✅ `uv sync --dev` installs all dependencies
- ✅ `uv run ruff format *.py` formats code
- ✅ `uv run ruff check *.py` passes (or flags expected issues)
- ✅ All tests pass via `uv run python -m unittest unit_tests.py`
- ✅ Coverage remains ≥80% per file, ≥90% overall
- ✅ CLAUDE.md reflects new commands
- ✅ Old pipenv files removed
- ✅ Can run poker hand CLI: `uv run python poker_hand_cli.py`

---

## 📚 Additional Resources

- **uv documentation**: https://docs.astral.sh/uv/
- **ruff documentation**: https://docs.astral.sh/ruff/
- **ruff rules**: https://docs.astral.sh/ruff/rules/
- **Migrating from black**: https://docs.astral.sh/ruff/formatter/#black-compatibility
- **Migrating from pylint**: https://docs.astral.sh/ruff/faq/#how-does-ruff-compare-to-pylint

---

## 💡 Implementation Status

**Status**: ⏸️ PAUSED - Waiting for CI/CD setup

**Next Steps**:
1. ✅ Set up GitHub Actions CI/CD with current tooling (pipenv, black, isort, pylint)
2. ✅ Verify all tests pass in CI
3. ⏳ Execute this migration plan
4. ⏳ Update CI/CD to use uv + ruff
5. ⏳ Verify no regressions via CI
