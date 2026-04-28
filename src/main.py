from src.gastos import adicionar_gasto, listar_gastos, total_gastos, total_em_dolar


def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total de gastos")
        print("4 - Total em dólar")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            try:
                valor = float(input("Valor: "))
                adicionar_gasto(valor)
                print("Gasto adicionado com sucesso!")
            except ValueError:
                print("Valor inválido!")
        elif op == "2":
            print("Gastos:", listar_gastos())
        elif op == "3":
            print("Total em BRL:", total_gastos())
        elif op == "4":
            try:
                print("Total em USD:", total_em_dolar())
            except Exception as e:
                print("Erro ao buscar cotação:", e)
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
