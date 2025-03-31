import streamlit as st

st.set_page_config(page_title="🧠 Simulation Control Center", layout="wide")
st.title("🧰 Creator Control Panel (Explain Mode)")

st.sidebar.title("🧠 Explain Mode")
explain = st.sidebar.toggle("Show 'Why this button matters'", value=True)

def explain_button(label, run_cmd, explanation):
    if st.button(label):
        st.success(f"🟢 Running: `{run_cmd}`")
        st.code(run_cmd, language="bash")
        if explain:
            st.info(explanation)

st.header("🎮 Game Engines")
explain_button(
    "▶️ Run Simulation Gameboard",
    "streamlit run streamlit_app.py",
    "Launches the full game loop including onboarding, AI advisors, and round management."
)

explain_button(
    "🚀 Launch Interactive Onboarding",
    "streamlit run streamlit_app.py",
    "Lets users browse companies, select funding, and start as CEO. Begins Round 1 of the simulation."
)

st.header("📊 Dashboards")
explain_button(
    "📈 Open CEO Financial Dashboard",
    "streamlit run streamlit_ceo_dashboard.py",
    "Loads Firebase-powered real-time financial data for any company."
)

st.header("🛠️ Developer Tools")
explain_button(
    "🧠 Launch AI Patch Console",
    "streamlit run streamlit_smart_patch_console.py",
    "Scans project folder for broken modules and uses GPT-4 to suggest or auto-apply fixes."
)

explain_button(
    "📝 Open Module Editor",
    "streamlit run streamlit_module_editor.py",
    "Enables editing any .py module inside the simulation right from your browser."
)

st.header("🔐 Secrets & Setup")
explain_button(
    "🔑 Setup OpenAI/Discord Keys",
    "streamlit run secrets_setup.py",
    "Generate or update your .streamlit/secrets.toml file securely."
)

st.header("📋 Config Validator")
explain_button(
    "📁 Run Config Validator",
    "python config_validator.py",
    "Checks whether all required files are present and that your simulation is ready to run."
)