from flask import Flask, render_template, request
from scanner import run_scan
from report_generator import generate_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        scan_results = run_scan(url)
        pdf_path = generate_report(url, scan_results)
        return render_template("report.html", results=scan_results, pdf=pdf_path)
    return render_template("report.html", results=None, pdf=None)

if __name__ == "__main__":
    app.run(debug=True)