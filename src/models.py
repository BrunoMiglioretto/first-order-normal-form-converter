from src.config import connective


class Formula:
    def __init__(self, negation=False):
        assert isinstance(negation, bool)

        self.tokens = []
        self.negation = negation

    def __str__(self):
        return "Formula"

    def append_token(self, token):
        self.tokens.append(token)


class Connective:
    def __init__(self, token):
        self.token = token

    def __str__(self):
        return f"Conectivo {connective[self.token]}"


class Literal:
    def __init__(self, token, negation=False):
        self.token = token
        self.negation = negation

    def __copy__(self):
        return Literal(self.token, negation=self.negation)

    def __str__(self):
        return f"Literal {self.token}"


class Predicate(Literal):
    def __init__(self, token, variable, negation=False):
        super().__init__(token, negation)
        self.variable = variable

    def __copy__(self):
        return Predicate(self.token, self.variable, negation=self.negation)

    def __str__(self):
        return f"Predicado {self.token}"


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
