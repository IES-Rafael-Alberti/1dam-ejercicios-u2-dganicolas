import pytest
from src.P2_1.ej2_4 import parimpar

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (2, "el numero es par"),
        (1, "el numero es impar"),
        (9, "el numero es impar"),
        (3, "el numero es impar"),
        (8, "el numero es par"),
        (4, "el numero es par"),
        (6, "el numero es par")
    ]
)
def test_parimpar_params(input_n, expected):
    assert parimpar(input_n) == expected
