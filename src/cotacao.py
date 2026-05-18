import requests


def obter_cotacao_dolar():
    url = "https://open.er-api.com/v6/latest/USD"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            dados = response.json()
            return dados["rates"]["BRL"]

        return None

    except Exception:
        return None