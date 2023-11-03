import pytest
from src.P2_1.ej2_5 import hacienda

@pytest.mark.parametrize(
    "input_n,input_n2, expected",
    [
        (2 , 33, "no tienes que pagar el impuesto"),
        (19 , 253, "no tienes que pagar el impuesto"),
        (34, 12233, "tienes que pagar el impuesto"),
        (23, 233, "no tienes que pagar el impuesto"),
        (78, 17233, "tienes que pagar el impuesto"),
        (12, 233, "no tienes que pagar el impuesto"),
        (17, 233, "no tienes que pagar el impuesto"),
        (1, 10233, "no tienes que pagar el impuesto"),
        (23 , 133, "no tienes que pagar el impuesto"),
    ]
)
def test_hacienda_params(input_n,input_n2, expected):
    assert hacienda(input_n,input_n2) == expected
