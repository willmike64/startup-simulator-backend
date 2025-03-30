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
                st.session_state.company_id = company['id']
                st.session_state.page = 'funding_round'
                st.rerun()
if st.checkbox("Show Debug Info"):
        st.json(st.session_state)