from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os


s = requests.Session()
s.headers["User-Agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
)


def get_input(target):
    soup = BeautifulSoup(requests.get(target), "html.parser")
    
    return soup

    
    