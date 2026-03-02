# Exemplo de repeticao com while em Python.
# O laco while continua executando enquanto uma condicao
# for verdadeira. Ele e util quando a repeticao depende
# de uma regra, e nao apenas de uma quantidade fixa.
#
# Neste arquivo, mostramos usos comuns de while:
# 1. percorrer uma lista com indice
# 2. fazer uma contagem regressiva
# 3. interromper o laco com break
# 4. pular uma iteracao com continue
# 5. repetir leituras com contador

lista_filmes = [
    "The Matrix",
    "Inception",
    "Interstellar",
    "The Dark Knight",
    "Pulp Fiction",
]

# ------------------------------------------
# Exemplo 1: percorrer lista usando indice
# ------------------------------------------
# Diferente do for, no while precisamos controlar
# manualmente o indice e atualiza-lo a cada volta.

print("=== Lista de filmes com while ===")
indice = 0

while indice < len(lista_filmes):
    print(f"{indice + 1}. {lista_filmes[indice]}")
    indice += 1


# -----------------------------------
# Exemplo 2: contagem regressiva
# -----------------------------------
# Este exemplo mostra um uso classico de while:
# repetir ate que um contador chegue a zero.

print("\n=== Contagem regressiva ===")
contador = 3

while contador > 0:
    print(contador)
    contador -= 1

print("Fim da contagem!")


# ------------------------------------
# Exemplo 3: interromper com break
# ------------------------------------
# break encerra imediatamente o while quando a condicao
# interna for atendida.

print("\n=== Procurando por 'Inception' com break ===")
indice = 0

while indice < len(lista_filmes):
    filme_atual = lista_filmes[indice]
    print(f"Verificando: {filme_atual}")

    if filme_atual == "Inception":
        print(f"Encontrado: {filme_atual}")
        break

    indice += 1


# --------------------------------------
# Exemplo 4: pular com continue
# --------------------------------------
# continue faz o while ignorar o restante da iteracao atual.
# No while, e importante atualizar o indice antes do continue
# para evitar um laco infinito.

print("\n=== Pulando 'Inception' com continue ===")
indice = 0

while indice < len(lista_filmes):
    filme_atual = lista_filmes[indice]

    if filme_atual == "Inception":
        indice += 1
        continue

    print(f"Exibindo: {filme_atual}")
    indice += 1


# -----------------------------------------
# Exemplo 5: repetir leituras com contador
# -----------------------------------------
# Aqui, o while repete a leitura de notas ate atingir a
# quantidade informada pelo usuario.

nome_filme = input("\nDigite o nome do filme para avaliacao:\n")
quantidade_avaliacoes = int(input("Digite quantas avaliacoes deseja fazer:\n"))

total_notas = 0
avaliacao_atual = 0

while avaliacao_atual < quantidade_avaliacoes:
    nota = float(input(f"Digite a nota {avaliacao_atual + 1}:\n"))
    total_notas += nota
    avaliacao_atual += 1

if quantidade_avaliacoes > 0:
    media = total_notas / quantidade_avaliacoes
    print(f"A media do filme '{nome_filme}' e: {media:.2f}")
else:
    print(f"Nenhuma avaliacao foi informada para o filme '{nome_filme}'.")
