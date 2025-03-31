import json
import os
from datetime import datetime

RESULTS_DIR = "data/results"

def log_result(company_id, user_id, action, result, impact, source="system"):
    os.makedirs(RESULTS_DIR, exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "company_id": company_id,
        "user_id": user_id,
        "action": action,
        "result": result,
        "impact": impact,
        "source": source
    }
    path = os.path.join(RESULTS_DIR, f"{company_id}.json")
    history = []

    if os.path.exists(path):
        with open(path, "r") as f:
            history = json.load(f)

    history.append(entry)

    with open(path, "w") as f:
        json.dump(history, f, indent=2)

def load_valuation_history(company_id):
    path = os.path.join(RESULTS_DIR, f"{company_id}.json")
    if not os.path.exists(path):
        return []

    with open(path, "r") as f:
        data = json.load(f)
    return [e for e in data if "valuation" in e.get("impact", {})]