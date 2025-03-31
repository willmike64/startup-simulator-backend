import streamlit as st
from advisors.ai_banker import get_banker_advice

def render_decision_ui():
    st.subheader("💼 CEO Decisions")

    company_data = {
        "name": "Neuronest",
        "valuation": "$5M",
        "funding_stage": "Seed"
    }

    if st.button("💬 Ask AI Banker"):
        result = get_banker_advice(company_data)
        st.success("🧠 AI Banker Responded:")
        st.write(result)

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))