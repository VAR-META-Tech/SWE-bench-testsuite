# Tests

This directory contains all test files for the SWE-bench test suite.

## Running Tests

Run all tests:
```bash
pytest
```

Run specific test file:
```bash
pytest tests/test_setup.py -v
pytest tests/test_integration.py -v
```

Run with output visible:
```bash
pytest tests/test_setup.py -v -s
```

## Test Files

### `test_setup.py`
Validates that the SWE-bench environment is properly configured.

This test:
- Verifies all dependencies are installed
- Checks Docker connectivity
- Validates SWE-bench can load datasets
- Ensures the evaluation harness can run

**Note**: On first run, instances may show "errors" due to missing Docker images. This is expected behavior. The test validates setup, not full evaluation.

**Run it:**
```bash
pytest tests/test_setup.py -v -s
```

### `test_integration.py`
Full LLM benchmark pipeline test: inference → evaluation.

This test runs the complete workflow:
1. **Run LLaMA inference** to generate predictions
2. **Evaluate predictions** using Docker test harness
3. **Generate report** with benchmark results

**Requirements:**
- LLaMA model (will download on first run - ~26GB)
- GPU recommended (CPU is very slow)
- Docker running
- Significant time (minutes to hours depending on dataset size)

**Run it:**
```bash
# Full pipeline
pytest tests/test_integration.py -v -s

# Or run directly
python tests/test_integration.py
```

**What it does:**
- Runs `run_llama` to generate model predictions
- Saves predictions to `benchmark_outputs/*.jsonl`
- Runs evaluation on the predictions
- Creates report: `<predictions>.llm-benchmark.json`
- Shows resolve rate and benchmark metrics

### `test_eval.py`
Additional evaluation tests (if any).

## Test Requirements

- Virtual environment must be activated
- Docker must be running
- Internet connection for downloading datasets
- On macOS Apple Silicon: `namespace=""` parameter required
- For integration tests: GPU and model storage

## Expected Behavior

### Setup Test (`test_setup.py`)
✅ **Pass**: Validates environment and dependencies  
⚠️ **Instance errors**: Expected on first run (missing Docker images)

### Integration Test (`test_integration.py`)
⏱️ **Long running**: Can take minutes to hours
💾 **Storage**: Model downloads ~26GB
🔥 **GPU**: Recommended for inference
✅ **Pass**: Completes full pipeline and generates report
