from gastos import adicionar_gasto, listar_gastos, total_gastos
from cotacao import obter_cotacao_dolar


def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total de gastos")
        print("4 - Ver cotação do dólar")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            valor = float(input("Valor: "))
            adicionar_gasto(valor)

        elif op == "2":
            print(listar_gastos())

        elif op == "3":
            print("Total:", total_gastos())

        elif op == "4":
            cotacao = obter_cotacao_dolar()

            if cotacao:
                print(f"Cotação atual do dólar: R$ {cotacao:.2f}")
            else:
                print("Erro ao buscar cotação.")

        elif op == "0":
            break


if __name__ == "__main__":
    menu()