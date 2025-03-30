from utils.session import init_session_state
init_session_state()

from utils.session import init_session_state
init_session_state()

import streamlit as st

def app():
    def show_company_selection():
        import streamlit as st
        st.write('📦 Company Selection UI')
if st.checkbox("Show Debug Info", key="debug_company_list"):
        st.json(st.session_state)

with st.expander("🛠 Debug Session State"):
    st.json(dict(st.session_state))