# ler a idade do usuario
idade = int(input("digite sua idade: "))

# ler a altura do usuario
altura = float(input("digite sua altura (ex: 1.70): "))

# verificar se a pessoa pode tirar a cnh
if idade >= 18 and altura >= 1.50:
    print("pode iniciar o processo!")
else:
    print("nao atende aos requisitos")
