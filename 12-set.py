# Exemplo de set em Python.
# Set e uma colecao NAO ordenada, mutavel e sem valores duplicados.
#
# Isso significa que:
# - a ordem de exibicao pode mudar
# - itens repetidos sao removidos automaticamente
# - voce pode adicionar e remover elementos depois da criacao
#
# Comparacao rapida:
# - lista: usa [], preserva ordem e aceita repeticao
# - tupla: usa (), preserva ordem, aceita repeticao e e imutavel
# - set: usa {}, nao garante ordem e nao aceita repeticao
#
# Em resumo:
# - use lista quando a ordem importa e os dados podem se repetir
# - use tupla quando a ordem importa e os dados nao devem mudar
# - use set quando voce quer valores unicos e operacoes de conjunto

films_set = {
    "Inception",
    "The Shawshank Redemption",
    "The Dark Knight",
    "Pulp Fiction",
    "Interstellar",
}

# Mostra o tipo da variavel.
print(type(films_set))

# 1. len() mostra quantos elementos existem no set.
print(len(films_set))

# 2. Valores duplicados sao ignorados automaticamente.
genres_set = {"Drama", "Drama", "Action", "Sci-Fi", "Sci-Fi"}
print(genres_set)

# 3. True e 1 sao considerados o mesmo valor em set.
# Isso acontece porque, em Python, True equivale a 1.
example_set = {"Inception", True, 1, 8.7}
print(example_set)

# 4. add() adiciona um unico item.
films_set.add("Fight Club")
print(films_set)

# 5. update() adiciona varios itens de outro set (ou de outra colecao).
# Se algum item ja existir, ele nao sera repetido.
more_films = {"The Matrix", "Se7en", "Interstellar"}
films_set.update(more_films)
print(films_set)

# 6. remove() apaga um item especifico.
# Se o valor nao existir, remove() gera erro.
films_set.remove("Se7en")
print(films_set)

# 7. discard() tambem remove um item, mas nao gera erro se ele nao existir.
films_set.discard("Avatar")
print(films_set)

# 8. Sets sao muito usados para eliminar repeticoes de listas e tuplas.
# Essa e uma forma simples de obter apenas valores unicos.
movies_list = ["Inception", "Inception", "Pulp Fiction", "Interstellar"]
movies_tuple = ("Drama", "Drama", "Sci-Fi", "Sci-Fi")

print(set(movies_list))
print(set(movies_tuple))

# 9. Operacoes de conjunto.
# Esses metodos sao muito uteis para comparar grupos de dados.
action_movies = {"Inception", "The Matrix", "John Wick"}
classic_movies = {"Pulp Fiction", "The Matrix", "The Godfather"}

# intersection(): itens que existem nos dois sets.
print(action_movies.intersection(classic_movies))

# union(): junta todos os itens sem repetir.
print(action_movies.union(classic_movies))

# difference(): itens que existem so no primeiro set.
print(action_movies.difference(classic_movies))
