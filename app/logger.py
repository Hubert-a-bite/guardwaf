from datetime import datetime
import json
import os

os.makedirs("logs", exist_ok=True)

def log_threat(analysis: dict):
    try:
        log_data = json.dumps(analysis, default=str)  
    except TypeError as e:
        print("Błąd serializacji JSON:", e)
        print("Dane:", analysis)
        return

    with open("logs/waf_alerts.log", "a") as log:
        log.write(f"[{datetime.now()}] {log_data}\n")
