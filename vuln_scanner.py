import requests

def check_security(url):
    results = []
    try:
        # Timeout 5 seconds taaki app hang na ho
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Check for X-Frame-Options (Clickjacking)
        if "X-Frame-Options" not in headers:
            results.append("[!] Risk: Clickjacking Vulnerability (X-Frame-Options missing)!")
        
        # Check for HSTS (SSL Security)
        if "Strict-Transport-Security" not in headers:
            results.append("[!] Risk: SSL/HSTS Header missing!")
            
        return results
    except Exception as e:
        return [f"Error: Connection failed ({str(e)})"]
