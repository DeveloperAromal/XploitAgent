from tools.base.scraper import WebScraper
from tools.base.stack_finder import StackFinder
from tools.base.subdomain import SubFinder
from tools.critical.crawler import crawler
from tools.critical.sql_injector import sql_injection
from tools.critical.xss import scan_xss

# def start_tools(target):
#     tools = [WebScraper(target), StackFinder(), SubFinder(target)]
    
#     for tool in tools:
#         print(f"[DEBUG] Running tool: {tool.__class__.__name__}")
#         try:
#             tool.run()
#         except Exception as e:
#             print(f"[Error] {tools.__class__.__name__}: {e}")




def start_tools(target):
    
    tools_func = [
        # ("WebScraper", lambda: WebScraper(target)),
        # ("StackFinder", lambda: StackFinder()),
        # ("SubFinder", lambda: SubFinder(target)),
        # ("Crawler", lambda: crawler(target)),
        # ("SQL injector", lambda: sql_injection(target))
        
        ("XSS", lambda: scan_xss(target))
    ]

    for name, func in tools_func:
        try:
            func()
        except Exception as e:
            print(f"[Error] ==> {name} : {e}")