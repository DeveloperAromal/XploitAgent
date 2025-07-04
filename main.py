from tools.base.scraper import WebScraper
from tools.base.stack_finder import StackFinder
from tools.leaky_header_finder import monitor_network 
from tools.base.subdomain import SubFinder
from tools.nmap import run_basic_port_scan
from emailer.send_report import Send_email


import time
from colorama import Fore, Style


def typewriter(text, delay=0.0005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() 

ascii_art = r"""

 /$$   /$$           /$$           /$$   /$$      /$$$$$$                                  /$$          
| $$  / $$          | $$          |__/  | $$     /$$__  $$                                | $$          
|  $$/ $$/  /$$$$$$ | $$  /$$$$$$  /$$ /$$$$$$  | $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$        
 \  $$$$/  /$$__  $$| $$ /$$__  $$| $$|_  $$_/  | $$$$$$$$ /$$__  $$ /$$__  $$| $$__  $$|_  $$_/        
  >$$  $$ | $$  \ $$| $$| $$  \ $$| $$  | $$    | $$__  $$| $$  \ $$| $$$$$$$$| $$  \ $$  | $$          
 /$$/\  $$| $$  | $$| $$| $$  | $$| $$  | $$ /$$| $$  | $$| $$  | $$| $$_____/| $$  | $$  | $$ /$$      
| $$  \ $$| $$$$$$$/| $$|  $$$$$$/| $$  |  $$$$/| $$  | $$|  $$$$$$$|  $$$$$$$| $$  | $$  |  $$$$/      
|__/  |__/| $$____/ |__/ \______/ |__/   \___/  |__/  |__/ \____  $$ \_______/|__/  |__/   \___/        
          | $$                                             /$$  \ $$                                    
          | $$                                            |  $$$$$$/                                    
          |__/                                             \______/          
                                            Happy hacking                          
""" 
typewriter(Fore.CYAN + ascii_art + Style.RESET_ALL, delay=0.0005)

# SubFinder("https://www.ontraq.in/")

target = input("Enter the target website or IP (e.g., example.com): ")
result = run_basic_port_scan(target)

print("Scan Result:\n")
print(result)
Send_email(
    receiver_email="example@gmail.com",
    subject="Weekly Report",
    report_file_path="reporting/report_maker.py",
    app_email="geethaniya42@gmail.com",
    app_password="twpeheehhampadva"
)




    


# https://ontraq.in/dashboard
