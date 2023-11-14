import pytest
from src.P2_2.ej2_3 import impar

@pytest.mark.parametrize(
    "n1, expected",
    [
        (5,"impar => 0,1,3,5"),
        (7,"impar => 0,1,3,5,7"),
        (8,"impar => 0,1,3,5,7"),
    ]
)
def test_impar_params(n1, expected):
    assert impar(n1) == expected