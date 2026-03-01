# Exemplo basico de manipulacao de strings em Python.
# Este exercicio mostra:
# 1. comparacao entre strings
# 2. uso de texto em varias linhas
# 3. repeticao de caracteres com o operador *
# 4. busca de trechos com o operador in
# Python e case sensitive: letras maiusculas e minusculas sao tratadas como diferentes.

# As duas strings sao parecidas, mas a primeira letra muda de "T" para "t".
movieName = "Top Gun: Maverick"
movieName2 = "top Gun: Maverick"

# Compara as duas strings.
print(movieName == movieName2) # False, pois as letras maiusculas e minusculas sao diferentes

# Strings entre tres aspas permitem escrever um texto em varias linhas.
movieDescription = """
Top Gun: Maverick é um filme de ação e aventura lançado em 2023, dirigido por Joseph Kosinski. O filme é uma sequência do clássico Top Gun de 1986 e segue a história do piloto de caça Pete 
\"Maverick\" Mitchell, interpretado por Tom Cruise, enquanto ele treina uma nova geração de pilotos da Marinha dos Estados Unidos. 
O filme é conhecido por suas cenas de ação emocionantes, efeitos visuais impressionantes e pela performance carismática de Tom Cruise. 
Top Gun: Maverick recebeu críticas positivas e foi um sucesso de bilheteria, consolidando-se como um dos filmes mais populares do ano.
"""

# Exibe apenas o titulo do filme.
print(movieName)

# Multiplicacao de strings:
# o caractere "=" e repetido 50 vezes para criar uma linha visual.
line = "="
print(line * 50)

# Exibe a descricao completa.
print(movieDescription)

# Busca de texto com o operador "in".
# Essa verificacao tambem respeita maiusculas e minusculas.
print("top" in movieName) # False, pois "top" esta em minusculo e o titulo comeca com "Top"
print("Top" in movieName) # True, pois "Top" esta presente no titulo
print("Maverick" in movieName) # True, pois "Maverick" esta presente no titulo
print("Cruise" in movieName) # False, pois "Cruise" nao aparece no titulo
