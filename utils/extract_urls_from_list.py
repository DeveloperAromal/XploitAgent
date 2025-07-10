import re

def extract_urls_from_text(text):
    return re.findall(r"https?://[^\s)>\]]+", text)
