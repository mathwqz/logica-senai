# pede pro usuário digitar alguma coisa, tipo frase ou número
frase = input("Digite uma expressão: ")

# transforma tudo em minúscula pra não confundir 'A' com 'a'
frase = frase.lower()

# aqui vamos guardar só o que importa: letras e números (sem espaço, vírgula, nada disso)
frase_limpa = ""

# vamos ler a frase uma letra por vez
indice = 0
while indice < len(frase):
    letra = frase[indice]

    # se for uma letra entre 'a' e 'z' ou número entre '0' e '9', a gente aproveita
    if (letra >= 'a' and letra <= 'z') or (letra >= '0' and letra <= '9'):
        frase_limpa = frase_limpa + letra  # vai montando a frase limpinha, letra por letra

    indice = indice + 1  # vai pra próxima letra

# agora vamos inverter a frase limpinha, letra por letra, começando do fim
frase_invertida = ""
indice = len(frase_limpa) - 1  # começa na última letra

while indice >= 0:
    frase_invertida = frase_invertida + frase_limpa[indice]  # vai juntando de trás pra frente
    indice = indice - 1  # vai andando pra trás

# agora a gente vê se a frase original (limpa) é igual à versão ao contrário
if frase_limpa == frase_invertida:
    print('"' + frase + '" é um palíndromo!')
else:
    print('"' + frase + '" não é um palíndromo.')
