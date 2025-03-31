import openai
import streamlit as st

openai.api_key = st.secrets.get("openai_key")

def call_openai(prompt: str, role: str = "system", model="gpt-4") -> str:
    if not openai.api_key:
        return "❌ OpenAI API key not set in Streamlit secrets."

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": f"You are {role}."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"💥 OpenAI API error: {e}"