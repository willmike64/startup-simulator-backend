from utils.session import init_session_state
init_session_state()

from utils.session import init_session_state
init_session_state()

import streamlit as st

def app():
    def render_investor_ui():
        import streamlit as st
        st.write('📈 Investor Dashboard')
if st.checkbox("Show Debug Info", key="debug_founder_dashboard"):
        st.json(st.session_state)

with st.expander("🛠 Debug Session State"):
    st.json(dict(st.session_state))