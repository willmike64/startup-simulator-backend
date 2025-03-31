# banking.py

class Loan:
    def __init__(self, borrower, principal, interest_rate, term_rounds, covenants):
        self.borrower = borrower
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_rounds = term_rounds
        self.remaining_rounds = term_rounds
        self.covenants = covenants
        self.active = True

    def check_covenants(self, metrics):
        violations = {}
        for key, min_val in self.covenants.items():
            if metrics.get(key, 0) < min_val:
                violations[key] = (metrics.get(key, 0), min_val)
        return violations

    def progress_round(self):
        self.remaining_rounds -= 1
        if self.remaining_rounds <= 0:
            self.active = False


class Bank:
    def __init__(self, name, fed, initial_tokens):
        self.name = name
        self.fed = fed
        self.reserve = initial_tokens
        self.loans = []

    def lend(self, loan: Loan):
        required_reserve = loan.principal * self.fed.reserve_ratio
        if self.reserve >= required_reserve:
            self.reserve -= required_reserve
            self.loans.append(loan)
            return True
        return False

    def recall_loans(self):
        recalled = []
        for loan in self.loans:
            if loan.active:
                loan.active = False
                recalled.append(loan)
        return recalled

    def check_compliance(self):
        total_loans = sum(l.principal for l in self.loans if l.active)
        required_reserve = total_loans * self.fed.reserve_ratio
        return self.reserve >= required_reserve

    def enforce_covenants(self, borrower_metrics_map):
        recalls = []
        for loan in self.loans:
            if loan.active:
                metrics = borrower_metrics_map.get(loan.borrower, {})
                violations = loan.check_covenants(metrics)
                if violations:
                    loan.active = False
                    recalls.append((loan, violations))
        return recalls

def run(company, session):
    return {'status': 'ok', 'module': 'banking'}



