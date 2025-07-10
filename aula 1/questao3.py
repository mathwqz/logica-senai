# definir uma variavel para o salário reajustado: novo_salario;
novo_salario = 0

# ler um valor para a variavel salario;
salario = int(input("digite o salário atual do funcionario: "))

# verificar se o valor do salario < 500, se sim reajustar em 15%;
if salario < 500:
    novo_salario = salario + (salario * 15 // 100)

# verificar se o valor do salario <= 1000, se sim reajustar em 10%;
if salario >= 500 and salario <= 1000:
    novo_salario = salario + (salario * 10 // 100)

# verificar se o valor do salario > 1000, se sim reajustar em 5%;
if salario > 1000:
    novo_salario = salario + (salario * 5 // 100)

# apresentar o valor reajustado implicando em novo_salario
print("o salário reajustado é: r$", novo_salario)
