# ler a estoque
quantidade = int(input("digite a quantidade em estoque: "))

# ler a validade
data_validade = input("digite a data de validade (dd-mm-aaaa): ")

# defini data atual
data_atual = "10-07-2025"

# verificar se tem que repor o produto
if quantidade < 10 or data_validade < data_atual:
    print("repor produto")
