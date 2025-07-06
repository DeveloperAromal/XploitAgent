import time
from colorama import Fore, Style
import threading


from server.app import app
from agent.decision_maker import analyse_the_site

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



def run_server():
    app.run(debug=False, use_reloader=False)

server_thread = threading.Thread(target=run_server)
server_thread.daemon = True 
server_thread.start() 


print(Fore.YELLOW + "\n[+] Running LangChain analysis on base scan...\n" + Style.RESET_ALL)
response = analyse_the_site()  
print(Fore.GREEN + "\n[+] AI Analysis:\n" + Style.RESET_ALL)
print(response)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[+] Stopping server...")
