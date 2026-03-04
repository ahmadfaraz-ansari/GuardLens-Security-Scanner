import requests
import threading
from queue import Queue
from colorama import Fore

# Configuration for Multi-Threading
NUM_THREADS = 50
q = Queue()

def scan_worker(target_url):
    """
    Worker function to process the subdomain queue.
    """
    while not q.empty():
        sub = q.get()
        url = f"http://{sub}.{target_url}"
        try:
            # Attempting to connect with a 2-second timeout
            res = requests.get(url, timeout=2)
            if res.status_code == 200:
                print(Fore.GREEN + f"[SUCCESS] Identified active subdomain: {url}")
        except requests.ConnectionError:
            # Silent ignore for failed connections
            pass
        except Exception:
            pass
        finally:
            q.task_done()

def find_subdomains(target_url):
    """
    Main function to initialize subdomain enumeration.
    """
    print(Fore.YELLOW + f"[*] Scan in progress: Performing subdomain enumeration for {target_url}...")
    
    try:
        # Loading wordlist into the processing queue
        with open("wordlist.txt", "r") as file:
            for line in file:
                sub = line.strip()
                if sub:
                    q.put(sub)
        
        # Initializing threads for concurrent execution
        for _ in range(NUM_THREADS):
            t = threading.Thread(target=scan_worker, args=(target_url,))
            t.daemon = True # Ensures threads exit when the main program terminates
            t.start()
            
        q.join() # Wait for the queue to be fully processed
        print(Fore.BLUE + "[+] Subdomain enumeration completed.")
        
    except FileNotFoundError:
        print(Fore.RED + "[!] Critical Error: 'wordlist.txt' not found in the project directory.")
    except Exception as e:
        print(Fore.RED + f"[!] An unexpected error occurred: {str(e)}")