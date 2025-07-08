from scapy.all import IP, TCP, sr1
import socket

def syn_scan(target, port_range=(20, 100)):
    try:
        ip = socket.gethostbyname(target)
        print(f"\n[+] Scanning target: {target} ({ip})\n")
    except socket.gaierror:
        print("[!] Invalid domain or IP")
        return

    scanned_ports = set()

    for port in range(port_range[0], port_range[1] + 1):
        if port in scanned_ports:
            continue  # Avoid duplicate scan
        scanned_ports.add(port)

        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)

        if resp is None:
            continue
        elif resp.haslayer(TCP) and resp[TCP].flags == 0x12:
            print(f"[OPEN] Port {port}")
            # Send RST to reset connection
            sr1(IP(dst=ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)

if __name__ == "__main__":
    domain = input("Enter domain or IP to scan: ")
    syn_scan(domain, port_range=(20, 100))
