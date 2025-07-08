import os
import json
from datetime import datetime


def logReport(log):
    timestamp = datetime.now().strftime("%d/%m/%y - %H:%M:%S")
    log_file = os.path.join("db", "log_file.ndjson")
    
    log_template = {
        "timestamp": timestamp,
        "log": log
    }
  
    with open(log_file, "w") as f:
        f.write(json.dumps(log_template) + "\n")
        
        
        