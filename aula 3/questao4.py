# ler a temperatura em celsius
celsius = float(input("digite a temperatura em celsius: "))

# converter para fahrenheit usando a formula
fahrenheit = celsius * 1.8 + 32

# mostrar a temperatura convertida
print(f"{fahrenheit}°f", end=" ")

# verificar se está acima de 100 graus fahrenheit
if fahrenheit > 100:
    print("(alerta: temperatura alta!)")
