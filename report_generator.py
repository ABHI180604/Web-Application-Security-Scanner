from fpdf import FPDF
from pathlib import Path

def generate_report(url, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Security Report for {url}", ln=True)
    pdf.ln(10)
    for item in results:
        pdf.multi_cell(0, 10, item)
    report_path = Path("report_pdf") / "report.pdf"
    pdf.output(report_path)
    return report_path