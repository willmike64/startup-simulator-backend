# funding_simulation.py

def simulate_seed_round(company_name, pitch_quality, founder_strength):
    import random
    base = pitch_quality * 0.5 + founder_strength * 0.5
    success_chance = base + random.uniform(-0.2, 0.2)
    funded = success_chance > 0.5
    valuation = 1_000_000 + int(pitch_quality * 500_000)

    return {
        "company": company_name,
        "funded": funded,
        "valuation": valuation if funded else 0,
        "notes": "✅ Successfully raised!" if funded else "❌ Investors passed this round."
    }

def run(company, session):
    return {'status': 'ok', 'module': 'funding_simulation'}



