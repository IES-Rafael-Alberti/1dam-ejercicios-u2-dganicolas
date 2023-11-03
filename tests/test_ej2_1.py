import pytest
from src.P2_1.ej2_1 import edaad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (1, "felicidades eres menor de edad"),
        (18, "felicidades eres mayor de edad"),
        (100, "felicidades eres mayor de edad"),
        (5, "felicidades eres menor de edad"),
        (17, "felicidades eres menor de edad"),
        (125, "felicidades eres mayor de edad")
    ]
)
def test_edaad_params(input_n, expected):
    assert edaad(input_n) == expected
