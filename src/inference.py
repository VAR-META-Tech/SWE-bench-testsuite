"""
LLaMA inference runner for SWE-bench.

This module provides utilities to run inference with LLaMA models
on SWE-bench datasets.
"""

from typing import Optional
import logging

logger = logging.getLogger(__name__)


def run_inference(
    model_name_or_path: str = "princeton-nlp/SWE-Llama-13b",
    dataset_name: str = "princeton-nlp/SWE-bench_Lite",
    max_instances: int = 1,
    output_dir: str = "outputs",
    split: str = "test",
    instance_ids: Optional[list[str]] = None,
    peft_path: Optional[str] = None,
    temperature: float = 0.2,
    top_p: float = 0.95,
    min_len: Optional[int] = None,
    max_len: Optional[int] = None,
) -> None:
    """
    Run inference with a LLaMA model on SWE-bench dataset.
    
    Args:
        model_name_or_path: HuggingFace model name or local path
        dataset_name: HuggingFace dataset name
        max_instances: Maximum number of instances to process
        output_dir: Directory for output files
        split: Dataset split to use ("test", "dev", etc.)
        instance_ids: Specific instance IDs to process (None for all)
        peft_path: Path to PEFT adapters (optional)
        temperature: Sampling temperature
        top_p: Nucleus sampling parameter
        min_len: Minimum generation length
        max_len: Maximum generation length
    
    Note:
        The instance_ids parameter is not directly supported by the underlying
        SWE-bench inference API. If you need to filter specific instances,
        you should prepare a custom dataset or filter the results after inference.
    """
    if instance_ids:
        logger.warning(
            "instance_ids parameter is not directly supported by run_llama. "
            "All instances will be processed. Consider filtering results after inference."
        )
    
    # Import here to avoid import errors if dependencies not available
    try:
        from swebench.inference.run_llama import main as swebench_llama_main
    except ImportError as e:
        raise ImportError(
            "Could not import swebench.inference.run_llama. "
            "Make sure SWE-bench is properly installed with inference dependencies."
        ) from e
    
    # Note: dataset_name maps to dataset_path in the actual function
    swebench_llama_main(
        model_name_or_path=model_name_or_path,
        dataset_path=dataset_name,  # This is the correct parameter name
        split=split,
        output_dir=output_dir,
        peft_path=peft_path,
        temperature=temperature,
        top_p=top_p,
        min_len=min_len,
        max_len=max_len,
        shard_id=None,
        num_shards=None,
    )


def main():
    """Run inference with default settings."""
    run_inference(
        model_name_or_path="princeton-nlp/SWE-Llama-13b",
        dataset_name="princeton-nlp/SWE-bench_Lite",
        max_instances=1,  # keep small for first run
        output_dir="outputs",
    )


if __name__ == "__main__":
    main()
