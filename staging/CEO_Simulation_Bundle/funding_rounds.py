# funding_rounds.py

def raise_funding_round(company_metrics, round_stage):
    valuation = company_metrics.get("Valuation", 0)
    round_size = {
        "Seed": 500_000,
        "Series A": 2_000_000,
        "Series B": 5_000_000,
        "Series C": 10_000_000
    }.get(round_stage, 1_000_000)

    dilution = {
        "Seed": 0.10,
        "Series A": 0.15,
        "Series B": 0.20,
        "Series C": 0.25
    }.get(round_stage, 0.15)

    new_shares = int(valuation * dilution / round_size * 1_000_000)
    return {
        "stage": round_stage,
        "amount_raised": round_size,
        "dilution": dilution,
        "new_shares_issued": new_shares
    }

def run(company, session):
    return {'status': 'ok', 'module': 'funding_rounds'}



