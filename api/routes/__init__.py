"""
API route modules.
"""

from api.routes.hands import router as hands_router
from api.routes.health import router as health_router

__all__ = ["hands_router", "health_router"]
