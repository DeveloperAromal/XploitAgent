import os
from datetime import datetime


def logReport(log):
    current = datetime.now().strftime("%d/%m/%y - %H:%M:%S")
    log_file = os.path.join("db", "log_file.txt")
    
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{current}    {log}\n")
