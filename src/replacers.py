from src.config import connective
from src.models import Connective, Formula, Quantifier

import copy

from src.printer import build_printable_formula


def transform_to_fnd(formula):
    formula = replace_biconditional(formula)
    print(f"Fórmula parcial: {build_printable_formula(formula)}")

    formula = replace_implication(formula)
    print(f"Fórmula parcial: {build_printable_formula(formula)}")

    while has_negated_formulas(formula):
        replace_negated_formulas(formula)

    print(f"Fórmula parcial: {build_printable_formula(formula)}")

    return formula


def transform_to_fnc(formula):
    pass


def replace_biconditional(formula):
    for index, token in enumerate(formula.tokens):
        if isinstance(token, Formula):
            replace_biconditional(token)
        elif not isinstance(token, Quantifier):
            if token.token == connective["biconditional"]:
                formula.tokens[index] = Connective(connective["and"])

                antecedent = formula.tokens[index - 1]
                consequent = formula.tokens[index + 1]

                antecedent_formula = Formula()
                antecedent_formula.tokens.append(copy.copy(antecedent))
                antecedent_formula.tokens.append(Connective(connective["implication"]))
                antecedent_formula.tokens.append(copy.copy(consequent))
                formula.tokens[index - 1] = antecedent_formula

                consequent_formula = Formula()
                consequent_formula.tokens.append(copy.copy(consequent))
                consequent_formula.tokens.append(Connective(connective["implication"]))
                consequent_formula.tokens.append(copy.copy(antecedent))
                formula.tokens[index + 1] = consequent_formula

    return formula


def replace_implication(formula):
    for index, token in enumerate(formula.tokens):
        if isinstance(token, Formula):
            replace_implication(token)
        elif not isinstance(token, Quantifier):
            if token.token == connective["implication"]:
                formula.tokens[index] = Connective(connective["or"])

                antecedent = formula.tokens[index - 1]
                antecedent.negation = not antecedent.negation

    return formula


def has_negated_formulas(formula):
    has_negated = False
    for token in formula.tokens:
        if isinstance(token, Formula) and token.negation:
            has_negated = True
        elif isinstance(token, Formula):
            has_negated = has_negated_formulas(token)

        if has_negated:
            return True

    return False


def replace_negated_formulas(formula):
    for token in formula.tokens:
        if isinstance(token, Formula) and token.negation:
            formula = replace_de_morgan(token)
        if isinstance(token, Formula):
            formula = replace_negated_formulas(token)

    return formula


def replace_de_morgan(formula):
    formula.negation = not formula.negation

    for index, token in enumerate(formula.tokens):
        if isinstance(token, Connective):
            if token.token == connective["or"]:
                formula.tokens[index] = Connective(connective["and"])
            else:
                formula.tokens[index] = Connective(connective["or"])
        else:
            token.negation = not token.negation

    return formula


# def replace_distribution(formula):

