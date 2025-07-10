from tools.base.scraper import WebScraper
from tools.base.stack_finder import StackFinder
from tools.base.subdomain import SubFinder
from tools.base.crawler import crawler
from tools.critical.port_scaner import port_scanner

def start_tools(target):
    
    tools_func = [
        # ("WebScraper", lambda: WebScraper(target)),
        # ("StackFinder", lambda: StackFinder()),
        # ("SubFinder", lambda: SubFinder(target)),
        # ("Crawler", lambda: crawler(target)),
        # ("Nmap", lambda: port_scanner(target))
    ]

    for name, func in tools_func:
        try:
            func()
            print("================================================")
        except Exception as e:
            print(f"[Error] ==> {name} : {e}")