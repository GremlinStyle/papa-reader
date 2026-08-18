#!/usr/bin/bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Running from: $SCRIPT_DIR"

if command -v python3 >/dev/null 2>&1; then
    echo "Python 3 is installed:"
    python3 --version
else
    echo "Python 3 is not installed."
    exit 1
fi

VENV="$SCRIPT_DIR/.venv_reader"

echo "Creating virtual environment..."
python3 -m venv "$VENV"

echo "Installing requirements..."
"$VENV/bin/pip" install -r "$SCRIPT_DIR/requirements.txt"

echo "Installation complete."