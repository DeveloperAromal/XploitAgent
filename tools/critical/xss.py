from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

s = requests.Session()
s.headers["User-Agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
)

def load_payloads():
    payload_file  = os.path.join("data", "xss_payloads.txt")
    with open(payload_file, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_forms(url):
    res = s.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        name = input_tag.attrs.get("name")
        if name:
            inputs.append({"type": input_type, "name": name})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

def submit_form(form_details, url, payload):
    target_url = urljoin(url, form_details["action"])
    data = {}

    for input in form_details["inputs"]:
        if input["type"] == "text" or input["type"] == "search":
            data[input["name"]] = payload
        else:
            data[input["name"]] = "test"

    if form_details["method"] == "post":
        res = s.post(target_url, data=data)
    else:
        res = s.get(target_url, params=data)

    return payload in res.text

def scan_xss(url):
    result = {
        "vulnerable": False,
        "details": [],
        "forms_found": 0
    }

    payloads = load_payloads()
    forms = get_forms(url)
    result["forms_found"] = len(forms)

    for form in forms:
        form_details = get_form_details(form)

        for payload in payloads:
            if submit_form(form_details, url, payload):
                result["vulnerable"] = True
                result["details"].append({
                    "form": form_details,
                    "payload": payload
                })
                break 

    return result

def scan_xss_batch(urls_dict):
    """
    Accepts: {"urls": [list_of_urls]}
    Returns: dict mapping url -> xss scan result
    """
    results = {}
    for url in urls_dict.get("urls", []):
        print(f"[✓] Scanning XSS for: {url}")
        results[url] = scan_xss(url)
    return results
