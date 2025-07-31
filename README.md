# Web Security Scanner

This is a simple web security scanner that checks for missing HTTP security headers and generates a PDF report.

## Features
- Scans a given URL for missing headers (X-Frame-Options, Content-Security-Policy).
- Generates a downloadable PDF report.
- Flask-based web interface.

## Usage
```bash
pip install -r requirements.txt
python app.py
```
Then visit http://localhost:5000 and enter the URL to scan.