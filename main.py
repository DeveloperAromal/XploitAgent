<<<<<<< HEAD
=======
from tools.base.scraper import WebScraper
from tools.base.stack_finder import StackFinder
from tools.leaky_header_finder import monitor_network 
from tools.base.subdomain import SubFinder
from tools.nmap import run_basic_port_scan
from emailer.send_report import Send_email


>>>>>>> 3d59adc036083fd821e61c943d6607b1b2e7140f
import time
from colorama import Fore, Style
import sys
import io

from server.app import app


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
-----------------------------------------Happy hacking-------------------------------------------                          
""" 
# https://ontraq.in/dashboard <=== This is the test website

typewriter(Fore.CYAN + ascii_art + Style.RESET_ALL, delay=0.0005)




def main():
    app.run(debug=False)





main()



























<<<<<<< HEAD
=======
    


# https://ontraq.in/dashboard
>>>>>>> 3d59adc036083fd821e61c943d6607b1b2e7140f
