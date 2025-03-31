import streamlit as st
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

init_session_state()
# Auto-redirect from "intro" to "lobby" to bypass manual login
# if st.session_state.page == "intro":
#    st.session_state.page = "lobby"
#    st.rerun()

st.write("🔥 Top of app.py")
st.write("🔍 Session State Main Lobby", dict(st.session_state))
st.write("✅ After Init:", dict(st.session_state))

def navigate(page):
    st.session_state.page = page
    st.rerun()

def app():
    st.set_page_config(page_title="Startup Simulator", layout="wide")

    st.sidebar.title("🚀 Startup Simulator")
    st.sidebar.write("🧭 Page:", st.session_state.page)
    st.sidebar.write("🎮 Mode:", st.session_state.mode)
    st.sidebar.write("🎭 Role:", st.session_state.role)
    st.sidebar.write("🏢 Company ID:", st.session_state.company_id)
    st.sidebar.write("💰 Funding Done:", st.session_state.funding_complete)

if st.session_state.page == "intro":
    st.set_page_config(page_title="BizSim Alpha", layout="centered")
    
    st.title("🚀 Welcome to BizSim")
    st.markdown("#### Build. Negotiate. Win.\n\nChoose your path as a startup CEO or investor and lead your company to the top.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎮 Start Simulation"):
            st.session_state.page = "lobby"
            st.rerun()

    with col2:
        if st.button("💾 Save Game"):
            st.write("✅ Saved (placeholder or Firebase call here)")


def app():
    import streamlit as st

    # -----------------------------
    # Session State Initialization
    # -----------------------------
    if "page" not in st.session_state:
        st.session_state.page = "intro"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "mode" not in st.session_state:
        st.session_state.mode = None
    if "role" not in st.session_state:
        st.session_state.role = None
    if "company_id" not in st.session_state:
        st.session_state.company_id = None
    if "funding_complete" not in st.session_state:
        st.session_state.funding_complete = False

    # -----------------------------
    # Sidebar Debug + Navigation
    # -----------------------------
    with st.sidebar:
        st.write("🧭 Page:", st.session_state.page)
        st.write("🎮 Mode:", st.session_state.mode)
        st.write("🎭 Role:", st.session_state.role)
        st.write("🏢 Company ID:", st.session_state.company_id)
        st.write("💰 Funding Done:", st.session_state.funding_complete)
        if st.session_state.page != "intro":
            if st.button("🔙 Back to Lobby"):
                st.session_state.page = "lobby"
                st.rerun()

    # -----------------------------
    # Navigation Helper
    # -----------------------------
    def navigate(page):
        st.session_state.page = page
        st.rerun()

    # -----------------------------
    # Import Modules
    # -----------------------------
    from views import streamlit_company_list as company_list
    from views import streamlit_ceo_dashboard as ceo_dashboard
    from views import streamlit_ceo_decisions as ceo_decisions
    from views import streamlit_funding_round as funding_round
    from views import streamlit_founder_dashboard as investor_view
    from views import streamlit_generate_companies as company_generator
    from views import streamlit_lobby as lobby
    from views import streamlit_onboarding as onboarding
    from components import stock_ticker_banner as news_banner
    from views import staffing

    # -----------------------------
    # Flow Routing
    # -----------------------------
    if st.session_state.page == "intro":
        st.title("💼 Startup Simulation")
        st.markdown("""
        Welcome to the Startup Business Simulation.

        In this simulation, you'll experience the challenges of managing or investing in a startup. Choose your path and interact with AI agents or real players.
        """)
        if st.button("Login / Start"):
            st.session_state.logged_in = True
            navigate("lobby")

    elif st.session_state.page == "lobby":
        if st.session_state.mode == "single" and not st.session_state.role:
            lobby.render_role_picker(navigate)
        elif st.session_state.mode == "single" and st.session_state.role:
            navigate("onboarding")
        else:
            lobby.render_lobby(navigate)

    elif st.session_state.page == "onboarding":
        onboarding.render_onboarding(navigate)

    elif st.session_state.page == "funding_round":
        funding_round.render_funding_ui(navigate)

    elif st.session_state.page == "single_player":
        if not st.session_state.funding_complete:
            navigate("funding_round")
        elif st.session_state.role == "CEO":
            company_list.show_company_selection()
            ceo_dashboard.render_ceo_ui()
            ceo_decisions.render_decision_ui()
            staffing.render_staffing_ui()
            news_banner.render_news()
        elif st.session_state.role == "Investor":
            investor_view.render_investor_ui()
            news_banner.render_news()
        else:
            st.warning("Unknown role selected. Returning to lobby.")
            navigate("lobby")

    elif st.session_state.page == "multiplayer":
        if st.session_state.role == "CEO":
            company_list.show_company_selection()
            ceo_dashboard.render_ceo_ui()
            funding_round.render_funding_ui(navigate)
            ceo_decisions.render_decision_ui()
            staffing.render_staffing_ui()
            news_banner.render_news()
        elif st.session_state.role == "Investor":
            investor_view.render_investor_ui()
            news_banner.render_news()
        else:
            st.warning("Please choose a role to continue.")
            lobby.render_role_picker(navigate)

    else:
        st.error("Unknown page state. Resetting...")
        navigate("intro")

st.write("🔥 Your final cleaned version")