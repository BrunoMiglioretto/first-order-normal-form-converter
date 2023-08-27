class Formula:
    def __init__(self, negation=False):
        self.tokens = []
        self.negation = negation

    def append_token(self, token):
        self.tokens.append(token)


class Connective:
    def __init__(self, token):
        self.token = token


class Literal:
    def __init__(self, token, negation=False):
        self.token = token
        self.negation = negation


class Predicate(Literal):
    def __init__(self, token, variable, negation=False):
        super().__init__(token, negation)
        self.variable = variable


class Quantifier:
    def __init__(self, variable, negation=False):
        self.variable = variable
        self.negation = negation


class ExistentialQuantifier(Quantifier):
    def __init__(self, variable, negation=False):
        super().__init__(variable, negation=negation)


class UniversalQuantifier(Quantifier):
    def __init__(self, variable, negation=False):
        super().__init__(variable, negation=negation)
