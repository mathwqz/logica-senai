def mostrar_menu():
    print("\nmenu:")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - calcular desconto (10%)")
    print("6 - sair")

while True:
    mostrar_menu()
    opcao = input("escolhe uma opção ae: ")

    if opcao == "1":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        print(f"resultado: {a + b}")

    elif opcao == "2":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        print(f"resultado: {a - b}")

    elif opcao == "3":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        print(f"resultado: {a * b}")

    elif opcao == "4":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        if b == 0:
            print("divisão por zero não tá tendo")
        else:
            print(f"resultado: {a / b}")

    elif opcao == "5":
        valor = float(input("digite o valor total: "))
        desconto = valor * 0.10
        final = valor - desconto
        print(f"valor com desconto: R$ {final:.2f}")

    elif opcao == "6":
        print("cabou a brincadeira, flw")
        break

    else:
        print("opção inválida, sua anta, escolhe direito.")
