import streamlit as st

def app():
    def render_investor_ui():
        import streamlit as st
        st.write('📈 Investor Dashboard')
if st.checkbox("Show Debug Info"):
        st.json(st.session_state)