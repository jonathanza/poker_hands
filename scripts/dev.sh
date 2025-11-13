#!/usr/bin/env bash
#
# Development mode: Run API with auto-reload and open docs
#

set -e

PORT="${PORT:-8000}"
HOST="${HOST:-127.0.0.1}"

echo "🚀 Starting Poker Hands API in development mode..."
echo ""
echo "📍 API server: http://$HOST:$PORT"
echo "📚 API docs: http://$HOST:$PORT/api/docs"
echo "📖 ReDoc: http://$HOST:$PORT/api/redoc"
echo ""
echo "Press Ctrl+C to stop"
echo ""

# Try to open browser (works on macOS and Linux)
sleep 2 && (command -v open >/dev/null && open "http://$HOST:$PORT/api/docs" || \
            command -v xdg-open >/dev/null && xdg-open "http://$HOST:$PORT/api/docs" || \
            true) &

uv run uvicorn api.main:app --host "$HOST" --port "$PORT" --reload
