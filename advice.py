import streamlit as st
from ai_banker import get_banker_advice
from ai_hr import get_hr_advice
from ai_board_members import get_board_advice

def get_advice(name: str, company: dict) -> str:
    if name == "AI Banker":
        return get_banker_advice(company)
    elif name == "HR":
        return get_hr_advice(company)
    elif name == "Board":
        return get_board_advice(company)
    return f"No custom advice available for {name}."