import subprocess
import os

def run_dependency_scan(output_path="reports/dependency_report.txt"):
    os.makedirs("reports", exist_ok=True)
    print("🔍 Running dependency vulnerability scan...")

    try:
        result = subprocess.run(
            ["safety", "check", "--full-report"],
            capture_output=True,
            text=True
        )
        with open(output_path, "w") as f:
            f.write(result.stdout)
        print(f"✅ Dependency scan completed. Results saved to {output_path}")
    except Exception as e:
        print(f"⚠️ Dependency scan failed: {e}")

if __name__ == "__main__":
    run_dependency_scan()
