# launchpad_engine.py — now supports AI-generated company lists

from company_generator_ai import generate_startups

company_ownership = {}

def offer_companies(use_ai=True):
    if use_ai:
        startups = generate_startups(n=15)
    else:
        startups = [
            {"name": f"Startup_{i+1}", "Valuation": 1000000 + (i * 50000), "buyers": []}
            for i in range(15)
        ]
    for startup in startups:
        startup.setdefault("Revenue", 0)
        startup.setdefault("Morale", 70)
        startup.setdefault("Customers", 0)
        startup.setdefault("Cash", 150000)
        startup.setdefault("dependencies", [])
    return startups

def buy_company(player_name, company_name, all_offers):
    for company in all_offers:
        if company["name"] == company_name:
            buyers = company_ownership.setdefault(company_name, [])
            base_price = company["Valuation"]
            price_multiplier = 1 + (0.25 * len(buyers))
            final_price = int(base_price * price_multiplier)
            buyers.append(player_name)
            return {
                "company": company_name,
                "buyer": player_name,
                "price_paid": final_price,
                "ownership_pct": round(1 / len(buyers) * 100, 2),
                "buyers": buyers
            }
    return None