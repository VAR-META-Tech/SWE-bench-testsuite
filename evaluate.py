from swebench.harness.run_evaluation import main

main(
    dataset_name="princeton-nlp/SWE-bench_Lite",
    predictions_path="outputs/predictions.jsonl",
    max_workers=1,
    run_id="eval",
    namespace="",           # REQUIRED on macOS Apple Silicon
    cache_level="env",
)
