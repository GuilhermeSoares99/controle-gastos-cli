import json
import os

FILE = "gastos.json"


def carregar():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def salvar(gastos):
    with open(FILE, "w") as f:
        json.dump(gastos, f)


def adicionar_gasto(valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")
    gastos = carregar()
    gastos.append(valor)
    salvar(gastos)


def listar_gastos():
    return carregar()


def total_gastos():
    return sum(carregar())
