# temperatura do paciente
temperatura = float(input("digite a temperatura: "))

# verificar dor de cabeça intensa
dor_de_cabeca = input("dor de cabeça intensa? (true/false): ") == "true"

# pressão arterial
pressao = int(input("digite a pressão arterial sistolica: "))

# verificar o caso de prioridade
if (temperatura > 39 and dor_de_cabeca) or pressao > 140:
    print("prioridade maxima")
else:
    print("aguarde avaliacao")
