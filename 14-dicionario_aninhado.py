import pprint

# Exemplo de dicionario aninhado em Python.
# Um dicionario aninhado e um dicionario que guarda outros dicionarios
# como valor. Isso e util para organizar dados mais completos, como um
# catalogo de filmes, alunos, produtos ou usuarios.
#
# Estrutura geral:
# {
#     "chave_principal": {
#         "subchave": "valor",
#         "outra_subchave": ["lista", "de", "valores"]
#     }
# }

catalogo_filmes = {
    "inception": {
        "titulo": "Inception",
        "ano_lancamento": 2010,
        "nota_imdb": 8.8,
        "generos": ["Sci-Fi", "Action", "Thriller"],
    },
    "interstellar": {
        "titulo": "Interstellar",
        "ano_lancamento": 2014,
        "nota_imdb": 8.6,
        "generos": ["Sci-Fi", "Drama"],
    },
    "the_dark_knight": {
        "titulo": "The Dark Knight",
        "ano_lancamento": 2008,
        "nota_imdb": 9.0,
        "generos": ["Action", "Drama", "Crime"],
    },
}

# pprint deixa a exibicao mais organizada quando a estrutura e grande.
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

print("Catalogo completo:")
pp.pprint(catalogo_filmes)

# 1. Acessar um valor dentro do dicionario interno.
print("\nGeneros de Interstellar:")
print(catalogo_filmes["interstellar"]["generos"])

# Tambem podemos acessar um item da lista que esta dentro do dicionario.
print("\nPrimeiro genero de Inception:")
print(catalogo_filmes["inception"]["generos"][0])

# 2. Adicionar uma nova informacao a um item ja existente.
catalogo_filmes["inception"]["diretor"] = "Christopher Nolan"
print("\nInception apos adicionar o diretor:")
pp.pprint(catalogo_filmes["inception"])

# 3. Adicionar uma nova estrutura aninhada.
catalogo_filmes["interstellar"]["streaming"] = {
    "disponivel": True,
    "plataforma": "Max",
}
print("\nInterstellar com dados de streaming:")
pp.pprint(catalogo_filmes["interstellar"])

# 4. Atualizar um valor dentro do dicionario aninhado.
catalogo_filmes["the_dark_knight"]["nota_imdb"] = 9.1
print("\nNota atualizada de The Dark Knight:")
print(catalogo_filmes["the_dark_knight"]["nota_imdb"])

# 5. Remover uma chave interna com pop().
streaming_removido = catalogo_filmes["interstellar"].pop("streaming")
print("\nDados de streaming removidos:")
print(streaming_removido)
print(catalogo_filmes["interstellar"])

# 6. Remover um item completo do dicionario principal.
filme_removido = catalogo_filmes.pop("the_dark_knight")
print("\nFilme removido do catalogo:")
print(filme_removido["titulo"])

print("\nCatalogo final:")
pp.pprint(catalogo_filmes)
