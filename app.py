import streamlit as st
import json
import pandas as pd

from datetime import datetime

# ✅ MUST BE FIRST Streamlit command
st.set_page_config(page_title="BizSim Alpha", layout="wide")

# ✅ Now safe to continue with logic
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
from utils.firebase_connector import save_user_game, log_session_data  # Firebase functions

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

# Set up results DataFrame for logging simulation data
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

# Firebase logging function
if "log_data" not in st.session_state:
    st.session_state["log_data"] = []

def log_current_session():
    current_state = dict(st.session_state)
    st.session_state["log_data"].append(current_state)
    log_session_data({
        "state": current_state,
        "results": st.session_state["results_df"].to_dict(orient="records")
    })

# Sidebar
with st.sidebar:
    st.title("🚀 BizSim")
    st.write("🧭 Page:", ss("page", "intro"))
    st.write("🎮 Mode:", ss("mode", "single"))
    st.write("🎭 Role:", ss("role", "unknown"))
    st.write("🏢 Company ID:", ss("company_id", "❓ Not set"))
    st.write("💰 Funding Done:", ss("funding_complete", False))
    if ss("page") != "intro":
        if st.button("🔙 Back to Lobby"):
            navigate("lobby")
    if st.button("♻️ Reset Session"):
        reset_session()
    if st.button("📝 Log Session Snapshot"):
        log_current_session()
        st.success("✅ Session state and results logged to Firebase")

    # View logged results
    if "results_df" in st.session_state and not st.session_state["results_df"].empty:
        with st.expander("📊 View Simulation Log"):
            st.dataframe(st.session_state["results_df"])

# Intro Page
if ss("page") == "intro":
    st.title("🚀 Welcome to BizSim")
    st.markdown("#### Build. Negotiate. Win. Choose your path as a startup CEO or investor.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎮 Launch Simulation"):
            navigate("lobby")
    with col2:
        if st.button("💾 Save Game"):
            save_user_game()
            log_current_session()
            st.success("✅ Game saved and session logged to Firebase")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))

# Routing
elif ss("page") == "lobby":
    if ss("mode") == "single" and not ss("role"):
        lobby.render_role_picker(navigate)
    elif ss("mode") == "single" and ss("role"):
        navigate("onboarding")
    else:
        lobby.render_lobby(navigate)

elif ss("page") == "onboarding":
    onboarding.render_onboarding(navigate)

elif ss("page") == "funding_round":
    funding_round.render_funding_ui(navigate)

elif ss("page") == "single_player":
    if not ss("funding_complete"):
        navigate("funding_round")
    elif ss("role") == "CEO":
        company_list.show_company_selection()
        ceo_dashboard.render_ceo_ui()
        ceo_decisions.render_decision_ui()
        staffing.render_staffing_ui()
        news_banner.render_news()
    elif ss("role") == "Investor":
        investor_view.render_investor_ui()
        news_banner.render_news()
    else:
        st.warning("Unknown role selected. Returning to lobby.")
        navigate("lobby")

elif ss("page") == "multiplayer":
    if ss("role") == "CEO":
        company_list.show_company_selection()
        ceo_dashboard.render_ceo_ui()
        funding_round.render_funding_ui(navigate)
        ceo_decisions.render_decision_ui()
        staffing.render_staffing_ui()
        news_banner.render_news()
    elif ss("role") == "Investor":
        investor_view.render_investor_ui()
        news_banner.render_news()
    else:
        st.warning("Please choose a role to continue.")
        lobby.render_role_picker(navigate)

else:
    st.error("Unknown page state. Resetting...")
    navigate("intro")
