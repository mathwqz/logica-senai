# ler o peso em kg
peso = float(input("digite seu peso em kg: "))

# ler a altura em metros
altura = float(input("digite sua altura em metros: "))

# calcular o imc com a formula: peso dividido por altura ao quadrado
imc = peso / (altura * altura)

# mostrar o valor do imc com classificacao
print("imc:", round(imc, 2))

if imc < 18.5:
    print("abaixo do peso")
elif imc <= 24.9:
    print("normal")
else:
    print("sobrepeso")
