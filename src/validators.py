from src.config import (
    valid_quantifiers,
    valid_propositions,
    valid_connectives,
    valid_modulators,
    valid_variables,
    valid_predicates,
    valid_parentheses,
)
from src.models import Formula, Connective, Predicate, Quantifier, Literal


def is_valid_character(character):
    if (
        character not in valid_propositions
        and character not in valid_connectives
        and character not in valid_modulators
        and character not in valid_quantifiers
        and character not in valid_variables
        and character not in valid_predicates
        and character not in valid_parentheses
        and character not in [" ", "\\"]
    ):
        raise Exception(f"Caracter inválido: {character}")


def validate_formula(formula):
    for index, token in enumerate(formula.tokens):
        if isinstance(index, Formula):
            validate_formula(formula)
        elif isinstance(token, Connective):
            validate_connective(index, formula)
        elif isinstance(token, Predicate):
            validate_predicate(index, formula)
        elif isinstance(token, Quantifier):
            validate_quantifier(index, formula)
        elif isinstance(token, Literal):
            validate_literal(index, formula)


def validate_literal(index, formula):
    try:
        if index == 0:
            return

        previous_token = formula.tokens[index - 1]
        if (
            isinstance(previous_token, Quantifier)
            or isinstance(previous_token, Literal)
            or isinstance(previous_token, Formula)
            or isinstance(previous_token, Predicate)
        ):
            raise Exception("Literal inválido")
    except IndexError:
        pass
    finally:
        try:
            next_token = formula.tokens[index + 1]
            if (
                isinstance(next_token, Quantifier)
                or isinstance(next_token, Literal)
                or isinstance(next_token, Formula)
                or isinstance(next_token, Predicate)
            ):
                raise Exception("Literal inválido")
        except IndexError:
            pass


def validate_quantifier(index, formula):
    try:
        if index == 0:
            return

        previous_token = formula.tokens[index - 1]
        if (
            isinstance(previous_token, Literal)
            or isinstance(previous_token, Formula)
            or isinstance(previous_token, Predicate)
        ):
            raise Exception("Quantificador inválido")
    except IndexError:
        pass
    finally:
        try:
            next_token = formula.tokens[index + 1]
            if isinstance(next_token, Literal) or isinstance(next_token, Connective):
                raise Exception("Quantificador inválido")
        except IndexError:
            pass


def validate_connective(index, formula):
    try:
        previous_token = formula.tokens[index - 1]
        next_token = formula.tokens[index + 1]

        if (
            not isinstance(previous_token, Predicate)
            and not isinstance(previous_token, Literal)
            and not isinstance(previous_token, Formula)
        ) or (
            not isinstance(next_token, Predicate)
            and not isinstance(next_token, Literal)
            and not isinstance(next_token, Formula)
            and not isinstance(next_token, Quantifier)
        ):
            raise Exception(
                "Tanto o token a esquerda quanto da direita precisão ser ou proposições ou predicados ou uma subformula"
            )
    except IndexError:
        raise Exception("Uma fórmula não pode iniciar ou finalizar com um conectivo.")


def validate_predicate(index, formula):
    try:
        if index == 0:
            return

        previous_token = formula.tokens[index - 1]
        if (
            isinstance(previous_token, Literal)
            or isinstance(previous_token, Formula)
            or isinstance(previous_token, Predicate)
        ):
            raise Exception("Predicado inválido")
    except IndexError:
        pass
    finally:
        try:
            next_token = formula.tokens[index + 1]
            if not isinstance(next_token, Connective):
                raise Exception("Predicado inválido")
        except IndexError:
            pass
