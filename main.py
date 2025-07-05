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

