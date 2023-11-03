import pytest
from src.P2_2.ej2_1 import palabr

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ("hola", "hola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\nhola\n"),
        ("pito", "pito\npito\npito\npito\npito\npito\npito\npito\npito\npito\n"),
        ("ayuda", "ayuda\nayuda\nayuda\nayuda\nayuda\nayuda\nayuda\nayuda\nayuda\nayuda\n"),
        ("por favor", "por favor\npor favor\npor favor\npor favor\npor favor\npor favor\npor favor\npor favor\npor favor\npor favor\n"),
        ("pytest shit", "pytest shit\npytest shit\npytest shit\npytest shit\npytest shit\npytest shit\npytest shit\npytest shit\npytest shit\npytest shit\n"),
    ]
)
def test_palabr_params(input_n, expected):
    assert palabr(input_n) == expected
