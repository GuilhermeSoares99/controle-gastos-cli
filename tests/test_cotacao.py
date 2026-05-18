import requests


def test_api_cotacao():
    response = requests.get(
        "https://open.er-api.com/v6/latest/USD"
    )

    assert response.status_code == 200

    dados = response.json()

    assert "rates" in dados
    assert "BRL" in dados["rates"]