# founder_recovery.py

def initiate_recovery_program(wellness_status):
    if wellness_status["burnout_risk"] > 70:
        return {
            "plan": "🧘 Retreat and coaching program initiated.",
            "duration_weeks": 4,
            "expected_recovery": 30
        }
    elif wellness_status["burnout_risk"] > 50:
        return {
            "plan": "💼 Executive support and time off.",
            "duration_weeks": 2,
            "expected_recovery": 15
        }
    else:
        return {
            "plan": "⚖️ Maintain routines and schedule breaks.",
            "duration_weeks": 1,
            "expected_recovery": 5
        }

def run(company, session):
    return {'status': 'ok', 'module': 'founder_recovery'}



