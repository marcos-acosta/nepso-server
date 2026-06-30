#!/usr/bin/env bash
set -euo pipefail

# Start the server in the background
uv run main.py &
SERVER_PID=$!

# Kill the server when this script exits (Ctrl-C included)
trap "kill $SERVER_PID 2>/dev/null" EXIT

# Expose it via ngrok (runs in the foreground)
ngrok http 8000
