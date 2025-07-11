# ler a velocidade do veiculo
velocidade = int(input("digite a velocidade em km/h: "))

# verificar se passou do limite de 80km/h
if velocidade > 80:
    km_excedido = velocidade - 80
    multa = 200 + (km_excedido * 5)
    print("multa: r$", multa)
else:
    print("velocidade ok, sem multa")
