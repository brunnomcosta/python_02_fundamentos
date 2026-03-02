# Exemplo de uso de *args e **kwargs em funcoes Python.
# Esses recursos permitem receber uma quantidade variavel
# de argumentos em uma funcao.
#
# Resumo:
# - *args recebe varios argumentos posicionais
# - **kwargs recebe varios argumentos nomeados
#
# Dentro da funcao:
# - *args se comporta como uma tupla
# - **kwargs se comporta como um dicionario
#
# Este arquivo mostra:
# 1. uso de *args
# 2. parametro fixo junto com *args
# 3. uso de **kwargs
# 4. parametro fixo junto com **kwargs
# 5. uso combinado de *args e **kwargs


# --------------------------------
# Exemplo 1: usando *args
# --------------------------------
# A funcao pode receber quantos numeros forem enviados.
# Todos eles chegam agrupados na tupla "numeros".

def somar_valores(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total


print("Exemplo 1:")
print(f"Soma de 7: {somar_valores(7)}")
print(f"Soma de 7 e 9: {somar_valores(7, 9)}")
print(f"Soma de 2, 3, 4 e 5: {somar_valores(2, 3, 4, 5)}")


# ---------------------------------------------
# Exemplo 2: parametro fixo junto com *args
# ---------------------------------------------
# O primeiro argumento vai para "nome".
# Os demais argumentos posicionais vao para "cursos".

def apresentar_aluno(nome, *cursos):
    print(f"Aluno: {nome}")

    if len(cursos) == 0:
        print("Nenhum curso informado.")
        return

    print("Cursos matriculados:")
    for curso in cursos:
        print(f"- {curso}")


print("\nExemplo 2:")
apresentar_aluno("Joao", "Python", "JavaScript", "SQL")


# --------------------------------
# Exemplo 3: usando **kwargs
# --------------------------------
# A funcao recebe varios argumentos nomeados.
# Todos eles chegam dentro do dicionario "dados_filme".

def exibir_dados_filme(**dados_filme):
    for chave, valor in dados_filme.items():
        print(f"{chave}: {valor}")


print("\nExemplo 3:")
exibir_dados_filme(
    titulo="Inception",
    diretor="Christopher Nolan",
    ano_lancamento=2010,
    nota=8.8,
)


# ------------------------------------------------
# Exemplo 4: parametro fixo junto com **kwargs
# ------------------------------------------------
# O argumento "categoria" e obrigatorio.
# Os demais detalhes podem variar e chegam em "informacoes".

def exibir_produto(categoria, **informacoes):
    print(f"Categoria: {categoria}")

    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")


print("\nExemplo 4:")
exibir_produto(
    "Eletronico",
    nome="Notebook",
    marca="Lenovo",
    preco=3500.00,
)


# ------------------------------------------------------
# Exemplo 5: usando *args e **kwargs na mesma funcao
# ------------------------------------------------------
# Aqui, a funcao recebe:
# - um titulo fixo
# - varios generos em *generos
# - varias informacoes extras em **detalhes

def montar_ficha_filme(titulo, *generos, **detalhes):
    print(f"Titulo: {titulo}")

    if len(generos) > 0:
        print("Generos:")
        for genero in generos:
            print(f"- {genero}")

    if len(detalhes) > 0:
        print("Detalhes extras:")
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")


print("\nExemplo 5:")
montar_ficha_filme(
    "Interstellar",
    "Sci-Fi",
    "Drama",
    diretor="Christopher Nolan",
    duracao_minutos=169,
    nota=8.6,
)
