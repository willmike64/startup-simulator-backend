# leaderboard_live.py

def update_leaderboard(companies, metric='Valuation'):
    return sorted(
        [{"name": c["name"], metric: c.get(metric, 0)} for c in companies],
        key=lambda x: x[metric],
        reverse=True
    )

def run(company, session):
    return {'status': 'ok', 'module': 'leaderboard_live'}



