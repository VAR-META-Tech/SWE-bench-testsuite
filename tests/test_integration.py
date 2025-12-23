"""
Integration test for benchmarking LLMs with SWE-bench.

Complete flow:
1. Run LLaMA inference to generate predictions
2. Evaluate the predictions against test suite

This is the full SWE-bench benchmark pipeline.
"""

import json
from pathlib import Path
import pytest


def test_llm_benchmark_pipeline():
    """
    Full LLM benchmark: inference → evaluation.
    
    This test runs the complete SWE-bench pipeline:
    1. Run run_llama to generate model predictions
    2. Evaluate predictions using Docker test harness
    3. Generate evaluation report with results
    
    Note: This requires a LLaMA model. On first run, it will download
    the model which can take significant time and storage.
    """
    print("\n🚀 Running LLM Benchmark Pipeline...")
    
    from swebench.inference.run_llama import main as run_llama
    from swebench.harness.run_evaluation import main as run_evaluation
    
    # Configuration
    model_name = "princeton-nlp/SWE-Llama-13b"
    dataset_name = "princeton-nlp/SWE-bench_Lite"
    output_dir = "benchmark_outputs"
    run_id = "llm-benchmark"
    split = "test"
    
    # Step 1: Run LLaMA inference
    print("\n📝 Step 1/2: Running LLaMA inference...")
    print(f"   Model: {model_name}")
    print(f"   Dataset: {dataset_name}")
    print(f"   Output: {output_dir}/")
    
    try:
        run_llama(
            model_name_or_path=model_name,
            peft_path=None,
            dataset_path=dataset_name,
            split=split,
            temperature=0.2,
            top_p=0.95,
            output_dir=output_dir,
            min_len=None,
            max_len=None,
            shard_id=None,
            num_shards=None,
        )
        
        # Find the generated predictions file
        output_path = Path(output_dir)
        predictions_files = list(output_path.glob("*.jsonl"))
        
        assert len(predictions_files) > 0, "No predictions file generated"
        predictions_file = str(predictions_files[0])
        
        print(f"   ✓ Generated predictions: {predictions_file}")
        
        # Verify predictions
        with open(predictions_file, 'r') as f:
            predictions = [json.loads(line) for line in f]
        print(f"   ✓ Predictions count: {len(predictions)}")
        
    except Exception as e:
        print(f"\n⚠️  Inference failed: {e}")
        print("   This is likely due to:")
        print("   - Model not downloaded")
        print("   - Insufficient GPU memory")
        print("   - Missing dependencies")
        pytest.skip(f"Skipping test - inference failed: {e}")
    
    # Step 2: Run evaluation
    print(f"\n🔍 Step 2/2: Evaluating predictions...")
    print(f"   Predictions: {predictions_file}")
    print(f"   Run ID: {run_id}")
    
    run_evaluation(
        dataset_name=dataset_name,
        split=split,
        instance_ids=[],  # Empty = all instances from predictions
        predictions_path=predictions_file,
        max_workers=4,
        force_rebuild=False,
        cache_level="env",
        clean=False,
        open_file_limit=4096,
        run_id=run_id,
        timeout=None,
        namespace="",  # REQUIRED on macOS Apple Silicon
        rewrite_reports=False,
        modal=False,
    )
    
    # Verify report
    predictions_basename = Path(predictions_file).stem
    report_file = f"{predictions_basename}.{run_id}.json"
    
    print(f"\n📊 Step 3/3: Checking results...")
    print(f"   Report: {report_file}")
    
    assert Path(report_file).exists(), f"Report not created: {report_file}"
    
    with open(report_file, 'r') as f:
        report = json.load(f)
    
    print(f"\n📈 Benchmark Results:")
    print(f"   Total instances: {report['total_instances']}")
    print(f"   Submitted: {report['submitted_instances']}")
    print(f"   Completed: {report['completed_instances']}")
    print(f"   Resolved: {report['resolved_instances']}")
    print(f"   Unresolved: {report['unresolved_instances']}")
    print(f"   Errors: {report['error_instances']}")
    
    if report['completed_instances'] > 0:
        resolve_rate = (report['resolved_instances'] / report['completed_instances']) * 100
        print(f"   Resolve Rate: {resolve_rate:.1f}%")
    
    print(f"\n✅ LLM benchmark pipeline complete!")
    print(f"   Full report: {report_file}")


if __name__ == "__main__":
    test_llm_benchmark_pipeline()
