from utils.session import init_session_state
init_session_state()

from utils.session import init_session_state
init_session_state()

import streamlit as st

def app():
    def render_decision_ui():
        import streamlit as st
        st.write('🧠 CEO Strategic Decisions')
if st.checkbox("Show Debug Info", key="debug_ceo_decisions"):
        st.json(st.session_state)

with st.expander("🛠 Debug Session State"):
    st.json(dict(st.session_state))