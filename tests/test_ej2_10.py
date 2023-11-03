import pytest
from src.P2_1.ej2_10 import pizzeria

@pytest.mark.parametrize(
    "n1, n2, expected",
    [
        ("vegana","pimiento", "tu pizza es vegana y tiene tomate, mozarella y pimiento"),
        ("vegana","tofu", "tu pizza es vegana y tiene tomate, mozarella y tofu"),
        ("no vegana","jamón", "tu pizza no es vegana y tiene tomate, mozarella y jamón"),
        ("no vegana","Peperoni", "tu pizza no es vegana y tiene tomate, mozarella y Peperoni"),
        ("no vegana","Salmón", "tu pizza no es vegana y tiene tomate, mozarella y Salmón"),
    ]
)
def test_pizzeria_params(n1,n2, expected):
    assert pizzeria(n1,n2) == expected