# boardroom_engine.py

import random

def simulate_board_meeting(board_members, metrics):
    discussion = []
    votes = {"yes": 0, "no": 0}

    for member in board_members:
        opinion = member.advise(metrics)
        discussion.append(f"{member.name} ({member.specialty}): {opinion}")
        vote = "no" if "cut" in opinion.lower() or "churn" in opinion.lower() else "yes"
        votes[vote] += 1

    decision = "Approved" if votes["yes"] >= votes["no"] else "Blocked"
    return {
        "discussion": discussion,
        "vote_result": votes,
        "decision": decision
    }

def run(company, session):
    return {'status': 'ok', 'module': 'boardroom_engine'}



