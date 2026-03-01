# Exemplo de fatiamento (slice) de strings em Python.
# A ideia do slice e selecionar apenas uma parte do texto.
#
# Sintaxe basica:
# string[inicio:fim]
#
# Regras importantes:
# 1. O indice inicial comeca em 0.
# 2. O indice "fim" nao e incluido no resultado.
# 3. Se "inicio" for omitido, Python comeca do inicio da string.
# 4. Se "fim" for omitido, Python vai ate o final da string.

movieName = "Top Gun"

# 1. Do primeiro caractere ate o final.
print(movieName[0:])  # Top Gun

# 2. Do segundo caractere ate o final.
print(movieName[1:])  # op Gun

# 3. Do inicio da string ate o indice 7 (sem incluir o 7).
print(movieName[:7])  # Top Gun

# 4. Do inicio da string ate o indice 6 (sem incluir o 6).
print(movieName[:6])  # Top Gu

# 5. Do indice 2 ate o final.
print(movieName[2:])  # p Gun

#
# Sintaxe com passo:
# string[inicio:fim:passo]
#
# O "passo" define de quantos em quantos caracteres o Python vai andar.
# Se ele nao for informado, o valor padrao e 1.

# 6. Do indice 2 ate o final, pulando de 2 em 2.
print(movieName[2::2])  # pGn

# 7. Do inicio ate o final, pegando um caractere sim e outro nao.
print(movieName[::2])  # TpGn

# 8. A partir do indice 1, pegando de 2 em 2.
print(movieName[1::2])  # o u

# 9. Com passo -1, a string e percorrida de tras para frente.
print(movieName[::-1])  # nuG poT
