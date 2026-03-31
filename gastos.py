from gastos import adicionar_gasto, listar_gastos, total_gastos

def menu():
    while True:
        print("\n1 - Adicionar gasto")
        print("2 - Listar gastos")
        print("3 - Total de gastos")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            valor = float(input("Valor: "))
            adicionar_gasto(valor)
        elif op == "2":
            print(listar_gastos())
        elif op == "3":
            print("Total:", total_gastos())
        elif op == "0":
            break

if __name__ == "__main__":
    menu()
