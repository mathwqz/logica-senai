# pedir a idade da pessoa
idade = int(input("digite sua idade: "))

# pedir o email dela
email = input("digite seu e-mail: ")

# pedir a senha que ela quer usar
senha = input("digite sua senha: ")

# agora vamos ver se ela pode se cadastrar
# tem que ter 13 anos ou mais
# o email tem que ter o @
# a senha tem que ter mais que 6 letras

if idade >= 13 and "@" in email and len(senha) > 6:
    print("cadastro aprovado!")
else:
    print("dados invalidos")
