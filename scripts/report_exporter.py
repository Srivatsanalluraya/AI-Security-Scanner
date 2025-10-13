import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def export_reports(summary_path="reports/summary.txt",
                   json_path="reports/final_report.json",
                   output_pdf="reports/security_report.pdf",
                   output_md="reports/security_report.md"):
    os.makedirs("reports", exist_ok=True)
    print("📦 Exporting reports in multiple formats...")

    # Read summary
    with open(summary_path, "r") as f:
        summary = f.read()

    # Write Markdown
    with open(output_md, "w") as f:
        f.write("# 🛡️ Security Scan Report\n\n")
        f.write(summary)

    # Convert to PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    c.setFont("Helvetica", 12)
    c.drawString(50, 800, "Security Scan Report")
    text_obj = c.beginText(50, 780)
    for line in summary.split("\n"):
        text_obj.textLine(line)
    c.drawText(text_obj)
    c.save()

    print(f"✅ Reports exported successfully:\n - {output_md}\n - {output_pdf}")

if __name__ == "__main__":
    export_reports()
