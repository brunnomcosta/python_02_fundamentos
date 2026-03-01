filmMatriz = ["Matriz", 1999, 8.7, True]

print(filmMatriz)
print("\n=== Informações do Filme ===")
print(f"Título: {filmMatriz[0]}")
print(f"Ano de Lançamento: {filmMatriz[1]}")
print(f"Nota: {filmMatriz[2]}")
print(f"Incluído no Plano: {filmMatriz[3]}")


filmsList = ["Inception", "Interstellar", "Dunkirk", "Tenet"]

#1 - Buscar os dois primeiros da lista
print(filmsList[0:2])

#2 - Buscar os dois últimos da lista
print(filmsList[-2:])

#3 - Buscar o último item da lista
print(filmsList[-1])

# 4 - Buscar filmes até a terceira posição
print(filmsList[:3])

#5 - Buscar filmes a partir da terceira posição
print(filmsList[2:])