# negotiation_engine.py

import random

def negotiate(base_offer, power_balance, morale_modifier=0.0):
    '''
    Returns the final deal amount after negotiation.
    - power_balance: 0 (target strong) to 1 (initiator strong)
    - morale_modifier: affects willingness to compromise
    '''
    negotiation_factor = (0.8 + random.random() * 0.4)
    adjustment = (power_balance - 0.5) * 2
    morale_influence = morale_modifier * 0.5

    final_offer = base_offer * (1 + adjustment * 0.1 + morale_influence * 0.05)
    return round(final_offer * negotiation_factor, 2)

def run(company, session):
    return {'status': 'ok', 'module': 'negotiation_engine'}



