import streamlit as st
import os
from pathlib import Path

st.set_page_config(page_title="🧠 Module Control Center", layout="wide")
st.title("🛠️ AI-Powered Module Editor")

base_path = Path(".").resolve()
py_files = sorted(base_path.glob("*.py"))

module_names = [f.name for f in py_files if f.name != "streamlit_app.py"]
selected = st.selectbox("Select a module to view/edit:", module_names)

if selected:
    file_path = base_path / selected
    content = file_path.read_text()
    updated = st.text_area("📝 Edit module:", value=content, height=600)
    
    if st.button("💾 Save Changes"):
        file_path.write_text(updated)
        st.success(f"{selected} updated successfully!")