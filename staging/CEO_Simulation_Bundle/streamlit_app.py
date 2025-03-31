import streamlit as st
import pandas as pd

from sim_state import initialize_simulation, load_simulation
from player_session import create_session, load_session, advance_round
from launchpad_engine import offer_companies, buy_company
from onboarding_investment import get_pitch_choices, select_pitch
from fed_and_banks import get_fed_policy
from ai import call_ai_advisors
from supply import run_supply_chain_analysis
from financial import generate_financials
from legal import legal_review
from team import check_morale

st.set_page_config(page_title="🎮 Startup Sim Onboarding", layout="wide")
st.title("📈 Startup Simulation: Interactive Onboarding")

# State tracker
if "simulation_started" not in st.session_state:
    st.session_state["simulation_started"] = False

if not st.session_state["simulation_started"]:
    st.subheader("🔍 Explore Available Companies")

    companies = offer_companies()
    company_names = [c["name"] for c in companies]
    selected = st.selectbox("Choose a company to preview", company_names)
    company = next(c for c in companies if c["name"] == selected)

    st.markdown("### 📋 Company Snapshot")
    st.json(company)
    st.write(f"🧠 Industry: {company.get('industry', 'TBD')}")
    st.write(f"💰 Valuation: ${company.get('Valuation', 0):,}")
    st.write(f"🧪 Morale: {company.get('Morale', 0)}%")
    st.write(f"📦 Dependencies: {', '.join(company.get('dependencies', []))}")

    st.markdown("### 💡 Suggested Capital Needs")
    st.info("🧮 Based on your starting valuation and dependencies, you may want to raise at least 10–20% of your valuation.")

    st.divider()
    st.subheader("💼 Choose Investment Offer")
    pitch_choices = get_pitch_choices()
    offer_titles = [p["title"] for p in pitch_choices]
    chosen_offer = st.selectbox("Select an investment offer", offer_titles)

    st.subheader("🧑‍🚀 Final Setup")
    name = st.text_input("Your name", value="Player 1")

    if st.button("✅ Confirm & Start Simulation"):
        deal = select_pitch(chosen_offer)
        buy_company(name, selected, companies)
        initialize_simulation()
        create_session(name, selected, False)
        st.session_state["simulation_started"] = True
        st.success(f"{name} leads {selected} with {deal['equity']} equity at a valuation of ${deal['valuation']:,}!")

# Once running
if st.session_state["simulation_started"]:
    data = load_simulation()
    session = load_session()
    company_id = session["company_id"]
    company = next((c for c in data["companies"] if c["name"] == company_id), None)
    round_num = session["current_round"]

    st.header(f"📋 {company_id} — Quarter {round_num}")
    st.subheader("📊 Key Stats")
    st.metric("Valuation", f"${company.get('Valuation', 0):,}")
    st.metric("Revenue", f"${company.get('Revenue', 0):,}")
    st.metric("Morale", f"{company.get('Morale', 0)}%")
    st.metric("Customers", f"{company.get('Customers', 0)}")

    st.subheader("🎯 Strategic Actions")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Call AI Advisor"):
            st.info(call_ai_advisors())
        if st.button("Check Morale"):
            st.json(check_morale())

    with col2:
        if st.button("Run Supply Chain"):
            st.success(run_supply_chain_analysis())
        if st.button("Legal Review"):
            st.warning(legal_review())

    st.subheader("📈 Financials This Round")
    st.write(generate_financials())

    if st.button("⏭️ Advance to Next Quarter"):
        advance_round()
        st.success("📆 Round advanced. Reload to continue.")
        st.rerun()