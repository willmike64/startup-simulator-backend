# founder_survey.py

def run_founder_survey(responses):
    # Responses should be a dict of question_id: score (1–5 scale)
    profile = {
        "risk_tolerance": round((responses.get("q1", 3) + responses.get("q2", 3)) / 10, 2),
        "ethics": round((responses.get("q3", 3) + responses.get("q4", 3)) / 10, 2),
        "strategic_style": "aggressive" if responses.get("q5", 3) >= 4 else "defensive"
    }
    profile["profile"] = classify_profile(profile)
    return profile

def classify_profile(p):
    if p["risk_tolerance"] >= 0.7 and p["ethics"] < 0.6:
        return "Hustler"
    if p["risk_tolerance"] >= 0.7:
        return "Visionary"
    if p["ethics"] >= 0.7:
        return "Operator"
    return "Pragmatist"

def run(company, session):
    return {'status': 'ok', 'module': 'founder_survey'}



