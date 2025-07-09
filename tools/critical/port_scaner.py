import nmap

def run_nmap_scan(target, port_range='1-1000'):
    scanner = nmap.PortScanner()

    print(f"\n[+] Scanning {target} on ports {port_range}...\n")

    # -sV = version detection
    scanner.scan(hosts=target, ports=port_range, arguments='-sV')

    for host in scanner.all_hosts():
        print(f"Host: {host} ({scanner[host].hostname()})")
        print(f"State: {scanner[host].state()}\n")

        for proto in scanner[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                service = scanner[host][proto][port]
                print(f"  Port {port}: {service['state']} - {service.get('name', '')} ({service.get('product', '')} {service.get('version', '')})")
            print()

if __name__ == "__main__":
    domain = input("Enter target IP or domain: ")
    run_nmap_scan(domain, port_range="20-1000")

# vidyatcklmr.ac.in