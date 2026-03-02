# Exemplo de funcoes lambda em Python.
# Lambda e uma forma curta de criar funcoes pequenas e de uso rapido.
# Ela costuma ser usada quando a funcao tem apenas uma expressao
# e quando nao vale a pena criar uma funcao completa com def.
#
# Estrutura:
# lambda parametros: expressao
#
# Importante:
# - lambda retorna o resultado da expressao automaticamente
# - lambda e melhor para casos simples
# - para regras maiores, prefira usar def


# --------------------------------
# Exemplo 1: operacao simples
# --------------------------------
# Aqui, a lambda recebe um numero e devolve o dobro dele.

dobro = lambda numero: numero * 2

print("Exemplo 1: operacao simples")
print(dobro(5))
print(dobro(12))


# --------------------------------
# Exemplo 2: mais de um parametro
# --------------------------------
# Lambda tambem pode receber varios parametros.
# Neste caso, calculamos a media de duas notas.

media_duas_notas = lambda nota_1, nota_2: (nota_1 + nota_2) / 2

print("\nExemplo 2: mais de um parametro")
print(media_duas_notas(8.5, 9.5))


# -----------------------------------------
# Exemplo 3: lambda com condicao simples
# -----------------------------------------
# Uma expressao condicional tambem pode ser usada dentro da lambda.

situacao_nota = lambda nota: "Aprovado" if nota >= 7 else "Revisar"

print("\nExemplo 3: condicao simples")
print(situacao_nota(8.0))
print(situacao_nota(5.5))


# ------------------------------------------------
# Exemplo 4: lambda usada como chave de ordenacao
# ------------------------------------------------
# Este e um dos usos mais comuns de lambda:
# passar uma regra pequena para o parametro "key".
# Aqui, ordenamos os filmes pela nota.

filmes = [
    {"titulo": "Top Gun: Maverick", "nota": 8.5},
    {"titulo": "The Batman", "nota": 7.5},
    {"titulo": "Avatar: The Way of Water", "nota": 8.7},
    {"titulo": "Black Panther: Wakanda Forever", "nota": 7.4},
]

filmes_ordenados_por_nota = sorted(
    filmes,
    key=lambda filme: filme["nota"],
    reverse=True,
)

print("\nExemplo 4: filmes ordenados por nota")
for filme in filmes_ordenados_por_nota:
    print(f"{filme['titulo']} - {filme['nota']}")


# --------------------------------------------------
# Exemplo 5: lambda para montar recomendacao rapida
# --------------------------------------------------
# Aqui, usamos uma lambda para gerar uma mensagem curta
# a partir dos dados de um filme.

criar_recomendacao = (
    lambda titulo, nota: (
        f"{titulo}: recomendado" if nota >= 8 else f"{titulo}: vale avaliar melhor"
    )
)

print("\nExemplo 5: recomendacao")
print(criar_recomendacao("Top Gun: Maverick", 8.5))
print(criar_recomendacao("The Batman", 7.5))
