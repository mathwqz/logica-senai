# pedir a idade da pessoa
idade = int(input("digite sua idade: "))

# pedir o email dela
email = input("digite seu e-mail: ")

# pedir a senha que ela quer usar
senha = input("digite sua senha: ")

# regras:
# tem que ter 13 anos ou mais
# o email tem que ter o @ e .com
# o email deve estar todo em letras minúsculas
# a senha tem que ter mais que 6 caracteres

if idade >= 13 and "@" in email and ".com" in email and len(senha) > 6 and email == email.lower():
    print("cadastro aprovado!")
else:
    print("dados invalidos")
