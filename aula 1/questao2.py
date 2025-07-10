# dizer as horas trabalhadas no mês
HT = int(input("digite a quantidade de horas trabalhadas no mês: "))

# inserir valor da hora aula
VH = int(input("digite o valor da hora aula: "))

# percentual de desconto do inss
PD = int(input("digite o percentual de desconto do INSS: "))

# calculo do salário bruto
SB = HT * VH

# calcular o desconto (TD = SB * (PD / 100))
TD = SB * PD // 100

# calcular o salário líquido
SL = SB - TD

# apresentar os valores do salario bruto e do salário líquido
print("Salário Bruto: R$", SB)
print("Salário Líquido: R$", SL)
