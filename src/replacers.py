from src.config import connective
from src.models import Connective, Formula

import copy


def transform_to_fnd(formula):
    formula = replace_biconditional(formula)
    formula = replace_implication(formula)

    while has_negated_formulas(formula):
        replace_negated_formulas(formula)

    return formula


def transform_to_fnc(formula):
    pass


def replace_biconditional(formula):
    for index, token in enumerate(formula.tokens):
        if isinstance(token, Formula):
            replace_biconditional(token)
        elif token.token == connective["biconditional"]:
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
        elif token.token == connective["implication"]:
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

    for token in formula.tokens:
        if isinstance(token, Connective):
            if token.token == connective["or"]:
                token.token = Connective(connective["and"])
            else:
                token.token = Connective(connective["or"])
        else:
            token.negation = not token.negation

    return formula
