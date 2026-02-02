#!/bin/bash
set -e

# Define virtual environment directory
VENV_DIR="venv"

# check if venv exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run build script
echo "Building site..."
python build.py

echo "Done! Site generated."
