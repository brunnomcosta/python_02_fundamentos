# Exemplo de dicionario em Python.
# Dicionario e uma colecao que armazena dados no formato:
# chave: valor
#
# Ele e muito util quando voce quer dar nome para cada informacao.
# Em vez de acessar dados por posicao, como em listas e tuplas,
# no dicionario voce acessa os valores pela chave.
#
# Resumo rapido:
# - dicionario usa {}
# - cada chave aponta para um valor
# - chaves nao podem se repetir
# - valores podem ser de varios tipos (texto, numero, lista, etc.)
# - o dicionario pode ser alterado depois de criado

film_inception = {
    "title": "Inception",
    "year_release": 2010,
    "imdb_rating": 8.8,
    "genres": ["Sci-Fi", "Action", "Thriller"],
}

# Exibe o dicionario completo.
print(film_inception)

# len() mostra quantos pares chave:valor existem no dicionario.
print(len(film_inception))

# Mostra o tipo da variavel.
print(type(film_inception))

# 1. Acessar valores pela chave.
# Quando a chave existe, podemos usar colchetes.
print(film_inception["genres"])

# get() tambem busca um valor pela chave.
# Ele e util porque evita erro se a chave nao existir.
print(film_inception.get("imdb_rating"))

# Tambem e possivel definir um valor padrao para chaves inexistentes.
print(film_inception.get("director", "Diretor nao cadastrado"))

# 2. Acessar um valor dentro de uma lista armazenada no dicionario.
# Aqui mostramos apenas o primeiro genero do filme.
print(film_inception["genres"][0])

# 3. keys() retorna todas as chaves do dicionario.
print(film_inception.keys())

# 4. values() retorna todos os valores do dicionario.
print(film_inception.values())

# 5. items() retorna chave e valor juntos.
print(film_inception.items())

# 6. Adicionar um novo item.
# Se a chave ainda nao existir, ela sera criada.
film_inception["director"] = "Christopher Nolan"
print(film_inception)

# 7. Atualizar um item existente.
# update() altera o valor de uma chave ja existente
# ou cria a chave, se ela ainda nao existir.
film_inception.update({"imdb_rating": 8.7})
print(film_inception)

# 8. Verificar se uma chave existe.
print("director" in film_inception)
print("duration" in film_inception)

# 9. Remover um item com pop().
# pop() remove a chave informada e retorna o valor removido.
removed_director = film_inception.pop("director")
print(removed_director)
print(film_inception)
