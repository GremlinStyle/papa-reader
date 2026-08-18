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

exec "$PYTHON" "$MAIN"