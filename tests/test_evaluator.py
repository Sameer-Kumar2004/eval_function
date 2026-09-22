from src.eval_function.evaluator import evaluate_expression


def test_addition():
    assert evaluate_expression("10 + 20") == 30