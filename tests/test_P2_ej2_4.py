import pytest
from src.P2_2.ej2_4 import cuenta

@pytest.mark.parametrize(
    "n1, expected",
    [
        (5,"serie => 5,4,3,2,1,0"),
        (7,"serie => 7,6,5,4,3,2,1,0"),
        (8,"serie => 8,7,6,5,4,3,2,1,0"),
    ]
)
def test_cuenta_params(n1, expected):
    assert cuenta(n1) == expected