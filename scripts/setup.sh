#!/usr/bin/env bash
#
# Setup script for Poker Hands project
# Installs uv, dependencies, and sets up development environment
#

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_step() {
    echo -e "${BLUE}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Main setup
main() {
    echo -e "${GREEN}"
    echo "╔═══════════════════════════════════════════════╗"
    echo "║   Poker Hands Setup Script                   ║"
    echo "║   v3.0.0                                      ║"
    echo "╚═══════════════════════════════════════════════╝"
    echo -e "${NC}"

    # Check Python version
    print_step "Checking Python version..."
    if ! command_exists python3; then
        print_error "Python 3 is not installed. Please install Python 3.10 or higher."
        exit 1
    fi

    PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
    REQUIRED_VERSION="3.10"

    if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
        print_error "Python $PYTHON_VERSION found, but Python $REQUIRED_VERSION or higher is required."
        exit 1
    fi
    print_success "Python $PYTHON_VERSION detected"

    # Install uv if not present
    print_step "Checking for uv package manager..."
    if ! command_exists uv; then
        print_warning "uv not found. Installing uv..."
        curl -LsSf https://astral.sh/uv/install.sh | sh

        # Add uv to PATH for current session
        export PATH="$HOME/.cargo/bin:$PATH"

        if command_exists uv; then
            print_success "uv installed successfully"
        else
            print_error "Failed to install uv. Please install manually from: https://github.com/astral-sh/uv"
            exit 1
        fi
    else
        UV_VERSION=$(uv --version | cut -d' ' -f2)
        print_success "uv $UV_VERSION is already installed"
    fi

    # Install project dependencies
    print_step "Installing project dependencies..."
    if [ "$1" == "--api" ] || [ "$1" == "--all" ]; then
        print_step "Installing with API support (FastAPI, uvicorn)..."
        uv sync --dev --extra api
    else
        print_step "Installing core dependencies..."
        uv sync --dev
        print_warning "API dependencies not installed. Run with --api flag to include them."
    fi
    print_success "Dependencies installed"

    # Install pre-commit hooks (optional)
    print_step "Setting up pre-commit hooks..."
    if command_exists pre-commit; then
        pre-commit install
        print_success "Pre-commit hooks installed"
    else
        print_warning "pre-commit not found. Skipping hook installation."
        print_warning "To install: pip install pre-commit && pre-commit install"
    fi

    # Verify installation
    print_step "Verifying installation..."

    # Test core library
    if uv run python -c "from core import Card, Hand, HandClassifier; print('Core library OK')" 2>/dev/null; then
        print_success "Core library working"
    else
        print_error "Core library verification failed"
        exit 1
    fi

    # Test API if installed
    if [ "$1" == "--api" ] || [ "$1" == "--all" ]; then
        if uv run python -c "from api.main import app; print('API OK')" 2>/dev/null; then
            print_success "API library working"
        else
            print_error "API verification failed"
            exit 1
        fi
    fi

    # Run tests
    print_step "Running tests..."
    if uv run python -m unittest discover -s tests -p "test_*.py" -q 2>/dev/null; then
        print_success "All tests passed"
    else
        print_error "Some tests failed. Run 'uv run python -m unittest discover -s tests' for details."
    fi

    # Success message
    echo ""
    echo -e "${GREEN}╔═══════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║  ✓ Setup Complete!                           ║${NC}"
    echo -e "${GREEN}╚═══════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo ""

    if [ "$1" != "--api" ] && [ "$1" != "--all" ]; then
        echo "  ${YELLOW}To install API dependencies:${NC}"
        echo "    ./scripts/setup.sh --api"
        echo ""
    fi

    echo "  ${YELLOW}Try the core library:${NC}"
    echo "    uv run python -c 'from core import Card, Hand, HandClassifier; print(Card(rank=\"A\", suit=\"H\"))'"
    echo ""

    if [ "$1" == "--api" ] || [ "$1" == "--all" ]; then
        echo "  ${YELLOW}Start the API server:${NC}"
        echo "    uv run uvicorn api.main:app --reload"
        echo ""
        echo "  ${YELLOW}Access API documentation:${NC}"
        echo "    http://localhost:8000/api/docs"
        echo ""
    fi

    echo "  ${YELLOW}Run tests:${NC}"
    echo "    uv run python -m unittest discover -s tests"
    echo ""
    echo "  ${YELLOW}Run CLI:${NC}"
    echo "    uv run python poker_hand_cli.py"
    echo ""
}

# Show usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --api      Install with API dependencies (FastAPI, uvicorn)"
    echo "  --all      Install everything (same as --api)"
    echo "  -h, --help Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0              # Install core dependencies only"
    echo "  $0 --api        # Install with API support"
}

# Parse arguments
if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    usage
    exit 0
fi

# Run main setup
main "$1"
