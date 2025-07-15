# pede o número pro usuário
n = int(input("Digite um número inteiro positivo: "))

# verifica se é menor ou igual a 1
if n <= 1:
    print(f"{n} não é uma chave prima válida.")
else:
    eh_primo = True  # assume que é primo até provar o contrário
    i = 2
    while i <= n // 2:
        if n % i == 0:  # se achar um divisor, já era
            eh_primo = False
            break  # para o loop logo, já sabemos que não é primo
        i += 1

    if eh_primo:
        print(f"{n} é uma chave prima válida!")
    else:
        print(f"{n} não é uma chave prima válida.")
