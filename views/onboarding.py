import streamlit as st

def render_onboarding(navigate):
    st.title("🚀 Startup Onboarding")
    st.write("Select a company, review objectives, and begin.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))