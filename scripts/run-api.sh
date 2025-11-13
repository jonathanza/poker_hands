#!/usr/bin/env bash
#
# Start the FastAPI server
#

set -e

PORT="${PORT:-8000}"
HOST="${HOST:-0.0.0.0}"

echo "Starting Poker Hands API server..."
echo "  Host: $HOST"
echo "  Port: $PORT"
echo ""
echo "API documentation will be available at:"
echo "  http://localhost:$PORT/api/docs"
echo ""

uv run uvicorn api.main:app --host "$HOST" --port "$PORT" --reload
