import json
import pandas as pd
from datetime import datetime

def generate_report(results):
    with open("logs/summary.json", "w") as f:
        json.dump(results, f, indent=4, default=str)  

    flat = []
    for r in results:
        row = {
            "query": r["request"].get("query"),
            "user_agent": r["request"].get("user_agent"),
            "threats": ", ".join(r["threats"]),
            "score": r["heuristic_score"],
            "ml": r["ml_detected"],
            "bot": r["bot"],
            "malicious": r["malicious"]
        }
        flat.append(row)

    df = pd.DataFrame(flat)
    df.to_csv("logs/summary.csv", index=False)
    df.to_excel("logs/summary.xlsx", index=False)
