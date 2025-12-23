import json
from pathlib import Path

def test_evaluation_result_exists():
    path = Path("evaluation_results/eval/results.json")
    assert path.exists(), "Evaluation results not found. Did you run evaluate.py?"

def test_has_instances():
    data = json.loads(Path("evaluation_results/eval/results.json").read_text())
    assert data["submitted_instances"] > 0
