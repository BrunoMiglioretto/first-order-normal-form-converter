class Literal:
    def __init__(self, token, negation=False):
        self.token = token
        self.negation = negation


class Connective:
    def __init__(self, token, left_literal, right_literal):
        assert isinstance(left_literal, Literal)
        assert isinstance(right_literal, Literal)

        self.token = token
        self.left_literal = left_literal
        self.right_literal = right_literal


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


class Formula:
    def __init__(self):
        self.tokens = []

    def append_token(self, token):
        self.tokens.append(token)
