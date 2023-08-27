from IPython.core.display import Math
from IPython.core.display_functions import display
import traceback


from src.builders import build_formula_token
from src.replacers import transform_to_fnd

latex_formulas = [
    r"P(x) \leftrightarrow Q(x)",
    r"P \leftrightarrow (Q \wedge R)",
    r"P \rightarrow (Q \wedge \neg R)",
    r"(P \rightarrow Q) \wedge \neg (R \vee \neg S)",
    r"\exists x (P(x) \vee Q(x)) \wedge \neg \forall y (R(y) \rightarrow S(y))",
    r"\forall x (P(x) \rightarrow Q(x))",
    r"P \leftrightarrow Q \equiv (P \rightarrow Q) \wedge (Q \rightarrow P)",
]


try:
    for latex in latex_formulas[1:2]:
        print(f"Analisando latex: {latex}")
        _, formula = build_formula_token(latex)

        formula = transform_to_fnd(formula)

        # display(Math(latex))
except Exception as e:
    print(f"Erro: {e}")
    traceback.print_exc()
