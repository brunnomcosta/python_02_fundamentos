# Exemplo de entrada de dados e exibicao de informacoes no terminal.
# Objetivo:
# 1. Ler dados digitados pelo usuario
# 2. Converter alguns valores para outros tipos
# 3. Exibir os mesmos dados com tecnicas diferentes de formatacao
# O prefixo f em f"..." cria uma f-string e insere o valor do que estiver entre {}.

# Importa um tipo booleano usado na tentativa de tratar a resposta do plano.
from xmlrpc.client import boolean


# input() sempre retorna string; por isso alguns valores sao convertidos.
# int(...) transforma texto numerico em numero inteiro.
# float(...) transforma texto numerico em numero decimal.
# boolean(...) representa uma tentativa de converter a resposta para um valor logico.
name = input("Digite seu nome do filme:\n")
yearLaunch = int(input("Digite o ano de lançamento do filme:\n"))
noteMovie = float(input("Digite a nota do filme:\n"))
planIncluded = boolean(input("O filme está incluído no plano? (True/False):\n"))

print(f"O nome do filme é: {name}")
print(f"O ano de lançamento do filme é: {yearLaunch}")
print(f"A nota do filme é: {noteMovie}")
print(f"O filme está incluído no plano: {planIncluded}")

# O bloco acima mostra cada dado em uma linha separada.
# Mostra o tipo final de cada variavel depois das conversoes.
print(type(name))
print(type(yearLaunch))
print(type(noteMovie))
print(type(planIncluded))


# Abaixo, os mesmos dados sao exibidos com diferentes estilos de formatacao.

# Alternativa 1: usando virgulas no print()
print("Dados do Filme")
print("======================")
print("Nome do filme:", name)
print("Ano de lançamento:", yearLaunch)
print("Nota do filme:", noteMovie)

# Alternativa 2: usando f-strings em cada linha
print("\nDados do Filme")
print("======================")
print(f"Nome do filme: {name}")
print(f"Ano de lançamento: {yearLaunch}")
print(f"Nota do filme: {noteMovie}")

# Alternativa 3: usando \n dentro de uma unica string
print("\nDados do Filme")  
print("======================")
print(f"Nome do filme: {name}\nAno de lançamento: {yearLaunch}\nNota do filme: {noteMovie}")

# Alternativa 4: usando string de multiplas linhas
print("\nDados do Filme")
print("======================")
print(f"""Nome do filme: {name}
Ano de lançamento: {yearLaunch}
Nota do filme: {noteMovie}""")

# Alternativa 5: usando sep para quebrar linhas
print("\nDados do Filme")
print("======================")
print(f"Nome do filme: {name}", f"Ano de lançamento: {yearLaunch}", f"Nota do filme: {noteMovie}", sep="\n")

# Alternativa 6: misturando texto fixo, variaveis e \n no mesmo print()
print("\nDados do Filme")
print("======================")
print("Nome do filme: ", name,"\nAno de lançamento: ",  yearLaunch,"\nNota do filme: ", noteMovie)



# Alternativa 7: usando o metodo .format()
print("\nDados do Filme")
print("======================")
print("Nome do filme: {}\nAno de lançamento: {}\nNota do filme: {}".format(name, yearLaunch, noteMovie))

# Alternativa 8: usando a formatacao antiga com %
print("\nDados do Filme")
print("======================")
print("Nome do filme: %s\nAno de lançamento: %d\nNota do filme: %.1f" % (name, yearLaunch, noteMovie))

# Alternativa 9: usando concatenacao com +
print("\nDados do Filme")
print("======================")
print("Nome do filme: " + name + "\nAno de lançamento: " + str(yearLaunch) + "\nNota do filme: " + str(noteMovie))


# Alternativa 10: quebrando a string em varias linhas no codigo
print("\nDados do Filme")
print("======================")
print(f"Nome do filme: {name}\n"
f"Ano de lançamento: {yearLaunch}\n"
f"Nota do filme: {noteMovie}")
