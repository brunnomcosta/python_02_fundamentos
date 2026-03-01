# Exemplo de tupla em Python.
# Tupla e uma colecao ordenada de valores, parecida com lista.
# A principal diferenca e que a tupla e imutavel:
# depois de criada, seus itens nao podem ser alterados, adicionados ou removidos.
# Diferenca para a lista:
# - lista usa [] e pode ser alterada
# - tupla usa () e nao pode ser alterada depois de criada
# Em resumo: lista serve para dados que mudam; tupla, para dados fixos.
# Ela normalmente e usada quando os dados devem permanecer fixos.

filmsTuple = (
    "Inception",
    "The Shawshank Redemption",
    "The Dark Kgnith",
    "Pulp Fiction",
    "Interstellar",
)

# Mostra o tipo da variavel para confirmar que e uma tupla.
print(type(filmsTuple))

# Como a tupla e ordenada, os itens podem ser acessados por indice e slice.

# 1. Busca os dois primeiros itens da tupla.
print(filmsTuple[:2])

# 2. Busca o ultimo item da tupla.
print(filmsTuple[-1])

# 3. Busca os filmes ate uma determinada posicao.
# O indice final nao entra no resultado.
print(filmsTuple[:3])

# 4. Busca os filmes a partir de uma posicao em diante.
print(filmsTuple[2:])

# 5. index(valor) retorna a posicao do item informado.
print(filmsTuple.index("Pulp Fiction"))
