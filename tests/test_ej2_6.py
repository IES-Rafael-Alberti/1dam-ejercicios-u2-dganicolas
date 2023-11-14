import pytest
from src.P2_1.ej2_6 import grupo

@pytest.mark.parametrize(
    "n1, n2, expected",
    [
        ("hombre","carlos", "perteneces al grupo B"),
        ("mujer","antonia", "perteneces al grupo A"),
        ("hombre","julio", "perteneces al grupo B"),
        ("mujer","laura", "perteneces al grupo A"),
        ("hombre","diego", "perteneces al grupo B"),
        ("mujer","ana", "perteneces al grupo A"),
        ("hombre","paco", "perteneces al grupo A"),
        ("mujer","carla", "perteneces al grupo A"),
        ("hombre","cesar", "perteneces al grupo B"),
    ]
)
def test_grupo_params(n1,n2, expected):
    assert grupo(n1,n2) == expected
