
# ai-swebench-runner

This project runs SWE-bench inference and evaluation to benchmark AI models.

## Setup

Requirements:
- Python 3.10+
- Docker Desktop (running)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run inference (generate diffs)
```bash
python run_llama.py
```
Run evaluation (Docker)
```bash
python evaluate.py
```

Run tests
```bash
pytest test_eval.py
```# SWE-bench-testsuite
# SWE-bench-testsuite
