import streamlit as st

def render_staffing_ui():
    st.header("👥 Team Builder")
    st.write("Manage teams, departments, and open roles.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))