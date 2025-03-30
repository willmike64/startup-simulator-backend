from utils.session import init_session_state
init_session_state()

from utils.session import init_session_state
init_session_state()

import streamlit as st

def app():
    def render_onboarding(navigate):
        import streamlit as st
        st.subheader("🚀 Choose a Company to Acquire")
        companies = [
            {"id": 1, "name": "SmartHome AI", "valuation": 3_000_000},
            {"id": 2, "name": "BioHealthX", "valuation": 5_000_000},
            {"id": 3, "name": "GreenEnergy Grid", "valuation": 4_500_000}
        ]
        for company in companies:
            st.write(f"**{company['name']}** - Valuation: ${company['valuation']:,}")
            if st.button(f"Select {company['name']}"):
                st.rerun()
if st.checkbox("Show Debug Info", key="debug_onboarding"):
        st.json(st.session_state)

with st.expander("🛠 Debug Session State"):
    st.json(dict(st.session_state))