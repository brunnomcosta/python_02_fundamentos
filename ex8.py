# Exercicio 8 - Set
# O programa:
# 1. le 5 numeros inteiros (aceitando repeticoes)
# 2. armazena os valores em um set para remover duplicatas
# 3. mostra o set final
# 4. mostra quantos valores unicos existem
# 5. mostra o maior valor do set
#
# Observacao importante:
# O set remove valores repetidos automaticamente e nao garante
# uma ordem fixa de exibicao ao ser impresso.

# Cria um set vazio para guardar apenas valores unicos.
numeros_unicos = set()

# Repete 5 vezes para ler os 5 numeros pedidos no exercicio.
for _ in range(5):
    numero_digitado = int(input())

    # Ao adicionar em um set, valores repetidos sao ignorados automaticamente.
    numeros_unicos.add(numero_digitado)

# Exibe o set com os valores sem repeticao.
# A ordem visual pode variar, porque set e uma colecao nao ordenada.
print(numeros_unicos)

# Exibe a quantidade de elementos unicos armazenados.
print(len(numeros_unicos))

# Exibe o maior numero presente no set.
print(max(numeros_unicos))
