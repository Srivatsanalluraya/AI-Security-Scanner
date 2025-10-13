import os
import json
from openai import OpenAI

def generate_summary(input_path="reports/final_report.json", output_path="reports/summary.txt"):
    print("🤖 Generating AI-powered security summary...")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("❌ Missing OPENAI_API_KEY in environment variables.")

    client = OpenAI(api_key=api_key)

    with open(input_path, "r") as f:
        report_data = f.read()

    prompt = f"""
You are a security assistant. Analyze this scan report and summarize the findings 
for developers in clear, human-readable language. Include:
- Vulnerability type
- Severity (if possible)
- A short explanation
- Recommended fix or mitigation

Report Data:
{report_data}
"""

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response.choices[0].message.content.strip()

    os.makedirs("reports", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(summary)

    print(f"✅ AI summary generated and saved to {output_path}")

if __name__ == "__main__":
    generate_summary()
