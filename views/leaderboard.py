import streamlit as st
import os
import json

def render_leaderboard():
    st.title("🏆 Valuation Leaderboard")

    results_dir = "data/results"
    rows = []

    for file in os.listdir(results_dir):
        if file.endswith(".json"):
            path = os.path.join(results_dir, file)
            with open(path, "r") as f:
                data = json.load(f)
                if data:
                    last = data[-1]
                    val = last.get("impact", {}).get("valuation")
                    if val:
                        rows.append((last["company_id"], val))

    if rows:
        sorted_rows = sorted(rows, key=lambda x: x[1], reverse=True)
        st.table([{"Company": r[0], "Valuation": f"${r[1]:,}"} for r in sorted_rows])
    else:
        st.info("No valuation data logged yet.")