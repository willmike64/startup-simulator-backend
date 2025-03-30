import streamlit as st

def init_session_state():
    defaults = {
        "page": "Lobby",
        "logged_in": False,
        "mode": None,
        "role": None,
        "company_id": None,
        "funding_complete": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value