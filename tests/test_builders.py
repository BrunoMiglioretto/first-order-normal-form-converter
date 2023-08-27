from src.builders import (
    is_quantifier_token,
    is_negation_modifier_token,
    is_connective_token,
)


def test_is_quantifier_token():
    latex = r"\forall x (P(x) \rightarrow Q(x))"

    assert is_quantifier_token(latex)


def test_is_negation_token():
    latex = r"\neg \forall x (P(x) \rightarrow Q(x))"

    assert is_negation_modifier_token(latex)


def test_is_connective_token():
    latex = r"\rightarrow Q(x))"

    assert is_connective_token(latex)
