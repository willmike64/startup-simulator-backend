import streamlit as st
from pathlib import Path

st.title("🔐 secrets.toml Setup Form")

st.markdown("Use this form to create your Streamlit `.streamlit/secrets.toml` file.")

openai_key = st.text_input("OpenAI API Key", value="", type="password")
discord_token = st.text_input("Discord Bot Token", value="", type="password")
discord_channel_id = st.text_input("Discord Channel ID", value="")

if st.button("Generate secrets.toml"):
    secrets_content = f"""OPENAI_API_KEY = "{openai_key}"
DISCORD_BOT_TOKEN = "{discord_token}"
DISCORD_CHANNEL_ID = "{discord_channel_id}"
"""
    secrets_path = Path(".streamlit")
    secrets_path.mkdir(exist_ok=True)
    with open(secrets_path / "secrets.toml", "w") as f:
        f.write(secrets_content.strip())
    st.success("✅ File written to .streamlit/secrets.toml")
    st.code(secrets_content.strip(), language="toml")