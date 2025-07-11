import requests
import os
from tools.base import scraper
from utils.log import logReport
from bs4 import BeautifulSoup
from colorama import Fore, Style


def crawl_web(target, endpoints):
    target = target.strip().rstrip('/')
    save_path = os.path.join("db", "endpoints.txt")

    for endpoint in endpoints:
        endpoint = endpoint.strip().lstrip('/')
        url = f"{target}/{endpoint}"
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print(f"[✓] Valid endpoint: {url}")
                print(f"{Fore.GREEN}[*] Scraping the web{Style.RESET_ALL}")
                
                soup = BeautifulSoup(response.text, "html.parser")

                with open(save_path, "a", encoding="utf-8") as f:
                    f.write(f"\n\n===== {url} =====\n")
                    f.write(soup.prettify() + "\n")

                logReport("[*] Process finished")   
                logReport("[*] Saved to endpoints.txt")     
                print(f"{Fore.GREEN}[*] Process finished{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}[*] Saved to endpoints.txt\n{Style.RESET_ALL}")
            else:
                print(f"[-] Invalid endpoint: {url} (Status: {response.status_code})")

        except Exception as e:
            print(f"[!] Error occurred while checking {url}: {e}")

def crawler(target):
    data_file = os.path.join("data", "api_list.txt")
    
    if not os.path.exists(data_file):
        print("[!] Endpoint list not found.")
        return

    with open(data_file, "r") as f:
        endpoints = [line.strip() for line in f if line.strip()]

    crawl_web(target, endpoints)
   