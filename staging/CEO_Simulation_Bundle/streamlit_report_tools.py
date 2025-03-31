import streamlit as st
from click_logger import log_click, get_click_log
from executive_summary import generate_summary
import json

st.set_page_config(page_title="📋 Reports & Logs", layout="wide")
st.title("🧾 Simulation Reports + Event Log")

st.sidebar.header("📎 Report Controls")
if st.sidebar.button("📌 Log a Sample Click"):
    log_click("Sample Click", context="Manual Trigger")
    st.sidebar.success("Click logged!")

st.subheader("📈 Executive Summary")
summary = generate_summary()
st.json(summary)

download = json.dumps(summary, indent=2)
st.download_button("📥 Download as JSON", data=download, file_name="executive_summary.json")

st.divider()

st.subheader("🧠 Click Log History")
logs = get_click_log()
if logs:
    for entry in logs[-10:][::-1]:  # Show last 10 entries
        st.markdown(f"- **{entry['timestamp']}** — `{entry['label']}` *(context: {entry['context']})*")
else:
    st.info("No click logs yet.")