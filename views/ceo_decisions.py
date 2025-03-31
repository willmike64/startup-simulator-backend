import streamlit as st
from advisors.ai_banker import get_banker_advice

def render_decision_ui():
    st.subheader("💼 CEO Decisions")
    st.write("Strategic pivots, investments, AI advisors")

    company_data = {
        "name": "NeuroNest",
        "valuation": "$2M",
        "funding_stage": "Seed",
        "industry": "HealthTech"
    }

    if st.button("💬 Ask AI Banker for Advice"):
        response = get_banker_advice(company_data)
        st.success("🧠 AI Banker Responded:")
        st.write(response)

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))