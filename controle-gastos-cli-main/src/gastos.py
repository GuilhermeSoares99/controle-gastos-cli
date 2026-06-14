from src.database import supabase


def adicionar_gasto(valor):
    if valor < 0:
        raise ValueError("Valor não pode ser negativo")

    supabase.table("gastos").insert({
        "valor": valor
    }).execute()


def listar_gastos():
    resposta = (
        supabase
        .table("gastos")
        .select("*")
        .execute()
    )

    return resposta.data


def total_gastos():
    resposta = (
        supabase
        .table("gastos")
        .select("valor")
        .execute()
    )

    return sum(item["valor"] for item in resposta.data)