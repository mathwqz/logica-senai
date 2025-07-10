# valor da compra
valor = float(input("digite o valor da compra: "))

# sigla do estado
estado = input("digite a sigla do estado: ").upper()

# verificar se é valido ao desconto
if (estado == "RJ" or estado == "MG") and valor > 200:
    desconto = valor * 10 / 100
    valor_final = valor - desconto
else:
    valor_final = valor

# valor final
print("valor com desconto: r$", valor_final)
