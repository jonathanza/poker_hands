# Development Scripts

This directory contains helper scripts for development and deployment.

## 📦 Setup Script

### `setup.sh`

Installs all dependencies and sets up the development environment.

**Usage:**
```bash
# Core dependencies only
./scripts/setup.sh

# With API support (FastAPI, uvicorn)
./scripts/setup.sh --api

# Show help
./scripts/setup.sh --help
```

**What it does:**
- ✅ Checks Python version (3.10+ required)
- ✅ Installs `uv` if not present
- ✅ Installs project dependencies
- ✅ Sets up pre-commit hooks
- ✅ Verifies installation with tests

## 🚀 Run Scripts

### `run-api.sh`

Starts the FastAPI server with auto-reload.

**Usage:**
```bash
./scripts/run-api.sh

# Custom host/port
PORT=8080 ./scripts/run-api.sh
HOST=0.0.0.0 PORT=8000 ./scripts/run-api.sh
```

**Access:**
- API docs: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

### `dev.sh`

Development mode: Starts API server and opens documentation in browser.

**Usage:**
```bash
./scripts/dev.sh

# Custom port
PORT=8080 ./scripts/dev.sh
```

## 🧪 Test Script

### `test.sh`

Runs tests with various options.

**Usage:**
```bash
# Run all tests
./scripts/test.sh

# Run with coverage report
./scripts/test.sh --coverage

# Run specific test suites
./scripts/test.sh --api      # API tests only
./scripts/test.sh --core     # Core library tests only
./scripts/test.sh --legacy   # Legacy tests only

# Show help
./scripts/test.sh --help
```

## 🔍 Lint Script

### `lint.sh`

Checks and fixes code formatting and linting issues.

**Usage:**
```bash
# Check formatting and linting
./scripts/lint.sh

# Auto-fix issues
./scripts/lint.sh --fix

# Show help
./scripts/lint.sh --help
```

## 🛠️ Quick Start

```bash
# 1. Setup project
./scripts/setup.sh --api

# 2. Run tests
./scripts/test.sh

# 3. Start development server
./scripts/dev.sh
```

## 📝 Notes

- All scripts use `uv run` to ensure correct virtual environment
- Scripts are executable (`chmod +x`)
- Color-coded output for better readability
- Graceful error handling with helpful messages
