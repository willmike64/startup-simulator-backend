# investment_summary.py

def generate_summary(company, round_number):
    summary = {
        "Company Name": company["name"],
        "Industry": company.get("industry", "TBD"),
        "Valuation": company["Valuation"],
        "Revenue": company["Revenue"],
        "Customers": company["Customers"],
        "Morale": company["Morale"],
        "Round": round_number,
        "Notes": []
    }

    if company["Revenue"] == 0:
        summary["Notes"].append("⚠️ Early stage company with limited financials.")
    if company["Valuation"] < 1500000:
        summary["Notes"].append("⚠️ Company may be pre-revenue or pre-product.")
    if company["Customers"] < 100:
        summary["Notes"].append("⚠️ Low customer traction. Consider market validation.")

    return summary

def run(company, session):
    return {'status': 'ok', 'module': 'investment_summary'}



