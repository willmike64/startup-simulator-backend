# investor_engine.py

def score_company(investor, company):
    score = 0
    if company.get("industry") in investor["focus_industries"]:
        score += 3
    if company.get("growth_type") == investor["preferred_growth"]:
        score += 2
    if company.get("valuation", 0) >= investor["min_valuation"]:
        score += 2
    return score

def make_investment_decision(investor, companies, threshold=5):
    decisions = []
    for company in companies:
        s = score_company(investor, company)
        if s >= threshold and investor["token_balance"] >= 10_000:
            investor["invested_in"].append(company["name"])
            investor["token_balance"] -= 10_000
            decisions.append((company["name"], 10_000))
    return decisions

def run(company, session):
    return {'status': 'ok', 'module': 'investor_engine'}



