#!/usr/bin/env bash
#
# Run tests with optional coverage
#

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

print_step() {
    echo -e "${BLUE}==>${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

if [ "$1" == "--coverage" ] || [ "$1" == "-c" ]; then
    print_step "Running tests with coverage..."
    uv run --with coverage coverage run --source=core,api -m unittest discover -s tests -p "test_*.py"
    uv run --with coverage coverage run --append -m unittest unit_tests.py
    echo ""
    print_step "Coverage Report:"
    uv run --with coverage coverage report
    print_success "Tests completed with coverage"
elif [ "$1" == "--api" ]; then
    print_step "Running API tests only..."
    uv run python -m unittest tests.test_api -v
    print_success "API tests completed"
elif [ "$1" == "--core" ]; then
    print_step "Running core tests only..."
    uv run python -m unittest tests.test_core tests.test_properties -v
    print_success "Core tests completed"
elif [ "$1" == "--legacy" ]; then
    print_step "Running legacy tests only..."
    uv run python -m unittest unit_tests.py -v
    print_success "Legacy tests completed"
elif [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  --coverage, -c    Run with coverage report"
    echo "  --api             Run API tests only"
    echo "  --core            Run core library tests only"
    echo "  --legacy          Run legacy tests only"
    echo "  -h, --help        Show this help"
    echo ""
    echo "Examples:"
    echo "  $0                # Run all tests"
    echo "  $0 --coverage     # Run with coverage"
    echo "  $0 --api          # Run API tests only"
else
    print_step "Running all tests..."
    uv run python -m unittest discover -s tests -p "test_*.py" -v
    uv run python -m unittest unit_tests.py -v
    print_success "All tests completed"
fi
