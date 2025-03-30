
import streamlit as st

def debug_session_state():
    st.subheader("🛠 Session Debug Info")
    for key in st.session_state:
        st.write(f"🔹 {key}: {st.session_state[key]}")
