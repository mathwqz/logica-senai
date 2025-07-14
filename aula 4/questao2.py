# perguntar a cor do semáforo
cor = input("digite a cor do semaforo (verde/amarelo/vermelho): ").lower()

# perguntar a velocidade do carro
velocidade = int(input("digite a velocidade do carro: "))

# se a cor nao for verde e a velocidade for maior que 60, o carro leva multa
if cor != "verde" and velocidade > 60:
    print("multa aplicada")
else:
    print("sem multa")
