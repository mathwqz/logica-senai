# senha
senha = input("digite a senha: ")

# a senha tem pelo menos 8 caracteres?
comprimento_valido = len(senha) >= 8

# tem pelo menos um numero?
tem_numero = any(c.isdigit() for c in senha)

# tem pelo menos uma letra maiuscula?
tem_maiuscula = any(c.isupper() for c in senha)

# nao tem espaço em branco?
nao_tem_espaco = " " not in senha

# verifica se todos os criterios foram atendidos
if comprimento_valido and tem_numero and tem_maiuscula and nao_tem_espaco:
    print("senha valida")
else:
    print("senha fraca")
