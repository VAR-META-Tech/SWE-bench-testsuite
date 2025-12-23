# SWE-bench Test Suite

A well-structured wrapper and test suite for running [SWE-bench](https://github.com/princeton-nlp/SWE-bench) evaluations and inference.

## 📁 Project Structure

```
SWE-bench-testsuite/
├── src/                    # Source code
│   ├── __init__.py
│   ├── evaluate.py        # Evaluation wrapper
│   ├── inference.py       # Inference wrapper
│   └── README.md
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_setup.py      # Setup validation test
│   ├── test_eval.py       # Evaluation tests
│   └── README.md
├── SWE-bench/             # Git submodule
├── logs/                  # Evaluation logs (generated)
├── outputs/               # Model outputs (generated)
├── .venv/                 # Virtual environment
├── pyproject.toml         # Project configuration
├── setup.sh               # Setup script
└── readme.md             # This file
```

## 🚀 Setup

### Requirements
- Python 3.9+
- Docker Desktop (running)
- Git

### Quick Setup

```bash
# Clone with submodules
git clone --recursive https://github.com/VAR-META-Tech/SWE-bench-testsuite.git
cd SWE-bench-testsuite

# Run setup script
sh setup.sh

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

## 💻 Usage

### Run Evaluation

```bash
# Using the module
python -m src.evaluate

# Or import in your code
python -c "from src.evaluate import run_evaluation; run_evaluation()"
```

### Run Inference

```bash
# Using the module
python -m src.inference

# Or import in your code
python -c "from src.inference import run_inference; run_inference()"
```

### Run Tests

```bash
# Run all tests
pytest

# Run specific test with output
pytest tests/test_setup.py -v -s

# Run with coverage
pytest --cov=src tests/
```

### Validate Setup

```bash
# Quick setup validation test
pytest tests/test_setup.py -v
```

This will verify:
- ✅ Virtual environment is configured
- ✅ Dependencies are installed
- ✅ SWE-bench can load datasets
- ✅ Docker connection works
- ✅ Evaluation harness executes

## 📚 API Examples

### Custom Evaluation

```python
from src.evaluate import run_evaluation

run_evaluation(
    dataset_name="princeton-nlp/SWE-bench_Lite",
    predictions_path="outputs/predictions.jsonl",
    instance_ids=["sympy__sympy-20590", "django__django-11001"],
    max_workers=2,
    run_id="my-custom-eval",
    namespace="",  # Required on macOS Apple Silicon
    cache_level="env",
)
```

### Custom Inference

```python
from src.inference import run_inference

run_inference(
    model_name_or_path="princeton-nlp/SWE-Llama-13b",
    dataset_name="princeton-nlp/SWE-bench_Lite",
    max_instances=10,
    output_dir="outputs",
)
```

## 🔧 Configuration

### macOS Apple Silicon

On macOS with Apple Silicon, you **must** use `namespace=""`:

```python
run_evaluation(..., namespace="")
```

### Docker Image Caching

- `cache_level="env"`: Cache at environment level (recommended)
- `cache_level="instance"`: Cache at instance level (faster rebuilds)

## 📝 Notes

- **First Run**: Docker images will be built on-demand, which can take time
- **Test Behavior**: Setup tests may show instance "errors" due to missing images - this is expected
- **Docker**: Ensure Docker Desktop is running before evaluation

## 🐛 Troubleshooting

### "No module named 'pytest'"
```bash
source .venv/bin/activate
pip install pytest
```

### Docker Connection Errors
```bash
# Ensure Docker Desktop is running
docker ps
```

### Missing Images
```bash
# Build images manually
python -m swebench.harness.docker_build \
    --instances sympy__sympy-20590 \
    --namespace ""
```

## 📖 Documentation

- [Source Code Documentation](src/README.md)
- [Test Documentation](tests/README.md)
- [SWE-bench Official Docs](https://github.com/princeton-nlp/SWE-bench)

## 📄 License

See the [SWE-bench repository](https://github.com/princeton-nlp/SWE-bench) for license information.
