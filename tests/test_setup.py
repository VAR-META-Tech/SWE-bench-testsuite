"""
Test to verify SWE-bench setup is working correctly.

This test runs a simple evaluation on a single instance to ensure:
1. SWE-bench is properly installed
2. Docker is available and working
3. The evaluation harness can run successfully

Note: The test expects Docker images might not be built yet,
so an "error" in the instance is expected behavior on first run.
The test passes if the harness executes without import or connection errors.
"""

import sys
from pathlib import Path

import pytest

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from evaluate import run_evaluation


def test_swebench_evaluation_setup():
    """
    Test that SWE-bench evaluation can run successfully on a single instance.
    
    This uses the 'gold' predictions path which tests against the ground truth patches.
    Running on sympy__sympy-20590 as a smoke test.
    
    This test validates:
    - Virtual environment is properly configured
    - All dependencies are installed correctly
    - SWE-bench package imports work
    - Docker connection is available
    - Dataset can be loaded from HuggingFace
    - Evaluation harness can execute
    
    Expected behavior on first run:
    - Dataset downloads successfully
    - Evaluation harness starts
    - Instance may show "error" due to missing Docker images
    - Test still passes (validates setup, not full evaluation)
    """
    print("\n🚀 Running SWE-bench evaluation setup test...")
    
    # Run the evaluation using our wrapper
    run_evaluation(
        dataset_name="princeton-nlp/SWE-bench_Lite",
        split="test",
        instance_ids=["sympy__sympy-20590"],
        predictions_path="gold",
        max_workers=1,
        force_rebuild=False,
        cache_level="env",
        clean=False,
        open_file_limit=4096,
        run_id="validate-gold",
        timeout=None,
        namespace="", 
        rewrite_reports=False,
        modal=False,
    )
    
    print("\n✅ SWE-bench evaluation setup test passed!")
    print("Note: Instance 'errors' due to missing Docker images are expected on first run.")
    print("To build images, run: python -m swebench.harness.docker_build --instances <id> --namespace ''")


if __name__ == "__main__":
    # Allow running directly with: python -m tests.test_setup
    test_swebench_evaluation_setup()
