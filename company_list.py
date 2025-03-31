from utils.session import init_session_state
init_session_state()

import streamlit as st

def app():
    def show_company_selection():
        import streamlit as st
        st.write('📦 Company Selection UI')
if st.checkbox("ShowCompanyList", key="show_company_list"):
    Debug Info", key="debug_company_list"):
        st.json(st.session_state)

