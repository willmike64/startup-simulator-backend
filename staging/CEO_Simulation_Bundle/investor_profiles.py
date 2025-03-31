# investor_profiles.py

import random

INDUSTRIES = [
    "Urban Agriculture", "Craft Brewery", "Food Production", "Renewable Energy",
    "Construction", "Logistics", "Food Delivery", "Utilities", "AgTech SaaS",
    "Urban Design", "Agricultural Equipment", "Agri-Finance"
]

GROWTH_TYPES = ["fast", "stable", "disruptive"]
RISK_TYPES = ["low", "medium", "high"]

def generate_investor(name, investor_type):
    return {
        "name": name,
        "type": investor_type,
        "risk_profile": random.choice(RISK_TYPES),
        "focus_industries": random.sample(INDUSTRIES, k=2),
        "preferred_growth": random.choice(GROWTH_TYPES),
        "min_valuation": random.randint(50_000, 200_000),
        "invested_in": [],
        "token_balance": random.randint(10_000, 100_000)
    }

# Generate AI investors
AI_LARGE_INVESTORS = [generate_investor(f"AI-Large-{i+1}", "institutional") for i in range(100)]
AI_ANGEL_INVESTORS = [generate_investor(f"AI-Angel-{i+1}", "angel") for i in range(50)]

# User-as-investor slot
USER_INVESTOR = {
    "name": "User-Investor",
    "type": "user",
    "risk_profile": "custom",
    "focus_industries": [],
    "preferred_growth": "",
    "min_valuation": 0,
    "invested_in": [],
    "token_balance": 100_000
}

def run(company, session):
    return {'status': 'ok', 'module': 'investor_profiles'}



