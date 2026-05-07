from calculadora import suma

def test_suma_positivos():
    assert suma(2, 3) == 5

from calculadora import resta

def test_resta_positivos():
    assert resta(5, 3) == 2

from calculadora import multiplicacion

def test_multiplicacion_positivos():
    assert multiplicacion(4, 5) == 20

from calculadora import division

def test_division_positivos():
    assert division(10, 2) == 5

import pytest

def test_division_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        division(5, 0)