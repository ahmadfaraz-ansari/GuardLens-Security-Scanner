import requests
from colorama import Fore

def check_security(url):
    print(Fore.YELLOW + f"[*] Checking security headers for {url}...")
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        
        if 'X-Frame-Options' not in headers:
            print(Fore.RED + f"[!] Risk: Clickjacking Vulnerability (X-Frame-Options missing)!")
        if 'Strict-Transport-Security' not in headers:
            print(Fore.RED + f"[!] Risk: SSL/HSTS Header missing!")
        else:
            print(Fore.BLUE + f"[OK] Site has some security headers.")
    except:
        print(Fore.RED + "[!] Error connecting to site.")