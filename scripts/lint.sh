#!/usr/bin/env bash
#
# Run linting and formatting checks
#

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_step() {
    echo -e "${BLUE}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

if [ "$1" == "--fix" ] || [ "$1" == "-f" ]; then
    print_step "Formatting code with ruff..."
    uv run ruff format .
    print_success "Code formatted"
    
    print_step "Fixing linting issues..."
    uv run ruff check --fix .
    print_success "Linting issues fixed"
elif [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --fix, -f     Auto-fix formatting and linting issues"
    echo "  -h, --help    Show this help"
    echo ""
    echo "Examples:"
    echo "  $0            # Check formatting and linting"
    echo "  $0 --fix      # Auto-fix issues"
else
    print_step "Checking code formatting..."
    if uv run ruff format --check .; then
        print_success "Code is properly formatted"
    else
        print_warning "Code formatting issues found. Run with --fix to auto-format."
        exit 1
    fi
    
    print_step "Running linter..."
    if uv run ruff check .; then
        print_success "No linting issues found"
    else
        print_warning "Linting issues found. Run with --fix to auto-fix."
        exit 1
    fi
    
    print_success "All checks passed"
fi
