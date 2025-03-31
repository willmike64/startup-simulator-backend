import streamlit as st

def render_ceo_ui():
    st.title("🧠 CEO Dashboard")
    st.write("Key metrics, goals, and AI interactions.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))