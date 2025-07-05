import subprocess

def run_command_in_popup(cmd: str):
    # It's generally better to get the current working directory dynamically
    # than hardcoding a user path. However, if the intent is to always
    # start in a specific known path, the original approach is fine for that specific use case.
    # For robust scripting, consider: import os; current_dir = os.getcwd()
    POWERSHELL_PROMPT = r"C:\Users\aroma" # Changed to a directory path

    """
    Run the given command in a new pop-up PowerShell window (Windows only).
    The window stays open after execution to let user see the output.
    """
    # Using 'start powershell' is correct for opening a new window.
    # -NoExit keeps the window open.
    # -Command allows you to pass a command string.
    # It's important to properly escape quotes within the command string.
    powershell_cmd = (
        f'start powershell -NoExit -Command "cd \\"{POWERSHELL_PROMPT}\\" ; {cmd}"'
    )
    subprocess.Popen(powershell_cmd, shell=True)

def run_basic_port_scan(target: str):
    """Scan all TCP ports (1–65535) on the target."""
    cmd = f"nmap -Pn -p- {target}"
    run_command_in_popup(cmd)

def run_service_version_scan(target: str):
    """Detect services and versions running on open ports."""
    cmd = f"nmap -sV {target}"
    run_command_in_popup(cmd)

def run_os_detection_scan(target: str):
    """Attempt to detect the operating system."""
    cmd = f"nmap -O {target}"
    run_command_in_popup(cmd)

def run_aggressive_scan(target: str):
    """Aggressive scan: OS detection, version detection, script scanning, and traceroute."""
    cmd = f"nmap -A {target}"
    run_command_in_popup(cmd)

def run_vuln_script_scan(target: str):
    """Use NSE to scan for known vulnerabilities (CVEs)."""
    cmd = f"nmap --script vuln {target}"
    run_command_in_popup(cmd)

def run_http_enum_scan(target: str):
    """Enumerate directories and web technologies on ports 80 and 443."""
    cmd = f"nmap -p 80,443 --script http-enum {target}"
    run_command_in_popup(cmd)

def run_smb_vuln_scan(target: str):
    """Check for SMB-related vulnerabilities (e.g., EternalBlue)."""
    cmd = f"nmap -p 445 --script smb-vuln* {target}"
    run_command_in_popup(cmd)

def run_ssl_cert_scan(target: str):
    """Scan for SSL certificate info and supported cipher suites."""
    cmd = f"nmap -p 443 --script ssl-cert,ssl-enum-ciphers {target}"
    run_command_in_popup(cmd)

def run_dns_brute_scan(target: str):
    """Brute-force DNS subdomains (requires open port 53)."""
    cmd = f"nmap -p 53 --script dns-brute {target}"
    run_command_in_popup(cmd)

def run_ftp_check(target: str):
    """Check for anonymous FTP login and bounce attacks."""
    cmd = f"nmap -p 21 --script ftp-anon,ftp-bounce {target}"
    run_command_in_popup(cmd)

def run_custom_ports_scan(target: str, ports: str):
    """Scan a custom list of ports (comma-separated)."""
    cmd = f"nmap -Pn -p {ports} {target}"
    run_command_in_popup(cmd)

def run_custom_script_scan(target: str, scripts: str):
    """Run specific NSE scripts (comma-separated)."""
    cmd = f"nmap --script {scripts} {target}"
    run_command_in_popup(cmd)