#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON="$SCRIPT_DIR/.venv_reader/bin/python"
MAIN="$SCRIPT_DIR/main.py"

if [ ! -f "$PYTHON" ]; then
    echo "Error: virtual environment not found."
    echo "Run setup.sh first."
    exit 1
fi

if [ ! -f "$MAIN" ]; then
    echo "Error: main.py not found."
    exit 1
fi

PID=$(pgrep -f "/tmp/temp_file.wav"|| true)


if [ -n "$PID" ]; then
    echo "Process already running (PID: $PID)"
    kill "$PID"
    exit 0
fi

exec "$PYTHON" "$MAIN"