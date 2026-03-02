# Exemplo de parametros e argumentos em funcoes Python.
# Parametros sao os nomes definidos na criacao da funcao.
# Argumentos sao os valores enviados quando a funcao e chamada.
#
# Este arquivo mostra formas comuns de trabalhar com argumentos:
# 1. parametro simples
# 2. varios parametros posicionais
# 3. parametro com valor padrao
# 4. argumentos nomeados
# 5. retorno com base nos parametros recebidos
# 6. quantidade variavel de argumentos com *args


# --------------------------------
# Exemplo 1: parametro simples
# --------------------------------
# A funcao recebe um unico valor e o usa na mensagem.

def exibir_titulo_filme(titulo):
    print(f"Filme informado: {titulo}")


print("Exemplo 1:")
exibir_titulo_filme("Inception")


# ------------------------------------------
# Exemplo 2: varios parametros posicionais
# ------------------------------------------
# Aqui, a ordem dos argumentos importa.
# O primeiro valor vai para "titulo", o segundo para "ano_lancamento"
# e o terceiro para "nota".

def exibir_detalhes_filme(titulo, ano_lancamento, nota):
    print(f"Titulo: {titulo}")
    print(f"Ano de lancamento: {ano_lancamento}")
    print(f"Nota: {nota}")


print("\nExemplo 2:")
exibir_detalhes_filme("Interstellar", 2014, 8.6)


# -----------------------------------------
# Exemplo 3: parametro com valor padrao
# -----------------------------------------
# Se nenhum argumento for enviado para "diretor",
# a funcao usa o valor definido no parametro.

def descrever_filme(titulo, diretor="Diretor nao informado"):
    print(f"O filme {titulo} foi dirigido por {diretor}.")


print("\nExemplo 3:")
descrever_filme("Pulp Fiction", "Quentin Tarantino")
descrever_filme("Avatar")


# -----------------------------------------
# Exemplo 4: argumentos nomeados
# -----------------------------------------
# Nesta forma, informamos cada valor pelo nome do parametro.
# Isso torna a chamada mais clara e evita erro por ordem incorreta.

def exibir_catalogo(titulo, genero, duracao_minutos):
    print(f"{titulo} | {genero} | {duracao_minutos} minutos")


print("\nExemplo 4:")
exibir_catalogo(
    titulo="The Dark Knight",
    genero="Action",
    duracao_minutos=152,
)


# -----------------------------------------
# Exemplo 5: parametros com retorno
# -----------------------------------------
# A funcao recebe duas notas e devolve a media.
# O valor retornado pode ser guardado em uma variavel.

def calcular_media_duas_notas(nota_1, nota_2):
    return (nota_1 + nota_2) / 2


media = calcular_media_duas_notas(8.5, 9.5)

print("\nExemplo 5:")
print(f"A media calculada foi: {media:.2f}")


# -----------------------------------------
# Exemplo 6: quantidade variavel com *args
# -----------------------------------------
# *args permite receber varios argumentos sem definir
# antes quantos valores serao enviados.
# Dentro da funcao, "notas" se comporta como uma tupla.

def calcular_media_varias_notas(*notas):
    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


media_varias_notas = calcular_media_varias_notas(7.5, 8.0, 9.5, 10.0)

print("\nExemplo 6:")
print(f"A media de varias notas foi: {media_varias_notas:.2f}")
