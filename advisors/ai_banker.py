from utils.ai import call_openai

def get_banker_advice(company_data):
    prompt = f"Review this startup's funding request and provide investment advice. Company details: {company_data}"
    return call_openai(prompt, role="AI Banker")