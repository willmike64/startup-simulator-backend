import streamlit as st

def render_news():
    st.info('📣 AI News: Market shifts expected due to new regulations.')

    with st.expander("🛠 Debug Session State", expanded=False):
        st.json(dict(st.session_state))