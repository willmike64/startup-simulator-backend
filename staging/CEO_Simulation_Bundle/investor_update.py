# investor_update.py

def generate_investor_update(company_name, metrics):
    update = f"""📈 Investor Update from {company_name}
Revenue: ${metrics.get('Revenue', 0):,.2f}
Profit: ${metrics.get('Profit', 0):,.2f}
Valuation: ${metrics.get('Valuation', 0):,.2f}
Morale: {metrics.get('morale', 0)}%
Growth Rate: {metrics.get('growth_rate', 0):.2%}
Runway: {metrics.get('runway', 0)} months
Thank you for your continued support!
"""
    return update

def run(company, session):
    return {'status': 'ok', 'module': 'investor_update'}



