import pytest
from src.P2_1.ej2_2 import seguridad

@pytest.mark.parametrize(
    "input_n, expected",
    [
        ('hola', "felicidades sabes la contraseña"),
        ('admin', "felicidades sabes la contraseña"),
        ('contraseña', "felicidades sabes la contraseña"),
        ("nicolas", "master no te la sabes"),
        ("smr", "master no te la sabes"),
        ("ivan", "master no te la sabes")
    ]
)
def test_seguridad_params(input_n, expected):
    assert seguridad(input_n) == expected
