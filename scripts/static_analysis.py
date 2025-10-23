import subprocess
import os

def run_static_scan(target_dir=".", output_path="reports/static_report.json"):
    os.makedirs("reports", exist_ok=True)
    print("🔎 Running static code analysis...")

    try:
        result = subprocess.run(
            ["bandit", "-r", target_dir, "-f", "json", "-o", output_path],
            capture_output=True,
            text=True
        )
        print(f"✅ Static code analysis completed. Results saved to {output_path}")
    except Exception as e:
        print(f"⚠️ Static scan failed: {e}")

if __name__ == "__main__":
    run_static_scan()
