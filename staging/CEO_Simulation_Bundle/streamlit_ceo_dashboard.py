import streamlit as st
from firebase_connector import initialize_firebase, get_company_state

st.set_page_config(page_title="📊 CEO Dashboard", layout="wide")
st.title("📈 Real-Time CEO Financial Dashboard")

db = initialize_firebase()
company_id = st.text_input("Enter your company name to view financials:")

if company_id:
    state = get_company_state(db, company_id)
    if state:
        st.header(f"{company_id} — Current Financials")
        col1, col2, col3 = st.columns(3)
        col1.metric("Revenue", f"${state.get('Revenue', 0):,}")
        col2.metric("Burn Rate", f"${state.get('Burn', 0):,}")
        col3.metric("Profit", f"${state.get('Profit', 0):,}")

        st.subheader("📊 Company Snapshot")
        st.write(state)
    else:
        st.warning("❌ No data found for that company.")