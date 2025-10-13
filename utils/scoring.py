import random

# Basic severity categories
SEVERITY_LEVELS = {
    "critical": (9.0, 10.0),
    "high": (7.0, 8.9),
    "medium": (4.0, 6.9),
    "low": (0.1, 3.9)
}

def classify_severity(score):
    """Map numeric CVSS-like score to severity label."""
    for level, (low, high) in SEVERITY_LEVELS.items():
        if low <= score <= high:
            return level
    return "unknown"

def calculate_priority(vulnerability):
    """
    Estimate priority based on:
      - CVSS score (if given)
      - EPSS (Exploit Prediction Scoring System)
      - Simple AI reasoning fallback (if missing)
    """
    score = 0.0
    cvss = vulnerability.get("cvss_score")
    epss = vulnerability.get("epss_score")

    if cvss:
        score = cvss
    elif epss:
        score = epss * 10
    else:
        # Random fallback (in a real system you'd use an ML or AI inference)
        score = random.uniform(2.0, 8.5)

    severity = classify_severity(score)
    return {
        "score": round(score, 2),
        "severity": severity,
        "priority": f"{severity.upper()} ({score})"
    }

def prioritize_vulnerabilities(vulnerabilities):
    """
    Sort vulnerabilities list by severity and score.
    Expected input: List of dicts with `cvss_score` or `epss_score` fields.
    """
    prioritized = []
    for vuln in vulnerabilities:
        priority_data = calculate_priority(vuln)
        vuln.update(priority_data)
        prioritized.append(vuln)

    # Sort descending by score
    prioritized.sort(key=lambda v: v.get("score", 0), reverse=True)
    return prioritized

if __name__ == "__main__":
    # Example usage
    test_data = [
        {"id": "CVE-1234", "cvss_score": 8.2},
        {"id": "CVE-5678", "epss_score": 0.6},
        {"id": "CVE-9101"},
    ]
    prioritized = prioritize_vulnerabilities(test_data)
    for item in prioritized:
        print(item)
