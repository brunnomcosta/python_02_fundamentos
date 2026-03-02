# Exemplo de list comprehension em Python.
# List comprehension e uma forma curta e pratica de criar listas
# a partir de outras listas, strings, ranges ou qualquer iteravel.
#
# Estrutura mais comum:
# [expressao for item in iteravel]
#
# Quando queremos filtrar valores:
# [expressao for item in iteravel if condicao]
#
# Quando queremos decidir entre dois valores:
# [valor_se_verdadeiro if condicao else valor_se_falso for item in iteravel]

# -----------------------------------------------
# Exemplo 1: comparando for tradicional com a forma curta
# -----------------------------------------------
# Objetivo: criar uma lista com os numeros menores que 4.

numeros_menores_que_quatro = []

for numero in range(10):
    if numero < 4:
        numeros_menores_que_quatro.append(numero)

print("Com for tradicional:")
print(numeros_menores_que_quatro)

numeros_comprehension = [numero for numero in range(10) if numero < 4]

print("\nCom list comprehension:")
print(numeros_comprehension)


# --------------------------------
# Exemplo 2: transformar valores
# --------------------------------
# Aqui, criamos uma nova lista com o quadrado de cada numero.

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]

print("\nQuadrado de cada numero:")
print(quadrados)


# --------------------------------
# Exemplo 3: filtrar textos
# --------------------------------
# Este exemplo seleciona apenas os filmes que possuem a letra "e".

filmes = [
    "The Matrix",
    "Inception",
    "Interstellar",
    "Pulp Fiction",
    "Avatar",
]

filmes_com_letra_e = [filme for filme in filmes if "e" in filme.lower()]

print("\nFilmes com a letra 'e':")
print(filmes_com_letra_e)


# ----------------------------------------------------
# Exemplo 4: usar if/else dentro da comprehension
# ----------------------------------------------------
# Diferenca importante:
# - "if" no final filtra elementos
# - "if/else" no inicio escolhe qual valor sera colocado na lista

notas = [8.5, 6.0, 9.2, 7.0, 5.8]
situacoes = ["Aprovado" if nota >= 7 else "Revisar" for nota in notas]

print("\nSituacao de cada nota:")
print(situacoes)


# ---------------------------------------------
# Exemplo 5: busca simples em uma lista
# ---------------------------------------------
# O usuario digita um trecho do nome do filme.
# A list comprehension devolve todos os filmes que combinam com a busca.

termo_busca = input("\nDigite um trecho do nome do filme para buscar:\n").strip()

if termo_busca:
    filmes_encontrados = [
        filme for filme in filmes if termo_busca.lower() in filme.lower()
    ]

    print("\nResultado da busca:")

    if filmes_encontrados:
        print(filmes_encontrados)
    else:
        print("Nenhum filme foi encontrado.")
else:
    print("\nNenhum termo foi digitado.")
