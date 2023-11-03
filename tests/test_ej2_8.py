import pytest
from src.P2_1.ej2_8 import depresion

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (0.2, 2880.0),
        (0.1, 2640.0),
        (0.7, 8880.0),
        (0.3, 3120.0),
        (0.8, 9120.0),
        (1.0, 9600.0),
    ]
)
def test_depresion_params(input_n, expected):
    assert depresion(input_n) == expected
