# financial.py — Round-based financial engine

import random

def generate_financials():
    return {
        "revenue": 120000,
        "burn_rate": 30000,
        "expenses": 80000,
        "COGS": 20000,
        "profit": 40000
    }

def update_financials(company, round_number):
    base_revenue = company.get("Revenue", 0)
    growth_factor = 1.05 + (round_number * 0.01)  # Simulated growth each round
    revenue = int(base_revenue * growth_factor) + random.randint(5000, 20000)
    expenses = int(revenue * 0.5)
    profit = revenue - expenses

    company["Revenue"] = revenue
    company["Burn"] = expenses
    company["Profit"] = profit
    return company