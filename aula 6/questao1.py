# aqui a gente pede pro usuário digitar qualquer frase ou número
expressao_original = input("Digite uma expressão: ")

# transforma tudo em letra minúscula pra evitar problema com maiúsculas (tipo 'A' e 'a')
expressao_formatada = expressao_original.lower()

# agora a gente vai preparar a frase limpinha, sem espaço, sem pontuação, só com letra ou número
caracteres_validos = ""

# vai passar letra por letra da frase
for caractere in expressao_formatada:
    # só vai guardar se for letra ou número (ignora espaço, vírgula, etc)
    if caractere.isalnum():  # esse isalnum só serve pra checar se é letra ou número mesmo
        caracteres_validos += caractere  # vai montando a frase limpinha, uma letra de cada vez

# agora que a frase tá limpa, a gente compara ela com ela mesma ao contrário
# se for igual, é palíndromo
if caracteres_validos == caracteres_validos[::-1]:  # esse [::-1] aqui inverte a frase
    print(f'"{expressao_original}" é um palíndromo!')
else:
    print(f'"{expressao_original}" não é um palíndromo.')
