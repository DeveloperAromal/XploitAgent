import nmap
import os
from urllib.parse import urlparse

def port_scanner(target: str) -> str:
    parse = urlparse(target)
    target = parse.netloc if parse.netloc else parse.path
    target = target.replace("https://", "").replace("http://", "").strip()

    print("[!] Nmap started......")
    
    port_data = os.path.join("data", "ports.txt")
    
    with open(port_data, "r") as f:
        port_list = f.read().splitlines()
        port = ",".join(port_list)

    nm = nmap.PortScanner()
    output = []

    try:
        nm.scan(target, port, arguments="-sS -T4")
        
        for host in nm.all_hosts():
            output.append(f"\nHost: {host}")
            output.append(f"Hostname: {nm[host].hostname()}")
            output.append(f"State: {nm[host].state()}")
            
            for proto in nm[host].all_protocols():
                output.append(f"\nProtocol: {proto}")
                lport = nm[host][proto].keys()

                for p in sorted(lport):
                    state = nm[host][proto][p]['state']
                    output.append(f"Port {p}/{proto}: {state}")
        
        return "\n".join(output)

    except Exception as e:
        return f"[ERROR] Nmap failed: {str(e)}"
