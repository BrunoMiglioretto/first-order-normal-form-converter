from src.config import valid_quantifiers, modulator, valid_predicates, valid_variables, valid_propositions, \
    valid_connectives
from src.models import Formula, Quantifier, ExistentialQuantifier, UniversalQuantifier, Predicate, Literal
from src.validators import is_valid_character
from src.config import quantifier


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
        same_characters = [
            character
            for index, character in enumerate(quantifier)
            if latex[index] == character
        ]
        if len(same_characters) == len(quantifier):
            return True

    return False


def is_negation_modifier_token(latex):
    same_characters = [
        character
        for index, character in enumerate(modulator["negation"])
        if latex[index] == character
    ]
    return len(same_characters) == len(modulator["negation"])


def is_proposition_token(latex):
    return latex[0] in valid_propositions


def is_connective_token(latex):
    for connective in valid_connectives:
        same_characters = [
            character
            for index, character in enumerate(connective)
            if latex[index] == character
        ]
        if len(same_characters) == len(connective):
            return True

    return False


def is_sub_formula_token(latex):
    return latex[0] == "("


def build_connective_token(latex):
    pass


def build_predicate_token(latex):
    predicate_character = latex.pop(0)
    variables = [variable.strip() for variable in latex[1:latex.find(")")].split(",")]

    if not variables:
        raise Exception("Predicado sem variaveis")

    invalid_variables = [variable for variable in variables if variable not in valid_variables]
    if invalid_variables:
        raise Exception(f"Variáveis da proposição {predicate_character} estão inválidas: {variables}")

    return latex[latex.find(")") + 2:], Predicate(predicate_character, variables)


def build_proposition_token(latex):
    proposition_character = latex.pop(0)
    proposition = Literal(proposition_character)
    return latex[1:], proposition


def build_sub_formula_token(latex):
    pass


def build_quantifier_token(latex):
    latex_split = latex.split()
    quantifier_type = latex_split[0]
    quantifier_variable = latex_split[1]

    if quantifier_type == quantifier["exists"]:
        return ExistentialQuantifier(quantifier_variable)
    else:
        return UniversalQuantifier(quantifier_variable)


def build_negation_modifier(latex):
    latex_split = latex.split()
    new_latex = " ".join(latex_split.pop(0))
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
        return build_formula(latex)
    elif is_connective_token(latex):
        return build_connective_token(latex)
    else:
        raise Exception("Token inválido")


def build_formula(latex):
    for character in enumerate(latex):
        is_valid_character(character)

    formula = Formula()
    while latex:
        (latex, token) = extract_next_token(latex)
        formula.append_token(token)

    return formula

r"""

A \leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A)
\leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A) 
B \equiv (A \rightarrow B) \wedge (B \rightarrow A) 
\equiv (A \rightarrow B) \wedge (B \rightarrow A) 
(A \rightarrow B) \wedge (B \rightarrow A) 


"""
