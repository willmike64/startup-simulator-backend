# founder_dna.py

def generate_founder_profile(name):
    profiles = {
        "visionary": {"risk_tolerance": 0.9, "ethics": 0.6, "media_charm": 0.8},
        "pragmatist": {"risk_tolerance": 0.6, "ethics": 0.8, "media_charm": 0.6},
        "operator": {"risk_tolerance": 0.5, "ethics": 0.9, "media_charm": 0.5},
        "hustler": {"risk_tolerance": 0.8, "ethics": 0.5, "media_charm": 0.9}
    }
    import random
    persona = random.choice(list(profiles.keys()))
    return {
        "name": name,
        "persona": persona,
        **profiles[persona]
    }

def run(company, session):
    return {'status': 'ok', 'module': 'founder_dna'}



