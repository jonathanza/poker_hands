# TODO: Current Sprint Tasks

**Current Phase**: Phase 3 - Complete Modernization (v2.0.0-beta.2)
**See**: [ROADMAP.md](./ROADMAP.md) for the complete project vision

---

## 📋 Phase 3: Complete Modernization (v2.0.0-beta.2)

**Goal**: Finish migration to modern Python tooling (uv + ruff)

### Status Tracker

#### ✅ Completed (Phase 1 & 2)
- [x] Add CI/CD pipelines (GitHub Actions)
- [x] Migrate linting from black + isort + pylint → ruff
- [x] Add auto-format workflow for PRs
- [x] Create pre-commit hooks configuration
- [x] Centralize configuration in pyproject.toml
- [x] Add CHANGELOG and semantic versioning
- [x] Update to Python 3.10+ (drop EOL versions)
- [x] Multi-version testing (3.10, 3.11, 3.12, 3.13)

#### 🚧 In Progress (Phase 3)
- [ ] Migrate from pipenv to uv
  - [ ] Update pyproject.toml dependencies
  - [ ] Create uv.lock file
  - [ ] Update CI workflows to use uv
  - [ ] Update CLAUDE.md with uv commands
  - [ ] Remove Pipfile and Pipfile.lock
  - [ ] Test all workflows with uv
- [ ] Documentation updates
  - [ ] Update README with uv installation instructions
  - [ ] Update development workflow guide
  - [ ] Add onboarding guide for new contributors

---

## 🎯 Detailed Migration Plan: Pipenv → uv

### Why uv?
- **10-100x faster** than pipenv
- Modern, actively maintained
- Compatible with standard pyproject.toml
- Single tool for environments and dependencies
- Better resolution algorithm
- Built-in lock file support

### Migration Steps

#### Step 1: Update pyproject.toml
Current dependencies are already in `pyproject.toml` from Phase 2.

**Current structure:**
```toml
[project]
dependencies = [
    "rich>=13.3.1",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.8.0",
    "coverage>=7.1.0",
    "pre-commit>=3.0.0",
]
```

**No changes needed** - Already compatible with uv!

#### Step 2: Install uv
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

#### Step 3: Create lock file
```bash
# Initialize uv and create lock file
uv lock

# This creates uv.lock with pinned versions
```

#### Step 4: Install dependencies
```bash
# Install all dependencies including dev
uv sync --dev

# Or just production dependencies
uv sync
```

#### Step 5: Update CI workflows

**File: `.github/workflows/ci.yml`**

Replace pipenv installation:
```yaml
# OLD
- name: Install pipenv
  run: pip install pipenv

- name: Install dependencies
  run: pipenv install --python $(which python) --dev --skip-lock --pre

- name: Run tests
  run: pipenv run python -m unittest unit_tests.py
```

With uv:
```yaml
# NEW
- name: Install uv
  run: curl -LsSf https://astral.sh/uv/install.sh | sh

- name: Install dependencies
  run: uv sync --dev

- name: Run tests
  run: uv run python -m unittest unit_tests.py
```

**Update all jobs**:
- [ ] Lint job (if needed)
- [ ] Test job (all Python versions)
- [ ] CLI smoke test job
- [ ] Coverage job

#### Step 6: Update CLAUDE.md

Replace development commands:
```markdown
## Development Commands

### Environment Setup

```bash
# OLD: Pipenv
pipenv install --dev --skip-lock --pre
pipenv shell

# NEW: uv
uv sync --dev
```

### Running Tests

```bash
# OLD
pipenv run python -m unittest unit_tests.py
pipenv run coverage run -m unittest unit_tests.py

# NEW
uv run python -m unittest unit_tests.py
uv run coverage run -m unittest unit_tests.py
```

### Linting

```bash
# Formatting (same - using ruff)
uv run ruff format *.py

# Linting (same - using ruff)
uv run ruff check --fix *.py
```

### Running the CLI

```bash
# OLD
pipenv run python3 poker_hand_cli.py

# NEW
uv run python3 poker_hand_cli.py
```
```

#### Step 7: Remove Pipfile
```bash
# After verifying everything works
git rm Pipfile Pipfile.lock
```

#### Step 8: Update .gitignore
```
# Add uv cache (if not already present)
.uv/
uv.lock  # Or commit this - it's your lock file
```

**Decision**: Should we commit `uv.lock`?
- ✅ **Yes** - For reproducible builds (recommended)
- ❌ **No** - For library distribution (less common)

**Recommendation**: Commit `uv.lock` for this project since we have applications (CLI, future API).

---

## 📊 Command Migration Reference

| Task | Old (pipenv) | New (uv) |
|------|--------------|----------|
| **Setup environment** | `pipenv install --dev` | `uv sync --dev` |
| **Add dependency** | `pipenv install <pkg>` | `uv add <pkg>` |
| **Add dev dependency** | `pipenv install --dev <pkg>` | `uv add --dev <pkg>` |
| **Remove dependency** | `pipenv uninstall <pkg>` | `uv remove <pkg>` |
| **Run command** | `pipenv run <cmd>` | `uv run <cmd>` |
| **Activate shell** | `pipenv shell` | Not needed with `uv run` |
| **Update dependencies** | `pipenv update` | `uv lock --upgrade` |
| **Show dependencies** | `pipenv graph` | `uv pip list` |

---

## ✅ Testing Checklist

Before completing Phase 3, verify:

### Local Testing
- [ ] `uv sync --dev` installs all dependencies
- [ ] `uv run python -m unittest unit_tests.py` passes
- [ ] `uv run coverage run -m unittest unit_tests.py` works
- [ ] `uv run ruff format *.py` works
- [ ] `uv run ruff check *.py` passes
- [ ] `uv run python poker_hand_cli.py` launches CLI
- [ ] Pre-commit hooks still work
- [ ] All development workflows functional

### CI Testing
- [ ] All CI jobs pass with uv
- [ ] Test matrix works (Python 3.10, 3.11, 3.12, 3.13)
- [ ] Coverage reporting works
- [ ] Auto-format workflow still works

### Documentation
- [ ] CLAUDE.md updated
- [ ] README.md updated
- [ ] CHANGELOG.md updated
- [ ] Comments in files updated

---

## 🎯 Success Criteria

Phase 3 is complete when:
- ✅ No pipenv dependencies remain
- ✅ All development uses uv
- ✅ All CI uses uv
- ✅ Documentation reflects new workflow
- ✅ All tests pass
- ✅ Coverage remains ≥ 90%
- ✅ Tagged as v2.0.0-beta.2

---

## 📈 Expected Benefits

After Phase 3 completion:
- ⚡ **10-100x faster** dependency installation
- 🎯 **Simpler workflow** (no shell activation needed)
- 📦 **Better resolution** of dependency conflicts
- 🔒 **More reliable** reproducible builds
- 🚀 **Ready for growth** (supports future API/TUI dependencies)

---

## 🔗 Related Documents

- [ROADMAP.md](./ROADMAP.md) - Full project vision (Phases 4-9)
- [CHANGELOG.md](./CHANGELOG.md) - Version history
- [CLAUDE.md](./CLAUDE.md) - Development guide (will be updated)
- [README.md](./README.md) - Project overview

---

## 📝 Next Steps After Phase 3

Once Phase 3 is complete, proceed to:
- **Phase 4**: Refactor core library with Pydantic models
- **Phase 5**: Implement FastAPI backend
- **Phase 6**: Build web interface
- **Phase 7**: Create flashy TUI with Textual

See [ROADMAP.md](./ROADMAP.md) for details on future phases.

---

**Last Updated**: 2025-11-11
**Current Version**: v2.0.0-beta.1
**Target Version**: v2.0.0-beta.2
