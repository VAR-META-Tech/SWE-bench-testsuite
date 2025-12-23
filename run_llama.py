from swebench.inference.run_llama import main

main(
    model_name_or_path="princeton-nlp/SWE-Llama-13b",
    dataset_name="princeton-nlp/SWE-bench_Lite",
    max_instances=1,        # keep small for first run
    output_dir="outputs",
)
