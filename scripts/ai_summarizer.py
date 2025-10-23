"""
AI Summarizer using Hugging Face Transformers
Generates a natural-language summary of the merged security scan report.
"""

import os
import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def generate_summary_hf(
    input_path="reports/final_report.json",
    output_path="reports/summary.txt",
    model_name="google/flan-t5-base"
):
    print("🤖 Generating AI-powered security summary using Hugging Face...")

    # Ensure input report exists
    if not os.path.exists(input_path):
        print(f"⚠️ No input report found at {input_path}. Exiting.")
        return

    # Load merged scan report
    with open(input_path, "r") as f:
        try:
            report_data = json.load(f)
        except json.JSONDecodeError:
            report_data = f.read()

    # Convert report to readable text
    report_text = json.dumps(report_data, indent=2) if isinstance(report_data, dict) else str(report_data)
    input_prompt = (
        "Summarize this software security scan report clearly for developers. "
        "Highlight vulnerabilities, their severity, and recommended fixes.\n\n"
        f"{report_text[:4000]}"  # keep within token limits
    )

    print(f"📦 Loading model: {model_name} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # Encode input
    inputs = tokenizer(input_prompt, return_tensors="pt", truncation=True, max_length=1024)

    # Generate summary
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=300,
        min_length=80,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Save summary
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(summary_text.strip())

    print(f"✅ Summary generated and saved to {output_path}\n")
    print("🧠 Summary Preview:")
    print("-" * 80)
    print(summary_text[:800])
    print("-" * 80)

if __name__ == "__main__":
    generate_summary_hf()
