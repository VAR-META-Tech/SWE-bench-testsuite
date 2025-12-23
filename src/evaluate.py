"""
Evaluation runner for SWE-bench.

This module provides utilities to run SWE-bench evaluations
with sensible defaults for macOS and other platforms.
"""

from typing import Optional
from pathlib import Path
from swebench.harness.run_evaluation import main as swebench_main


def run_evaluation(
    dataset_name: str = "princeton-nlp/SWE-bench_Lite",
    predictions_path: str = "outputs/predictions.jsonl",
    max_workers: int = 1,
    run_id: str = "eval",
    namespace: str = "",
    cache_level: str = "env",
    split: str = "test",
    instance_ids: Optional[list[str]] = None,
    force_rebuild: bool = False,
    clean: bool = False,
    open_file_limit: int = 4096,
    timeout: Optional[int] = None,
    rewrite_reports: bool = False,
    modal: bool = False,
    report_dir: str = ".",
) -> None:
    """
    Run SWE-bench evaluation with sensible defaults.
    
    Args:
        dataset_name: HuggingFace dataset name
        predictions_path: Path to predictions file or "gold" for ground truth
        max_workers: Number of parallel workers
        run_id: Identifier for this evaluation run
        namespace: Docker namespace (empty string required for macOS Apple Silicon)
        cache_level: Cache level for Docker images ("env" or "instance")
        split: Dataset split to use ("test", "dev", etc.)
        instance_ids: Specific instance IDs to evaluate (None for all)
        force_rebuild: Force rebuild of Docker images
        clean: Clean up images after evaluation
        open_file_limit: Maximum number of open files
        timeout: Timeout for evaluation in seconds
        rewrite_reports: Rewrite existing reports
        modal: Use Modal for remote execution
        report_dir: Directory for output reports
    """
    swebench_main(
        dataset_name=dataset_name,
        split=split,
        instance_ids=instance_ids or [],
        predictions_path=predictions_path,
        max_workers=max_workers,
        force_rebuild=force_rebuild,
        cache_level=cache_level,
        clean=clean,
        open_file_limit=open_file_limit,
        run_id=run_id,
        timeout=timeout,
        namespace=namespace,
        rewrite_reports=rewrite_reports,
        modal=modal,
        report_dir=report_dir,
    )


def main():
    """Run evaluation with default settings."""
    run_evaluation(
        dataset_name="princeton-nlp/SWE-bench_Lite",
        predictions_path="outputs/predictions.jsonl",
        max_workers=1,
        run_id="eval",
        namespace="",  # REQUIRED on macOS Apple Silicon
        cache_level="env",
    )


if __name__ == "__main__":
    main()
