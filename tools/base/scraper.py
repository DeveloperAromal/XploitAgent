from bs4 import BeautifulSoup
import requests
import os
from colorama import Fore, Style
from utils.log import logReport


def WebScraper(target):
    logReport("[*] Scraping the web")     
    print(f"{Fore.GREEN}[*] Scraping the web{Style.RESET_ALL}")
    save_path = os.path.join("db", "target_html.txt")
    
    target_req_html = requests.get(target).text
    soup = BeautifulSoup(target_req_html, "html.parser")
    pretty_soup = soup.prettify()
    
    with open(save_path, "w") as f:
        logReport("[*] Process finished")   
        logReport("[*] Saving the file")     
        print(f"{Fore.GREEN}[*] Process finished{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[*] Saving the file\n\n{Style.RESET_ALL}")
        f.write(pretty_soup)