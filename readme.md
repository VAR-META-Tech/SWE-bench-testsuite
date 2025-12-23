
# SWE-bench Test Suite

This project runs SWE-bench inference and evaluation to benchmark AI models.

## Setup

Requirements:
- Python 3.9+
- Docker Desktop (running)
- Git

### Quick Setup

```bash
# Clone with submodules
git clone --recursive https://github.com/VAR-META-Tech/SWE-bench-testsuite.git
cd SWE-bench-testsuite

# Run setup script
./setup.sh

# Activate virtual environment
source .venv/bin/activate
```

### Manual Setup

```bash
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Initialize SWE-bench submodule
git submodule update --init --recursive

# Install dependencies
pip install -e .
pip install -e ./SWE-bench
```

## Usage

### Run Inference (Generate Diffs)
```bash
python run_llama.py
```

### Run Evaluation (Docker)
```bash
python evaluate.py
```

### Run Tests
```bash
pytest test_eval.py
```
