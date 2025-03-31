import streamlit as st

def render_funding_ui(navigate):
    st.title("💸 Funding Round Simulation")
    st.write("Run through offers, counteroffers, and AI negotiations.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))