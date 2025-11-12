"""
FastAPI REST API for poker hand classification.

This package provides HTTP endpoints for classifying poker hands,
comparing hands, and batch operations.

Usage:
    # Run the API server
    uvicorn api.main:app --reload

    # Or using the main module
    python -m api.main
"""

from api.main import app

__all__ = ["app"]
