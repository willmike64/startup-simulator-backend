# founder_branding.py

def update_founder_reputation(events, current_score):
    for e in events:
        if "TechCrunch" in e:
            current_score += 10
        elif "highlighted" in e:
            current_score += 5
        elif "negative" in e:
            current_score -= 15
    return max(0, min(100, current_score))

def run(company, session):
    return {'status': 'ok', 'module': 'founder_branding'}



