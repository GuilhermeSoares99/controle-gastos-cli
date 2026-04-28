from src.api import get_dolar

def test_api():
    valor = get_dolar()
    assert valor > 0
