import pytest
from src.P2_1.ej2_7 import hacienda_roba_V2

@pytest.mark.parametrize(
    "input_n, expected",
    [
        (999, "te quito un 5% master"),
        (12000, "te quito un 15% master"),
        (32000, "te quito un 20% master"),
        (222222222222222, "te quito un 45% master, y me parece poco"),
        (234, "te quito un 5% master"),
        (40000, "te quito un 30% master"),
    ]
)
def test_hacienda_roba_V2_params(input_n, expected):
    assert hacienda_roba_V2(input_n) == expected
