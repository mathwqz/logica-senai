# perguntar quanto deu a compra
valor = float(input("digite o valor total da compra: "))

# perguntar a regiao da pessoa
regiao = input("digite sua regiao (norte/nordeste/sul/sudeste/centro-oeste): ").lower()

# se a compra passar de 200, ganha desconto de 10%
if valor > 200:
    desconto = valor * 0.10
else:
    desconto = 0

# se for da regiao sul ou sudeste, o frete é gratis
if regiao == "sul" or regiao == "sudeste":
    frete = 0
else:
    frete = 20

# calcular o valor total com desconto e frete
total = valor - desconto + frete

# mostrar o total final
print("total da compra: r$", total)
