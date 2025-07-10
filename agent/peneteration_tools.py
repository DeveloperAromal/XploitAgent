# from pydantic import BaseModel, Field
# from langchain_core.tools import tool

# from tools.critical.leaky_header_finder import detect_leaky_headers_batch
# from tools.critical.port_scaner import port_scanner
# from tools.critical.sql_injector import sql_injection
# from tools.critical.xss import scan_xss


# # -----------------------
# # TOOL: ScanHeaders
# # -----------------------

# class ScanHeadersInput(BaseModel):
#     """Input for scanning leaky headers from multiple URLs."""
#     urls: list[str] = Field(..., description="List of URLs to scan for leaky headers")

# @tool
# def ScanHeaders(input: ScanHeadersInput) -> dict:
#     """Scan for leaky headers in the provided URLs."""
#     return detect_leaky_headers_batch({"urls": input.urls})


# # -----------------------
# # TOOL: Nmap
# # -----------------------

# class NmapInput(BaseModel):
#     """Input for port scanning a target domain or IP address."""
#     target: str = Field(..., description="Target domain or IP to scan")

# @tool
# def Nmap(input: NmapInput) -> str:
#     """Run Nmap scan on the target."""
#     cleaned_target = input.target.strip().removeprefix("http://").removeprefix("https://")
#     return port_scanner(cleaned_target)


# # -----------------------
# # TOOL: SqlInjection
# # -----------------------

# class SqlInjectionInput(BaseModel):
#     """Input for SQL injection testing."""
#     urls: list[str] = Field(..., description="List of URLs to test for SQL injection")

# @tool
# def SqlInjection(input: SqlInjectionInput) -> dict:
#     """Scan for SQL Injection vulnerabilities in the provided URLs."""
#     return sql_injection(input.urls)


# # -----------------------
# # TOOL: Xss
# # -----------------------

# class XssInput(BaseModel):
#     """Input for XSS vulnerability scanning."""
#     urls: list[str] = Field(..., description="List of URLs to scan for XSS")

# @tool
# def Xss(input: XssInput) -> dict:
#     """Scan for XSS vulnerabilities in the provided URLs."""
#     return scan_xss(input.urls)


# # -----------------------
# # TOOL LIST
# # -----------------------

# all_tools = [ScanHeaders, Nmap, SqlInjection, Xss]



from langchain_core.tools import tool
from tools.critical.leaky_header_finder import detect_leaky_headers_batch
from tools.critical.port_scaner import port_scanner
from tools.critical.sql_injector import sql_injection
from tools.critical.xss import scan_xss

# -----------------------
# TOOL: ScanHeaders
# -----------------------

@tool
def ScanHeaders(urls: list[str]) -> dict:
    """Scan for leaky headers in the provided URLs."""
    return detect_leaky_headers_batch({"urls": urls})


# -----------------------
# TOOL: Nmap
# -----------------------

@tool
def Nmap(target: str) -> str:
    """Run Nmap scan on the target domain or IP address."""
    return port_scanner(target.strip())


# -----------------------
# TOOL: SqlInjection
# -----------------------

@tool
def SqlInjection(urls: list[str]) -> dict:
    """Scan for SQL Injection vulnerabilities in the provided URLs."""
    return sql_injection(urls)


# -----------------------
# TOOL: Xss
# -----------------------

@tool
def Xss(urls: list[str]) -> dict:
    """Scan for XSS vulnerabilities in the provided URLs."""
    return scan_xss(urls)


# -----------------------
# TOOL LIST
# -----------------------

all_tools = [ScanHeaders, Nmap, SqlInjection, Xss]
