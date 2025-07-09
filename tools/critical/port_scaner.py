import nmap
import os
from urllib.parse import urlparse


def port_scanner(target):
    
    parse = urlparse(target)
    target = parse.netloc if parse.netloc else parse.path
    target = target.replace("https://", "").replace("http://", "").strip()
    print("[!] Nmap started......")
    port_data = os.path.join("data", "ports.txt")
    
    with open(port_data, "r") as f:
        port_list = f.read().splitlines()
        port = ",".join(port_list)

    nm = nmap.PortScanner()
    
    try:
        nm.scan(target, port, arguments="-sS -T4")
        
        for host in nm.all_hosts():
            print(f"{host} -- {nm[host].hostname()}")
            print(f"State -- {nm[host].state()}")
            
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                
                
                for port in sorted(lport):
                    state = nm[host][proto][port]['state']
                    print(f"{port}/{proto} --- {state}")
                
            
    except Exception as e:
        print(e)
        
