# Ex1: ler nome e sobrenome e montar uma saudacao com f-string.
primeiroNome = input("Digite seu primeiro nome: ")
segundoNome = input("Digite seu sobrenome: ")

# Junta nome e sobrenome em uma unica string.
nomeFormatado = f"{primeiroNome} {segundoNome}"

# Exibe a mensagem final usando o nome completo.
print(f"Olá, {nomeFormatado}! Bem-vindo ao curso de Python!")

# Ex2: inverter a ordem das palavras de uma frase.
texto = "Pytho é muito interessante"

# split() separa a frase em uma lista de palavras.
palavras = texto.split()

# [::-1] inverte a lista e join() monta o texto novamente.
textoInvertido = " ".join(palavras[::-1])
#textoInvertido = " ".join(reversed(palavras))

# Mostra a frase original e a frase com a ordem das palavras invertida.
print(f"Texto original: {texto}")
print(f"Texto invertido: {textoInvertido}")

# Ex3: verificar se uma palavra e um palindromo.
texto1 = "arara"
texto2 = "python"

# Padroniza os textos para comparar melhor:
# lower() deixa tudo em minusculo e replace() remove espacos.
texto1_formatado = texto1.lower().replace(" ", "")
texto2_formatado = texto2.lower().replace(" ", "")

# Compara o texto com sua versao invertida.
pallindromo1 = texto1_formatado == texto1_formatado[::-1]
pallindromo2 = texto2_formatado == texto2_formatado[::-1]

# Exibe o resultado da verificacao.
print(f"'{texto1}' é um palíndromo? {pallindromo1}")
print(f"'{texto2}' é um palíndromo? {pallindromo2}")
