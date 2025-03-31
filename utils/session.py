import streamlit as st

def init_session_state():
    defaults = {
        "page": "intro",
        "mode": "single",
        "role": None,
        "username": None,
        "user_id": None,
        "logged_in": False,
        "funding_complete": False
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value