import os 
from bs4 import BeautifulSoup
from colorama import Fore, Style
from utils.log import logReport

def StackFinder():
    logReport("[*] Looking for the stack details")    
    print(f"{Fore.GREEN}[*] Looking for the stack details\n{Style.RESET_ALL}")
    load_data = os.path.join("db", "target_html.txt")
    save_path = os.path.join("db", "target_stack_data.txt")
    
    script_data = []
        
    with open(load_data, "r", encoding="utf-8") as f:
        data = f.read()
        
        soup = BeautifulSoup(data, "html.parser")
    
        script_tags = soup.find_all("script")
        
        for tag in script_tags:
            
            src = tag.get("src")
            
            if src:
                script_data.append(tag["src"])
                
              
                if "next" in src.lower():
                    presence = "Presence of Next js found on target"
                
        with open(save_path, "w") as f:
            logReport("[*] Process finished")  
            logReport("[*] Saving the file")      
            print(f"{Fore.GREEN}[*] Process finished{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}[*] Saving the file\n\n{Style.RESET_ALL}")
            f.write(presence)
        
