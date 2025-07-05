import os
import requests 
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from colorama import Fore, Style
from utils.log import logReport

tries_lock = threading.Lock()
tries = 0

def checkDomain(target, subdomain):
    global tries
    
    url = f"https://{subdomain}.{target}"
        
    try:
        requests.get(url, timeout=3)
        
        with tries_lock:
            tries += 1
            logReport(f"[*] Found {url}")    
            print(f"[*] Found {url}")
            logReport(f"[*] {tries} valid urls found...")    
            print(f"[*] {tries} valid urls found...")   
        return url
    
    except requests.ConnectionError:
        return None
    
    except requests.RequestException:
        return None

def Scanner(domain_name, subdomain_list):
    save_file = os.path.join("db", "valid_subdomains.txt")
    domain = domain_name.replace("https://", "").replace("www.", "")
    valid_subdomain = []
   
    with ThreadPoolExecutor(max_workers=200) as e:
        future = [e.submit(checkDomain, domain, subdomain) for subdomain in subdomain_list]
    
    
        for future in as_completed(future):
            result = future.result()
            if result:
                valid_subdomain.append(result)
                
                
    if valid_subdomain:
        with open(save_file, "w") as f:
            f.write('\n'.join(valid_subdomain))
        
        
def SubFinder(target):
    
    data_path = os.path.join("data", "subdomain_small_list.txt")
    
    with open(data_path, "r") as f:
        subdomains = f.read().splitlines()
        logReport(f"[+] Scaning {len(subdomains)} subdomains in {target}....")    
        print(f"{Fore.GREEN}[+] Scaning {len(subdomains)} subdomains in {target}....{Style.RESET_ALL}")
        
        Scanner(target, subdomains)



        
    