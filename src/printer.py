from src.config import quantifier
from src.models import Formula, Connective, Predicate, Quantifier, ExistentialQuantifier, UniversalQuantifier

printable_connective = {
    r"\wedge": "∧",
    r"\vee": "∨",
    r"\rightarrow": "→",
    r"\leftrightarrow": "↔",
}
printable_quantifier = {
    r"\forall": "∀",
    r"\exists": "∃",
}
printable_negation = "¬"


def build_printable_predicate(token):
    string = f"{token.token}({', '.join(token.variable)})"
    if token.negation:
        return f"{printable_negation}{string}"
    return string


def build_printable_quantifier(token, quantifier_type):
    string = f"{printable_quantifier[quantifier_type]} {token.variable}"
    if token.negation:
        return f"{printable_negation}{string}"
    return string


def build_printable_formula(formula):
    string = ""
    for token in formula.tokens:
        if isinstance(token, Formula):
            string = f"{string}({build_printable_formula(token)})"
        elif isinstance(token, Connective):
            string = f"{string} {printable_connective[token.token]} "
        elif isinstance(token, Predicate):
            string = f"{string}{build_printable_predicate(token)}"
        elif isinstance(token, ExistentialQuantifier):
            string = f"{string}{build_printable_quantifier(token, quantifier['exists'])}"
        elif isinstance(token, UniversalQuantifier):
            string = f"{string}{build_printable_quantifier(token, quantifier['exists'])}"
        else:
            string = f"{string}{token.token}"

    if formula.negation:
        return f"{printable_negation}{string}"
    return string
