# função que mostra o menu toda vez que o loop roda
def mostrar_menu():
    print("\nmenu:")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - calcular desconto (10%)")
    print("6 - sair")

# loop infinito até o usuário escolher sair (opção 6)
while True:
    mostrar_menu()  # chama o menu
    opcao = input("escolhe uma opção ae: ")  # lê a opção que o usuário escolheu

    # se escolher 1, faz soma
    if opcao == "1":
        a = float(input("digite o primeiro número: "))  # lê primeiro número
        b = float(input("digite o segundo número: "))   # lê segundo número
        print(f"resultado: {a + b}")  # mostra o resultado da soma

    # se escolher 2, faz subtração
    elif opcao == "2":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        print(f"resultado: {a - b}")

    # se escolher 3, faz multiplicação
    elif opcao == "3":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        print(f"resultado: {a * b}")

    # se escolher 4, faz divisão
    elif opcao == "4":
        a = float(input("digite o primeiro número: "))
        b = float(input("digite o segundo número: "))
        if b == 0:
            print("divisão por zero não tá tendo")  # não divide por zero
        else:
            print(f"resultado: {a / b}")  # se tudo certo, mostra o resultado

    # se escolher 5, calcula 10% de desconto
    elif opcao == "5":
        valor = float(input("digite o valor total: "))  # valor original
        desconto = valor * 0.10  # calcula 10% de desconto
        final = valor - desconto  # valor com desconto aplicado
        print(f"valor com desconto: R$ {final:.2f}")  # mostra o valor formatado com 2 casas decimais

    # se escolher 6, encerra o programa
    elif opcao == "6":
        print("cabou a brincadeira, flw")  # mensagem de saída
        break  # sai do loop e finaliza

    # se digitou algo que não existe no menu
    else:
        print("opção inválida, sua anta, escolhe direito.")
