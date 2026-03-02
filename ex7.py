# Exercicio 7 - Tupla
# O programa:
# 1. le o nome de 3 cidades
# 2. guarda os nomes em uma tupla
# 3. mostra a tupla completa
# 4. mostra o ultimo elemento
# 5. mostra a quantidade de elementos
#
# Observacao:
# A tupla e usada aqui porque o exercicio quer apenas armazenar
# os valores lidos, sem necessidade de alteracao depois.

# Le as tres cidades digitadas pelo usuario.
city1 = input()
city2 = input()
city3 = input()

# Cria uma tupla com as tres cidades.
# Como a tupla e ordenada, a posicao de cada cidade e preservada.
cities = (city1, city2, city3)

# Exibe a tupla completa.
print(cities)

# Exibe o ultimo item da tupla.
print(cities[-1])

# Exibe a quantidade de itens da tupla.
print(len(cities))
