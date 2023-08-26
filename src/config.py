connective = {
    "and": r"\wedge",
    "or": r"\vee",
    "implication": r"\rightarrow",
    "biconditional": r"\leftrightarrow",
    "equivalence": r"\equiv",
}
quantifier = {
    "forall": r"\forall",
    "exists": r"\exists",
}
modulator = {
    "negation": r"\neg",
}

valid_propositions = [
    "p",
    "q",
    "r",
    "s",
    "x",
]
valid_connectives = list(connective.values())
valid_modulators = list(modulator.values())
valid_quantifiers = list(quantifier.values())
valid_variables = [
    "x",
    "y",
    "z",
]
valid_predicates = [
    "P",
    "Q",
    "R",
    "S",
    "X",
]
valid_parentheses = [
    "(",
    ")",
]
