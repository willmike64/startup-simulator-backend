# founder_wellness.py

def track_wellness(stress_level, sleep_quality, workload):
    # All scores from 0 to 100
    burnout_risk = max(0, (workload * 0.4 + (100 - sleep_quality) * 0.3 + stress_level * 0.3))
    status = (
        "🔥 Burnout imminent!" if burnout_risk > 80 else
        "⚠️ High stress." if burnout_risk > 60 else
        "🟡 Manageable but monitor." if burnout_risk > 40 else
        "🟢 Healthy and focused."
    )
    return {
        "burnout_risk": round(burnout_risk, 1),
        "status": status
    }

def run(company, session):
    return {'status': 'ok', 'module': 'founder_wellness'}



