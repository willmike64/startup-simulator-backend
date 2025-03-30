import openai
import streamlit as st

def suggest_ceo_decision(context):
    openai.api_key = st.secrets.get("openai_key", "sk-...")  # Replace with your actual key or secret config
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a startup advisor."},
            {"role": "user", "content": context}
        ]
    )
    return response["choices"][0]["message"]["content"]