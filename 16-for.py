# Exemplo de repeticao com for em Python.
# O laco for e usado quando queremos percorrer elementos de uma
# colecao (como lista, string ou tupla) ou repetir uma acao
# uma quantidade definida de vezes.
#
# Neste arquivo, mostramos usos comuns de for:
# 1. percorrer uma lista
# 2. mostrar posicao e valor com enumerate()
# 3. interromper o laco com break
# 4. pular uma iteracao com continue
# 5. repetir uma leitura com range()

lista_filmes = [
    "The Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]

# --------------------------------
# Exemplo 1: percorrer uma lista
# --------------------------------
# Aqui, o for visita cada item da lista, um de cada vez.

print("=== Lista de filmes ===")
for filme in lista_filmes:
    print(filme)


# -----------------------------------------
# Exemplo 2: usar enumerate() na iteracao
# -----------------------------------------
# enumerate() devolve dois valores:
# - a posicao do item
# - o valor armazenado naquela posicao

print("\n=== Lista numerada de filmes ===")
for posicao, filme in enumerate(lista_filmes, start=1):
    print(f"{posicao}. {filme}")


# ------------------------------------
# Exemplo 3: interromper com break
# ------------------------------------
# break encerra o laco assim que a condicao e atendida.
# Neste caso, a busca para quando encontrar "Inception".

print("\n=== Procurando por 'Inception' com break ===")
for filme in lista_filmes:
    print(f"Verificando: {filme}")
    if filme == "Inception":
        print(f"Encontrado: {filme}")
        break


# --------------------------------------
# Exemplo 4: pular com continue
# --------------------------------------
# continue faz o laco ignorar o restante da iteracao atual
# e seguir para o proximo item.

print("\n=== Pulando 'Inception' com continue ===")
for filme in lista_filmes:
    if filme == "Inception":
        continue
    print(f"Exibindo: {filme}")


# --------------------------------------------
# Exemplo 5: usar range() para repetir leituras
# --------------------------------------------
# range(quantidade) gera uma sequencia de numeros de 0 ate
# quantidade - 1. Aqui, usamos isso para pedir varias notas
# e calcular a media final.

nome_filme = input("\nDigite o nome do filme para avaliacao:\n")
quantidade_avaliacoes = int(input("Digite quantas avaliacoes deseja fazer:\n"))

total_notas = 0

for numero_avaliacao in range(quantidade_avaliacoes):
    nota = float(input(f"Digite a nota {numero_avaliacao + 1}:\n"))
    total_notas += nota

if quantidade_avaliacoes > 0:
    media = total_notas / quantidade_avaliacoes
    print(f"A media do filme '{nome_filme}' e: {media:.2f}")
else:
    print(f"Nenhuma avaliacao foi informada para o filme '{nome_filme}'.")
