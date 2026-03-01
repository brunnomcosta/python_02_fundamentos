# Exemplo de metodos de strings em Python.
# Este exercicio mostra como transformar, localizar e dividir textos.

movieName = "Top Gun"
movieDescription = """
Top Gun Maverick, e um filme de aviacao e aventura
muito consagrado na industria

"""

# upper(): converte todos os caracteres para maiusculo.
print(movieName.upper())

# lower(): converte todos os caracteres para minusculo.
print(movieName.lower())

# capitalize(): deixa a primeira letra em maiusculo e o restante em minusculo.
print(movieName.capitalize())

# title(): deixa a primeira letra de cada palavra em maiusculo.
print(movieName.title())

# center(largura, caractere): centraliza o texto em uma largura definida.
print(movieName.center(10, '-'))

# find(texto): retorna a posicao da primeira ocorrencia encontrada.
print(movieName.find("u"))

# count(texto): conta quantas vezes um trecho aparece.
print(movieName.count("o"))

# replace(antigo, novo): troca um trecho por outro.
print(movieName.replace("Top", "Bottom"))

# split(separador): quebra a string em uma lista usando o separador informado.
print(movieDescription.split(","))
