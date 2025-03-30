import json
import os
from datetime import datetime
import streamlit as st

def log_decision(action: str, result: str):
    user_id = st.session_state.get("user_id", "anonymous")
    role = st.session_state.get("role", "unknown")
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "user": user_id,
        "role": role,
        "action": action,
        "result": result
    }

    log_path = f"data/logs/{user_id}.json"
    os.makedirs("data/logs", exist_ok=True)

    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(log_entry)

    with open(log_path, "w") as f:
        json.dump(logs, f, indent=2)