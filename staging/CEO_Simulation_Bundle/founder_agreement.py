# founder_agreement.py

def generate_agreement(team):
    text = f"🏢 Founders Agreement for {team['team_name']}\n\n"
    text += "By signing below, each founder agrees to contribute to their assigned role, uphold company vision, and meet deadlines.\n\n"
    for member in team["members"]:
        text += f"- {member['name']} ({member['role']}): {member['shares']}% equity\n"
    text += "\nSignatures: ___________________________"
    return text

def sign_agreement(team):
    team["agreement_signed"] = True
    return team

def run(company, session):
    return {'status': 'ok', 'module': 'founder_agreement'}



