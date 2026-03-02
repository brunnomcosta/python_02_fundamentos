# Exercicio 9 - Dicionario
# O programa:
# 1. le o nome e o preco de 3 produtos
# 2. guarda os dados em um dicionario
# 3. mostra o dicionario completo
# 4. mostra o nome do produto mais caro
# 5. mostra a media dos precos com 2 casas decimais
#
# Estrutura usada:
# - chave: nome do produto
# - valor: preco do produto (float)
#
# Exemplo de dicionario montado:
# {"Arroz": 15.5, "Feijao": 8.9, "Macarrao": 6.75}

# Cria um dicionario vazio para armazenar os produtos.
produtos = {}

# Repete 3 vezes para ler os dados pedidos no exercicio.
for _ in range(3):
    nome_produto = input().strip()
    preco_produto = float(input())

    # Guarda o produto no dicionario.
    # O nome vira a chave e o preco vira o valor.
    produtos[nome_produto] = preco_produto

# Exibe o dicionario completo.
print(produtos)

# Encontra a chave com o maior valor.
# key=produtos.get faz a comparacao usando os precos.
produto_mais_caro = max(produtos, key=produtos.get)
print(produto_mais_caro)

# Soma todos os precos e divide pela quantidade de produtos.
media_precos = sum(produtos.values()) / len(produtos)

# Exibe a media com 2 casas decimais, como no exemplo do exercicio.
print(f"{media_precos:.2f}")
