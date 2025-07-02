import threading
from concurrent.futures import ThreadPoolExecutor
import os
import requests




def subdomainFinder(target, subdomain):
    
    valid_subdomains = []
    main_domain = target.removeprefix("https://")
    
    url = f"{subdomain}.{main_domain}"

    try:
        res = requests.get(url)
        print(res.status_code())
        if res.status_code(200):
            valid_subdomains.append(subdomain)
        
    except:
        return subdomain       





    
