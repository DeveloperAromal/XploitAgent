from playwright.sync_api import sync_playwright
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
        "api_endpoints": list(endpoints),
        "leaked_headers": leaked_headers
    }


if __name__ == "__main__":
    target_url = "https://futuretechies.vercel.app"  # Replace with the target URL
    results = monitor_network(target_url)

    print("API Endpoints:")
    for endpoint in results["api_endpoints"]:
        print(endpoint)

    print("\nLeaked Headers:")
    for header, value in results["leaked_headers"]:
        print(f"{header}: {value}")



