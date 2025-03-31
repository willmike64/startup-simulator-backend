# sim_state.py — now auto-syncs to Firebase after each round update

import json
from pathlib import Path
from launchpad_engine import offer_companies
from financial import update_financials
from firebase_connector import initialize_firebase, upload_company_state

state_file = Path("live_data.json")

def initialize_simulation():
    companies = offer_companies()
    for c in companies:
        c["Revenue"] = 0
        c["Burn"] = 0
        c["Profit"] = 0
        c["Morale"] = 70
        c["Customers"] = 0
        c["Cash"] = 150000
    data = {"round": 1, "companies": companies}
    with open(state_file, "w") as f:
        json.dump(data, f)
    return data

def load_simulation():
    if state_file.exists():
        with open(state_file, "r") as f:
            return json.load(f)
    return {}

def advance_and_update():
    data = load_simulation()
    data["round"] += 1
    db = initialize_firebase()
    updated = []
    for c in data["companies"]:
        updated_company = update_financials(c, data["round"])
        upload_company_state(db, updated_company["name"], updated_company)
        updated.append(updated_company)
    data["companies"] = updated
    with open(state_file, "w") as f:
        json.dump(data, f)
    return data["round"]