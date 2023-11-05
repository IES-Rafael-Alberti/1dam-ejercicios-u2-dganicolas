import pytest
from src.P2_2.ej2_2 import años

@pytest.mark.parametrize(
    "n1, expected",
    [
        (0,"has cumplido 0 años."),
        (1,"has cumplido 0 años.\nhas cumplido 1 años."),
        (2,"has cumplido 0 años.\nhas cumplido 1 años.\nhas cumplido 2 años."),
    ]
)
def test_años_params(n1, expected):
    assert años(n1) == expected