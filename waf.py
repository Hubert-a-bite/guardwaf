from app.log_parser import parse_access_log, export_logs_to_csv, export_logs_to_excel
from app.core import WAFEngine
from app.logger import log_threat
from app.report import generate_report

entries = parse_access_log("data/access.log")
export_logs_to_csv(entries)
export_logs_to_excel(entries)

engine = WAFEngine()
results = []
for request in entries:
    result = engine.inspect(request)
    if result["malicious"]:
        log_threat(result)
    results.append(result)

generate_report(results)
print("Scanning completed.")
