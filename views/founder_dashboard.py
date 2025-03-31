import streamlit as st

def render_investor_ui():
    st.title("📈 Founder Dashboard")
    st.write("Investor perspectives, KPIs, and company tracking.")

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))