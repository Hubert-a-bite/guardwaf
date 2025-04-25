import re
from app.log_type_detector import detect_log_type
import csv
import pandas as pd

log_patterns = {
    "nginx": re.compile(r'(?P<ip>[\d.]+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<path>[^ ]+) HTTP.*" (?P<status>\d+) \d+ ".*?" "(?P<ua>[^"]+)"'),
    "apache": re.compile(r'(?P<ip>[\d.]+) - \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\w+) (?P<path>[^ ]+) HTTP.*" (?P<status>\d+) \d+ ".*?" "(?P<ua>[^"]+)"')
}

def parse_access_log(filepath: str, force_type: str = None) -> list:
    entries = []
    with open(filepath, "r", encoding="utf-8") as f:
        first_line = f.readline()
        f.seek(0)
        log_type = force_type or detect_log_type(first_line)
        pattern = log_patterns.get(log_type)

        if not pattern:
            raise ValueError("Unknown logo type")

        for line in f:
            match = pattern.search(line)
            if match:
                entries.append({
                    "ip": match["ip"],
                    "datetime": match["datetime"],
                    "method": match["method"],
                    "query": match["path"],
                    "user_agent": match["ua"]
                })
    return entries

def export_logs_to_csv(entries, filename="logs/nginx_analysis.csv"):
    keys = entries[0].keys()
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(entries)

def export_logs_to_excel(entries, filename="logs/nginx_analysis.xlsx"):
    df = pd.DataFrame(entries)
    df.to_excel(filename, index=False)
