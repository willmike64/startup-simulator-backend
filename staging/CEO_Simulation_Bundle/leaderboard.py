# leaderboard.py

def generate_leaderboard(company_stats_list):
    return sorted(company_stats_list, key=lambda c: c["valuation"], reverse=True)

def run(company, session):
    return {'status': 'ok', 'module': 'leaderboard'}



