import streamlit as st
import json
import pandas as pd
from datetime import datetime

from utils.session import init_session_state
from views import (
    company_list,
    ceo_dashboard,
    ceo_decisions,
    funding_round,
    founder_dashboard as investor_view,
    generate_companies as company_generator,
    lobby,
    onboarding,
    staffing
)
from components import stock_ticker_banner as news_banner
# from utils.firebase_connector import save_user_game, log_session_data
import admin_ui

init_session_state()

# Optional clean helper for session state access
def ss(key, default=None):
    return st.session_state[key] if key in st.session_state else default

def navigate(page):
    st.session_state["page"] = page
    st.rerun()

def reset_session():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

def init_results_df():
    if "results_df" not in st.session_state:
        st.session_state["results_df"] = pd.DataFrame(columns=["timestamp", "company_id", "event", "value"])

def log_event(event_name, value):
    init_results_df()
    new_row = {
        "timestamp": datetime.now().isoformat(),
        "company_id": ss("company_id", "unknown"),
        "event": event_name,
        "value": value
    }
    st.session_state["results_df"] = pd.concat([
        st.session_state["results_df"],
        pd.DataFrame([new_row])
    ], ignore_index=True)

if "log_data" not in st.session_state:
    st.session_state["log_data"] = []

def log_current_session():
    current_state = dict(st.session_state)
    st.session_state["log_data"].append(current_state)
    # log_session_data({
    #     "state": current_state,
    #     "results": st.session_state["results_df"].to_dict(orient="records")
    # })

# 🚨 Force launch to Admin Panel
st.info("🧑‍💼 Admin mode forced — displaying Admin UI")
admin_ui
st.stop()