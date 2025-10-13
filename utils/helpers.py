import json
import os
from datetime import datetime

def safe_load_json(path):
    """Safely load JSON file, return {} if missing or invalid."""
    if not os.path.exists(path):
        print(f"⚠️ File not found: {path}")
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"⚠️ Invalid JSON format in {path}")
        return {}

def save_json(data, path):
    """Write data as formatted JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"💾 Saved JSON to {path}")

def timestamp():
    """Return formatted timestamp string."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

def log_event(message):
    """Print log message with timestamp."""
    print(f"[{timestamp()}] {message}")

def normalize_text(text):
    """Clean up text (trim, remove extra spaces)."""
    return " ".join(text.split())

def extract_vulnerabilities(static_report):
    """
    Extract key vulnerability data from Bandit or other static scan JSON.
    Returns a list of normalized vulnerability dicts.
    """
    vulns = []
    if not static_report or "results" not in static_report:
        return vulns

    for issue in static_report["results"]:
        vuln = {
            "id": issue.get("test_id"),
            "description": issue.get("issue_text", "No description"),
            "severity": issue.get("issue_severity", "UNKNOWN"),
            "confidence": issue.get("issue_confidence", "UNKNOWN"),
            "location": issue.get("filename", ""),
            "line": issue.get("line_number", 0)
        }
        vulns.append(vuln)
    return vulns

if __name__ == "__main__":
    # Simple demo
    log_event("Helper utilities loaded successfully.")
    print(normalize_text("   This   is   a    test.   "))
