import requests

def run_scan(url):
    vulnerabilities = []
    try:
        response = requests.get(url)
        if "X-Frame-Options" not in response.headers:
            vulnerabilities.append("Missing X-Frame-Options header (clickjacking vulnerability).")
        if "Content-Security-Policy" not in response.headers:
            vulnerabilities.append("Missing Content-Security-Policy header (XSS protection).")
    except Exception as e:
        vulnerabilities.append(f"Failed to access {url}: {e}")
    return vulnerabilities