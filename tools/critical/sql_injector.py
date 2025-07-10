from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

s = requests.Session()
s.headers["User-Agent"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
)

with open(os.path.join("data", "sql_payload.txt"), "r") as f:
    payloads = f.read().splitlines()

def get_forms(url):
    res = s.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return soup.find_all("form")

def get_form_value(form):
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []

    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")

        if input_name:
            inputs.append({
                "type": input_type,
                "name": input_name,
                "value": input_value
            })

    return {
        "action": action,
        "method": method,
        "inputs": inputs
    }

def vulnerable(response):
    errors = {
        "quoted string not properly terminated",
        "unclosed quotation mark after the character string",
        "you have an error in your sql syntax",
        "warning: mysql",
        "mysql_fetch",
        "syntax error",
        "ora-01756",
        "unterminated quoted string",
    }
    content = response.content.decode(errors="ignore").lower()
    for error in errors:
        if error in content:
            return True
    return False

def sql_injection(url):
    """
    Runs SQL Injection test on a single URL.
    Returns True if vulnerable, False otherwise.
    """
    forms = get_forms(url)
    if not forms:
        return {"vulnerable": False, "message": "No forms found"}

    for form in forms:
        details = get_form_value(form)
        target_url = urljoin(url, details["action"])

        for payload in payloads:
            data = {}
            for input_tag in details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:
                    data[input_tag["name"]] = input_tag["value"] + payload
                elif input_tag["type"] != "submit":
                    data[input_tag["name"]] = payload

            try:
                if details["method"] == "post":
                    res = s.post(target_url, data=data, timeout=10)
                else:
                    res = s.get(target_url, params=data, timeout=10)

                if vulnerable(res):
                    return {"vulnerable": True, "payload": payload, "target": target_url}
            except Exception as e:
                return {"vulnerable": False, "error": str(e)}

    return {"vulnerable": False, "message": "No SQL Injection found"}

def sql_injection_batch(urls_dict):
    """
    Accepts: {"urls": [list_of_urls]}
    Returns: dict mapping url -> sql injection result dict
    """
    results = {}
    for url in urls_dict.get("urls", []):
        print(f"Scanning URL: {url}")
        results[url] = sql_injection(url)
    return results
