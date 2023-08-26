from src.config import (
    valid_quantifiers,
    valid_propositions,
    valid_connectives,
    valid_modulators,
    valid_variables,
    valid_predicates,
    valid_parentheses,
)


def is_valid_character(character):
    if (
        character not in valid_propositions
        and character not in valid_connectives
        and character not in valid_modulators
        and character not in valid_quantifiers
        and character not in valid_variables
        and character not in valid_predicates
        and character not in valid_parentheses
    ):
        raise Exception(f"Caracter inválido: {character}")


def is_valid_quantifier(index, tokens):
    if len(tokens) == index + 1:
        raise Exception("Quantificador no final da formula")


def is_valid_connective(index, tokens):
    try:
        previous_token_index = index - 1
        next_token_index = index + 1

        if (
            not is_predicate(previous_token_index, tokens)
            and not is_proposition(previous_token_index, tokens)
        ) or (
            not is_predicate(next_token_index, tokens)
            and not is_proposition(next_token_index, tokens)
        ):
            raise Exception(
                "Tanto o token a esquerda quanto da direita precisão ser ou proposições ou predicados."
            )
    except IndexError:
        raise Exception("Uma fórmula não pode iniciar ou finalizar com um conectivo.")


def is_valid_predicate(index, tokens):
    pass


def is_valid_modulator(index, tokens):
    pass


def is_valid_variable(index, tokens):
    pass
