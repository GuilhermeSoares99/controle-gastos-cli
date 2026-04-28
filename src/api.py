import requests

def get_dolar():
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erro ao acessar API")

    data = response.json()
    return data["rates"]["USD"]
