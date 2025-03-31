# founder_dossier.py

def generate_dossier(profile, decision_log):
    dossier = {
        "Profile Summary": profile,
        "Decision History": decision_log,
        "Alignment Score": {
            "aligned": sum(1 for d in decision_log if abs(d["risk_score"] - profile["risk_tolerance"]) < 0.2),
            "total": len(decision_log)
        }
    }
    return dossier

def run(company, session):
    return {'status': 'ok', 'module': 'founder_dossier'}



