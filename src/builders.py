from src.config import (
    valid_quantifiers,
    modulator,
    valid_predicates,
    valid_variables,
    valid_propositions,
    valid_connectives,
)
from src.models import (
    Formula,
    ExistentialQuantifier,
    UniversalQuantifier,
    Predicate,
    Literal,
    Connective,
)
from src.config import quantifier


def is_end_of_formula(latex):
    if not latex:
        return True

    if latex[0] == ")":
        return True

    return False


def is_predicate_token(latex):
    predicate_character = latex[0]

    if predicate_character not in valid_predicates:
        return False

    if latex[1] != "(":
        return False

    if latex[2] not in valid_variables:
        return False

    return True


def is_quantifier_token(latex):
    for quantifier in valid_quantifiers:
        is_quantifier = True
        for index, character in enumerate(quantifier):
            if latex[index] != character:
                is_quantifier = False
                break

        if is_quantifier:
            return True
    return False


def is_negation_modifier_token(latex):
    for index, character in enumerate(modulator["negation"]):
        if latex[index] != character:
            return False
    return True


def is_proposition_token(latex):
    return latex[0] in valid_propositions


def is_connective_token(latex):
    for connective in valid_connectives:
        is_connective = True
        for index, character in enumerate(connective):
            if latex[index] != character:
                is_connective = False
                break

        if is_connective:
            return True
    return False


def is_sub_formula_token(latex):
    return latex[0] == "("


def build_connective_token(latex):
    connective_token = latex.split()[0]
    new_latex = latex.replace(connective_token, "", 1)
    return new_latex.strip(), Connective(connective_token)


def build_predicate_token(latex):
    predicate_character = latex[0]
    variables = [variable.strip() for variable in latex[2 : latex.find(")")].split(",")]

    if not variables:
        raise Exception("Predicado sem variaveis")

    invalid_variables = [
        variable for variable in variables if variable not in valid_variables
    ]
    if invalid_variables:
        raise Exception(
            f"Variáveis da proposição {predicate_character} estão inválidas: {variables}"
        )

    return latex[latex.find(")") + 1 :].strip(), Predicate(
        predicate_character, variables
    )


def build_proposition_token(latex):
    proposition_character = latex[0]
    proposition = Literal(proposition_character)
    return latex[1:].strip(), proposition


def build_sub_formula_token(latex):
    new_latex, formula = build_formula_token(latex[1:])
    return new_latex[1:].strip(), formula


def build_quantifier_token(latex):
    latex_split = latex.split()
    quantifier_type = latex_split[0]
    quantifier_variable = latex_split[1]

    new_latex = " ".join(latex_split[2:])
    if quantifier_type == quantifier["exists"]:
        return new_latex, ExistentialQuantifier(quantifier_variable)
    else:
        return new_latex, UniversalQuantifier(quantifier_variable)


def build_negation_modifier(latex):
    new_latex = latex.replace(modulator["negation"], "", 1).strip()
    latex, token = extract_next_token(new_latex)
    token.negation = True

    return latex, token


def extract_next_token(latex):
    if is_quantifier_token(latex):
        return build_quantifier_token(latex)
    elif is_negation_modifier_token(latex):
        return build_negation_modifier(latex)
    elif is_predicate_token(latex):
        return build_predicate_token(latex)
    elif is_proposition_token(latex):
        return build_proposition_token(latex)
    elif is_sub_formula_token(latex):
        return build_sub_formula_token(latex)
    elif is_connective_token(latex):
        return build_connective_token(latex)
    else:
        raise Exception("Token inválido")


def build_formula_token(latex):
    formula = Formula()
    while not is_end_of_formula(latex):
        latex, token = extract_next_token(latex)
        formula.append_token(token)

    return latex, formula
