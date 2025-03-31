import streamlit as st

def render_company_generator():
    st.title("🏗️ Startup Generator")
    st.write("Generate AI-powered startup concepts.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))