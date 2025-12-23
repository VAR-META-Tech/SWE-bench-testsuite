#!/bin/bash

# Setup script for SWE-bench Test Suite
# This script installs all dependencies and clones the SWE-bench repository

set -e  # Exit on error

echo "🚀 Setting up SWE-bench Test Suite..."

# Check if Python 3.9+ is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "✓ Found Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Initialize and update git submodules
echo "📥 Initializing SWE-bench submodule..."
git submodule update --init --recursive

# Install dependencies from pyproject.toml
echo "📦 Installing dependencies from pyproject.toml..."
pip install -e .

# Install SWE-bench in editable mode
if [ -d "SWE-bench" ]; then
    echo "📦 Installing SWE-bench in editable mode..."
    pip install -e ./SWE-bench
else
    echo "⚠️  Warning: SWE-bench directory not found, skipping installation"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source .venv/bin/activate"
echo ""
echo "To run tests, use:"
echo "  pytest"
echo ""
