from bs4 import BeautifulSoup
import requests
import os


def WebScraper(target): 
    save_path = os.path.join("db", "target_html.txt")
    
    target_req_html = requests.get(target).text
    soup = BeautifulSoup(target_req_html, "html.parser")
    pretty_soup = soup.prettify()
    
    
    with open(save_path, "w") as f:
        f.write(pretty_soup)
        