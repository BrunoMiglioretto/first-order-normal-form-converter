from IPython.core.display import Math
from IPython.core.display_functions import display

from src.builders import build_formula

latex_formulas = [
    r"\neg P(x) \wedge Q(x)",
    r"P \rightarrow ( Q \wedge R )",
    r"P \rightarrow (Q \wedge \neg R)",
    r"(P \rightarrow Q) \wedge \neg (R \vee \neg S)",
    r"\exists x (P(x) \vee Q(x)) \wedge \neg \forall y (R(y) \rightarrow S(y))",
    r"\forall x (P(x) \rightarrow Q(x))",
    r"A \leftrightarrow B \equiv (A \rightarrow B) \wedge (B \rightarrow A)",
]


try:
    for latex in latex_formulas:
        print(f"Analisando latex: {latex}")
        formula = build_formula(latex)

        # formula_fnd = build_formula_fnd(formula)
        # formula_fnc = build_formula_fnc(formula)

        display(Math(latex))
except Exception as e:
    print(f"Erro: {e}")
