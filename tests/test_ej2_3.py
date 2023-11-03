import pytest
from src.P2_1.ej2_3 import division1

@pytest.mark.parametrize(
    "n1, n2, expected",
    [
        (2,0, 0),
        (4,0, 0),
        (4 ,2 ,2 ),
        (9 ,3 , 3)
    ]
)
def test_division1_params(n1,n2, expected):
    assert division1(n1,n2) == expected
