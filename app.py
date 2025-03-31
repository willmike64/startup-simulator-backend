import streamlit as st

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
# from utils.firebase_connector import save_user_game  # Optional if not ready

init_session_state()

def navigate(page):
    st.session_state.page = page
    st.rerun()

# Sidebar
with st.sidebar:
    st.title("🚀 BizSim")
    st.write("🧭 Page:", st.session_state.get("page", "intro"))
    st.write("🎮 Mode:", st.session_state.get("mode", "single"))
    st.write("🎭 Role:", st.session_state.get("role", "unknown"))
    st.write("🏢 Company ID:", st.session_state.get("company_id", "❓ Not set"))
    st.write("💰 Funding Done:", st.session_state.get("funding_complete", False))
    if st.session_state.get("page") != "intro":
        if st.button("🔙 Back to Lobby"):
            navigate("lobby")

# Intro Page
if st.session_state.get("page") == "intro":
    st.title("🚀 Welcome to BizSim")
    st.markdown("#### Build. Negotiate. Win. Choose your path as a startup CEO or investor.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎮 Start Simulation"):
            navigate("lobby")
    with col2:
        if st.button("💾 Save Game"):
            st.info("✅ Game saved (firebase temporarily disabled)")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))

# Routing
elif st.session_state.get("page") == "lobby":
    if st.session_state.get("mode") == "single" and not st.session_state.get("role"):
        lobby.render_role_picker(navigate)
    elif st.session_state.get("mode") == "single" and st.session_state.get("role"):
        navigate("onboarding")
    else:
        lobby.render_lobby(navigate)

elif st.session_state.get("page") == "onboarding":
    onboarding.render_onboarding(navigate)

elif st.session_state.get("page") == "funding_round":
    funding_round.render_funding_ui(navigate)

elif st.session_state.get("page") == "single_player":
    if not st.session_state.get("funding_complete"):
        navigate("funding_round")
    elif st.session_state.get("role") == "CEO":
        company_list.show_company_selection()
        ceo_dashboard.render_ceo_ui()
        ceo_decisions.render_decision_ui()
        staffing.render_staffing_ui()
        news_banner.render_news()
    elif st.session_state.get("role") == "Investor":
        investor_view.render_investor_ui()
        news_banner.render_news()
    else:
        st.warning("Unknown role selected. Returning to lobby.")
        navigate("lobby")

elif st.session_state.get("page") == "multiplayer":
    if st.session_state.get("role") == "CEO":
        company_list.show_company_selection()
        ceo_dashboard.render_ceo_ui()
        funding_round.render_funding_ui(navigate)
        ceo_decisions.render_decision_ui()
        staffing.render_staffing_ui()
        news_banner.render_news()
    elif st.session_state.get("role") == "Investor":
        investor_view.render_investor_ui()
        news_banner.render_news()
    else:
        st.warning("Please choose a role to continue.")
        lobby.render_role_picker(navigate)

else:
    st.error("Unknown page state. Resetting...")
    navigate("intro")