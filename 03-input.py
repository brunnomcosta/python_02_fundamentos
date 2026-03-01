#Utilizando o Input
# O prefixo f em print(f"...") cria uma f-string e troca {variavel} pelo valor dela.

from xmlrpc.client import boolean


name = input("Digite seu nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))
planIncluded = boolean(input("O filme está incluído no plano? (True/False):\n"))

print(f"O nome do filme é: {name}")
print(f"O ano de lançamento do filme é: {yearLaunch}")
print(f"A nota do filme é: {noteMovie}")
print(f"O filme está incluído no plano: {planIncluded}")

print(type(name))
print(type(yearLaunch))
print(type(noteMovie))
print(type(planIncluded))