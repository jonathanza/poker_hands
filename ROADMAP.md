# Project Roadmap

**Version**: 2.0.0-beta.1 → 3.0.0 and beyond
**Project**: poker-hands - Python Poker Hand Classifier
**Vision**: Transform from a simple library into a comprehensive poker hand analysis platform with CLI, API, Web UI, and TUI interfaces.

---

## 🎯 Project Vision

Create a modern, multi-interface poker hand classifier that demonstrates best practices in Python development while providing a delightful user experience across multiple interaction modes.

### Core Philosophy
- **Library-first**: Core poker logic remains a clean, testable library
- **API-driven**: All interfaces consume a unified FastAPI backend
- **Modern tooling**: Use cutting-edge Python tools (uv, ruff, FastAPI)
- **Beautiful interfaces**: Rich TUI and polished web UI
- **Developer-friendly**: Comprehensive docs, types, tests, CI/CD

---

## 📊 Current Status: v2.0.0-beta.1

### ✅ Completed (Phase 1 & 2)
- [x] Comprehensive CI/CD pipelines (GitHub Actions)
- [x] Migrated to ruff for linting and formatting
- [x] Auto-format workflow for PRs
- [x] Pre-commit hooks configuration
- [x] Centralized configuration (pyproject.toml)
- [x] CHANGELOG and semantic versioning
- [x] Python 3.10+ support (dropped EOL versions)
- [x] Multi-version testing (3.10, 3.11, 3.12, 3.13)
- [x] Coverage enforcement (90%+ threshold)

### 🎨 Current Architecture
```
poker_hands/
├── poker_hand.py          # Core library (Rank enum, PokerHand class)
├── poker_hand_cli.py      # Simple CLI using rich
└── unit_tests.py          # Test suite
```

---

## 🚀 Roadmap

### Phase 3: Complete Modernization (v2.0.0-beta.2)
**Timeline**: Current sprint
**Goal**: Finish migration to modern tooling

#### Tasks
- [ ] Migrate from pipenv to uv
  - [ ] Replace Pipfile with pyproject.toml dependencies
  - [ ] Update CI workflows to use uv
  - [ ] Update documentation with uv commands
  - [ ] Remove Pipfile and Pipfile.lock
- [ ] Update CLAUDE.md with new workflows
- [ ] Add developer onboarding guide
- [ ] Tag release: `v2.0.0-beta.2`

**Success Criteria**: All development workflows use uv + ruff

---

### Phase 4: Refactor Core Library (v2.1.0) ✅ COMPLETED
**Timeline**: ~~Next sprint~~ **Completed 2025-11-11**
**Goal**: Prepare library for API integration

#### Architectural Changes
```
poker_hands/
├── core/
│   ├── __init__.py
│   ├── models.py          # Pydantic models for cards and hands
│   ├── classifier.py      # Core classification logic
│   ├── enums.py          # Rank, Suit, HandType enums
│   └── validators.py     # Input validation
├── cli/
│   └── cli.py            # Refactored CLI (uses core)
├── tests/
│   ├── test_core.py      # 37 unit tests, 91% coverage
│   ├── test_properties.py # 23 Hypothesis property tests
│   └── __init__.py
├── poker_hand.py          # Backward-compatible wrapper
└── unit_tests.py          # Legacy tests (11 tests, all passing)
```

#### Tasks
- [x] Add type hints everywhere (mypy strict mode)
- [x] Refactor into modular architecture
- [x] Introduce Pydantic models for validation
- [x] Separate concerns (models, logic, presentation)
- [x] Add comprehensive docstrings (Sphinx-compatible)
- [x] Achieve 91% test coverage (exceeds 90% target)
- [x] Add property-based testing (Hypothesis)
- [x] Update documentation (CLAUDE.md, CHANGELOG.md)
- [x] Create backward-compatible wrapper (no breaking changes)

**Success Criteria**: ✅ Clean, testable core library ready for API integration

#### Achievements
- 71 total tests (37 core + 23 property + 11 legacy)
- 91% core library coverage
- 100% backward compatibility maintained
- Type hints throughout
- Immutable Pydantic models
- Enhanced CLI with rich formatting

---

### Phase 5: FastAPI Backend (v3.0.0)
**Timeline**: Month 1
**Goal**: Create production-ready REST API

#### New Structure
```
poker_hands/
├── core/                  # Core library (from Phase 4)
├── api/
│   ├── __init__.py
│   ├── main.py           # FastAPI app
│   ├── routes/
│   │   ├── hands.py      # Hand classification endpoints
│   │   └── health.py     # Health check, metrics
│   ├── schemas/
│   │   ├── requests.py   # Request models
│   │   └── responses.py  # Response models
│   ├── middleware.py     # CORS, rate limiting, logging
│   └── dependencies.py   # Dependency injection
├── cli/                   # CLI interface (uses core)
└── tests/
    ├── test_core.py
    ├── test_api.py
    └── test_integration.py
```

#### API Endpoints
```
GET  /api/v1/health              # Health check
POST /api/v1/classify            # Classify a single hand
POST /api/v1/classify/batch      # Classify multiple hands
POST /api/v1/compare             # Compare two hands
GET  /api/v1/hands/examples      # Get example hands
GET  /api/docs                   # OpenAPI documentation
```

#### Features
- [ ] RESTful API with FastAPI
- [ ] OpenAPI/Swagger documentation
- [ ] Request validation with Pydantic
- [ ] Error handling and status codes
- [ ] Rate limiting
- [ ] CORS configuration
- [ ] Logging and monitoring
- [ ] Dockerized deployment
- [ ] Health checks and metrics
- [ ] API versioning (v1)
- [ ] Authentication (optional, for future)

#### Dependencies
```toml
[project.optional-dependencies]
api = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "pydantic>=2.0.0",
    "python-multipart>=0.0.6",
]
```

**Success Criteria**: Production-ready API with comprehensive docs

---

### Phase 6: Web Interface (v3.1.0)
**Timeline**: Month 2
**Goal**: Beautiful, responsive web UI

#### Technology Stack
- **Frontend**: Modern framework (React/Vue/Svelte - TBD)
- **Styling**: Tailwind CSS or similar
- **API Client**: Generated from OpenAPI spec
- **Build**: Vite or similar
- **Deployment**: Static hosting (Vercel, Netlify, etc.)

#### Features
- [ ] Interactive card input interface
- [ ] Visual hand classification display
- [ ] Animated card reveals
- [ ] Hand comparison tool
- [ ] Example hands gallery
- [ ] Responsive design (mobile-first)
- [ ] Dark mode support
- [ ] Share results (URL parameters)
- [ ] Hand history
- [ ] Educational mode (explain classifications)

#### Structure
```
poker_hands/
├── core/                  # Core library
├── api/                   # FastAPI backend
├── cli/                   # CLI interface
├── web/
│   ├── src/
│   │   ├── components/   # UI components
│   │   ├── api/         # API client
│   │   ├── pages/       # Page components
│   │   └── assets/      # Images, styles
│   ├── public/
│   ├── package.json
│   └── vite.config.js
└── tests/
```

**Success Criteria**: Polished web UI consuming API

---

### Phase 7: Terminal UI (TUI) (v3.2.0)
**Timeline**: Month 3
**Goal**: Flashy, beautiful terminal interface using rich

#### Technology
- **Framework**: Rich + Textual (modern TUI framework)
- **Features**: Interactive, keyboard-driven
- **Style**: Beautiful animations, colors, layouts

#### Features
- [ ] Interactive card selection (keyboard/mouse)
- [ ] Live hand classification
- [ ] Visual card display (Unicode cards)
- [ ] Hand comparison mode
- [ ] Practice mode (random hands)
- [ ] Tutorial mode
- [ ] Keyboard shortcuts
- [ ] Mouse support
- [ ] Smooth animations
- [ ] Color schemes (themes)
- [ ] Help system
- [ ] Statistics tracking

#### Structure
```
poker_hands/
├── core/                  # Core library
├── api/                   # FastAPI backend (optional for TUI)
├── cli/                   # Simple CLI
├── tui/
│   ├── __init__.py
│   ├── app.py            # Main Textual app
│   ├── screens/
│   │   ├── main.py       # Main screen
│   │   ├── classify.py   # Classification screen
│   │   ├── compare.py    # Comparison screen
│   │   └── help.py       # Help screen
│   ├── widgets/
│   │   ├── card.py       # Card widget
│   │   ├── hand.py       # Hand display widget
│   │   └── result.py     # Result widget
│   └── themes/
│       ├── default.py
│       └── poker.py
└── tests/
```

#### Dependencies
```toml
[project.optional-dependencies]
tui = [
    "textual>=0.40.0",
    "rich>=13.3.1",
]
```

**Success Criteria**: Beautiful, interactive TUI that rivals GUI apps

---

### Phase 8: Documentation & Polish (v3.3.0)
**Timeline**: Month 4
**Goal**: Comprehensive documentation and examples

#### Documentation
- [ ] Complete README with all interfaces
- [ ] API documentation (OpenAPI)
- [ ] Library documentation (Sphinx)
- [ ] Tutorial series
- [ ] Architecture decision records (ADRs)
- [ ] Contributing guide
- [ ] Code of conduct
- [ ] Security policy
- [ ] Performance benchmarks
- [ ] Deployment guides

#### Polish
- [ ] Add demo GIFs/videos
- [ ] Create project logo
- [ ] Add badges (coverage, build, version)
- [ ] Optimize performance
- [ ] Add metrics and monitoring
- [ ] Security audit
- [ ] Accessibility audit (web UI)
- [ ] Mobile optimization (web UI)
- [ ] Cross-platform testing (CLI/TUI)

**Success Criteria**: Production-ready, well-documented project

---

### Phase 9: Advanced Features (v4.0.0+)
**Timeline**: Future
**Goal**: Advanced poker analysis features

#### Potential Features
- [ ] Multi-hand analysis
- [ ] Odds calculator
- [ ] Hand strength rankings
- [ ] Player vs player comparisons
- [ ] Tournament mode
- [ ] Hand history analysis
- [ ] Statistics and visualizations
- [ ] AI opponent (ML model)
- [ ] Multiplayer support
- [ ] Real-time updates (WebSockets)
- [ ] Mobile apps (React Native)
- [ ] Desktop apps (Electron/Tauri)

---

## 🎯 Technical Goals Across All Phases

### Code Quality
- 100% test coverage
- Type hints everywhere (mypy strict)
- Zero linting errors (ruff)
- Comprehensive docstrings
- Property-based testing

### Performance
- Sub-millisecond hand classification
- API response time < 100ms
- TUI 60fps animations
- Efficient batch processing

### DevOps
- CI/CD for all components
- Automated testing (unit, integration, e2e)
- Docker containers
- Kubernetes manifests (optional)
- Monitoring and logging
- Error tracking (Sentry)

### Security
- Input validation everywhere
- Rate limiting
- CORS configuration
- Security headers
- Dependency scanning
- OWASP compliance

---

## 📦 Deployment Architecture (End State)

```
┌─────────────────────────────────────────────────┐
│                    Users                        │
└──────────────┬──────────────┬──────────────────┘
               │              │
         ┌─────┴─────┐   ┌───┴───┐
         │  Browser  │   │Terminal│
         │  (Web UI) │   │(TUI/CLI)│
         └─────┬─────┘   └───┬───┘
               │             │
               │             └──────────┐
         ┌─────┴──────────────────┐    │
         │   FastAPI Backend      │◄───┘
         │   (REST API)           │
         └─────┬──────────────────┘
               │
         ┌─────┴──────────────────┐
         │   Core Library         │
         │   (poker_hands.core)   │
         └────────────────────────┘
```

---

## 🎨 Example Use Cases

### 1. Library (v2.x)
```python
from poker_hands import PokerHand

hand = PokerHand([('A', 'H'), ('K', 'H'), ('Q', 'H'), ('J', 'H'), ('T', 'H')])
print(hand.classify())  # "Royal Flush"
```

### 2. CLI (v2.x)
```bash
$ python poker_hand_cli.py
Enter a card in the format 'rank suit': ace hearts
# ... interactive prompts ...
Hand: A♥ K♥ Q♥ J♥ T♥
Classification: Royal Flush
```

### 3. API (v3.0+)
```bash
$ curl -X POST http://localhost:8000/api/v1/classify \
  -H "Content-Type: application/json" \
  -d '{"cards": [{"rank": "A", "suit": "H"}, ...]}'
{
  "classification": "Royal Flush",
  "strength": 10,
  "probability": 0.000154
}
```

### 4. TUI (v3.2+)
```bash
$ poker-tui
# Beautiful, interactive terminal interface with animations
```

---

## 📈 Success Metrics

### Project Maturity
- ✅ Unit test coverage ≥ 100%
- ✅ API documentation coverage = 100%
- ✅ Zero security vulnerabilities
- ✅ Performance benchmarks met
- ✅ User feedback incorporated

### Community
- GitHub stars ≥ 100
- Active contributors ≥ 5
- Issues/PRs responded to within 48h
- Monthly active users ≥ 1000

---

## 🔗 Related Documents

- [CHANGELOG.md](./CHANGELOG.md) - Version history
- [TODO.md](./TODO.md) - Current sprint tasks
- [CLAUDE.md](./CLAUDE.md) - Development guide
- [README.md](./README.md) - Project overview

---

## 📝 Notes

This roadmap is a living document and will evolve based on:
- Community feedback
- Technical discoveries
- Resource availability
- Priority changes

**Last Updated**: 2025-11-11 (v2.0.0-beta.1)
