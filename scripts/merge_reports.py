import json
import os

def merge_reports(dependency_path="reports/dependency_report.txt",
                  static_path="reports/static_report.json",
                  output_path="reports/final_report.json"):
    os.makedirs("reports", exist_ok=True)
    print("🔧 Merging scan reports...")

    data = {}

    # Load dependency scan text
    if os.path.exists(dependency_path):
        with open(dependency_path, "r") as f:
            data["dependency_report"] = f.read()
    else:
        data["dependency_report"] = "No dependency report found."

    # Load static scan JSON
    if os.path.exists(static_path):
        with open(static_path, "r") as f:
            try:
                data["static_report"] = json.load(f)
            except json.JSONDecodeError:
                data["static_report"] = {"error": "Invalid JSON in static report"}
    else:
        data["static_report"] = {"error": "No static report found."}

    # Write merged JSON
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ Reports merged successfully into {output_path}")

if __name__ == "__main__":
    merge_reports()
