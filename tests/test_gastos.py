import pytest
from src.gastos import adicionar_gasto, total_gastos

def test_adicionar_valido():
    adicionar_gasto(10)
    assert total_gastos() >= 10

def test_valor_negativo():
    with pytest.raises(ValueError):
        adicionar_gasto(-1)

def test_total():
    adicionar_gasto(5)
    assert total_gastos() >= 5
