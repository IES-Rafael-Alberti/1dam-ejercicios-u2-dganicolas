import pytest
from src.P2_1.ej2_9 import cuanto_dinero

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (10, "tu pagas 5€"),
        (23, "tu pagas 10€"),
        (3, "tu entras gratis"),
        (5, "tu pagas 5€"),
        (58, "tu pagas 10€"),
    ]
)
def test_cuanto_dinero_params(input_n, expected):
    assert cuanto_dinero(input_n) == expected
