# Source Code

This directory contains the main source code for the SWE-bench test suite.

## Modules

### `evaluate.py`
Wrapper for running SWE-bench evaluations with sensible defaults.

```python
from src.evaluate import run_evaluation

run_evaluation(
    dataset_name="princeton-nlp/SWE-bench_Lite",
    predictions_path="outputs/predictions.jsonl",
    max_workers=1,
    run_id="my-eval",
    namespace="",  # Required on macOS Apple Silicon
)
```

### `inference.py`
Wrapper for running LLaMA model inference on SWE-bench datasets.

```python
from src.inference import run_inference

run_inference(
    model_name_or_path="princeton-nlp/SWE-Llama-13b",
    dataset_name="princeton-nlp/SWE-bench_Lite",
    max_instances=10,
    output_dir="outputs",
)
```

## Usage

You can run the scripts directly:

```bash
# Run evaluation
python -m src.evaluate

# Run inference
python -m src.inference
```

Or import them in your own code:

```python
from src.evaluate import run_evaluation
from src.inference import run_inference
```
