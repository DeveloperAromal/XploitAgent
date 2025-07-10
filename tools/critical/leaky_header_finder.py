from playwright.sync_api import sync_playwright
import os
import re

def detect_leaky_headers(headers):
    findings = []
    for key, value in headers.items():
        if "key" in key.lower() or "token" in key.lower():
            findings.append((key, value))
    return findings

def monitor_network(target_url: str):
    endpoints = set()
    leaked_headers = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        def handle_request(request):
            url = request.url
            if any(api in url.lower() for api in ["/api/", "/auth", "/user", "/admin"]):
                endpoints.add(url)

            for k, v in request.headers.items():
                if re.search(r"(key|token|auth)", k, re.IGNORECASE):
                    leaked_headers.append((k, v))

        page.on("request", handle_request)
        page.goto(target_url, wait_until="networkidle")

        browser.close()
    
    return {
        "leaked_headers": leaked_headers,
        "possible_endpoints": list(endpoints)
    }

def detect_leaky_headers_batch(urls_dict):
    """
    Accepts: {"urls": [list_of_urls]}
    Returns: dict mapping url -> findings dict
    """
    results = {}
    for url in urls_dict.get("urls", []):
        print(f"Scanning {url} for leaky headers...")
        results[url] = monitor_network(url)
    return results
