# Exemplo de metodos de lista em Python.
# Este arquivo mostra como consultar, alterar, ordenar, copiar e remover itens.

filmsList = ["Inception", "Interstellar", "Dunkirk", "Tenet"]

# 1. len() retorna a quantidade de itens da lista.
print(f"Tamanho da lista: {len(filmsList)}")

# 2. index(valor) retorna a posicao do item informado.
# Aqui, ele mostra em qual indice "Dunkirk" esta.
print(f'Indice de "Dunkirk": {filmsList.index("Dunkirk")}')

# 3. append(valor) adiciona um novo item no final da lista.
filmsList.append("Memento")
print(f"Lista apos append: {filmsList}")

# 4. sort() ordena a propria lista em ordem alfabetica.
# Esse metodo altera a lista original.
filmsList.sort()
print(f"Lista ordenada: {filmsList}")

# 5. copy() cria uma copia da lista atual.
filmsCopy = filmsList.copy()
print(f"Copia da lista: {filmsCopy}")

# 6. remove(valor) exclui o item informado da copia.
# A lista original continua igual, porque a remocao acontece em filmsCopy.
filmsCopy.remove("Tenet")
print(f"Copia apos remove: {filmsCopy}")
print(f"Lista original sem alteracao: {filmsList}")
