from utils.ai import call_openai

def get_cfo_advice(company_data):
    prompt = f"You are a CFO reviewing a startup's financials. Offer financial insights or risk concerns. Company details: {company_data}"
    return call_openai(prompt, role="AI CFO")