# perguntar o estado da pessoa
estado = input("digite seu estado (sigla ex: sp): ").lower()

# perguntar quanto ela gastou
compra = float(input("digite o valor da compra: "))

# se for SP ou MG e a compra for maior que 100, o frete é grátis
if (estado == "sp" or estado == "mg") and compra > 100:
    frete = 0
else:
    frete = 30

# mostrar o valor do frete
print("frete: r$", frete)
