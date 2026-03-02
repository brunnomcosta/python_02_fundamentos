# Exemplo de funcoes em Python.
# Funcao e um bloco de codigo criado para executar uma tarefa
# especifica. Ela ajuda a organizar o programa, evitar repeticao
# e deixar o codigo mais facil de entender.
#
# Neste arquivo, mostramos usos comuns de funcoes:
# 1. funcao sem parametro e sem retorno
# 2. funcao com parametro
# 3. funcao com retorno
# 4. funcao que devolve True ou False
# 5. funcao que le dados e devolve um dicionario


# -----------------------------------------------
# Exemplo 1: funcao sem parametro e sem retorno
# -----------------------------------------------
# Esta funcao apenas executa uma acao: mostrar uma mensagem.

def exibir_boas_vindas():
    print("Bem-vindo ao estudo de funcoes em Python!")
    print("Funcoes ajudam a organizar melhor o codigo.")


exibir_boas_vindas()


# --------------------------------
# Exemplo 2: funcao com parametro
# --------------------------------
# O parametro permite que a funcao receba um valor externo.
# Assim, a mesma funcao pode ser reutilizada com dados diferentes.

def mostrar_filme(titulo, ano_lancamento):
    print(f"O filme {titulo} foi lancado em {ano_lancamento}.")


print("\nExemplo com parametros:")
mostrar_filme("Inception", 2010)
mostrar_filme("Interstellar", 2014)


# -----------------------------
# Exemplo 3: funcao com retorno
# -----------------------------
# Em vez de apenas imprimir, esta funcao calcula e devolve um valor.
# Quem chama a funcao decide o que fazer com o resultado.

def calcular_media(notas):
    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


notas_filme = [8.5, 9.0, 10.0]
media_filme = calcular_media(notas_filme)

print("\nExemplo com retorno:")
print(f"A media das notas e: {media_filme:.2f}")


# ---------------------------------------
# Exemplo 4: funcao que retorna True/False
# ---------------------------------------
# Funcoes tambem podem devolver um valor logico.
# Isso e util para verificacoes e decisoes no programa.

def filme_recomendado(nota, ano_lancamento):
    return nota >= 8.0 and ano_lancamento >= 2010


print("\nExemplo com retorno booleano:")

if filme_recomendado(8.8, 2010):
    print("Inception entra na lista de recomendacoes.")
else:
    print("Inception nao entra na lista de recomendacoes.")


# -------------------------------------------------
# Exemplo 5: funcao que le dados e devolve um registro
# -------------------------------------------------
# Esta funcao junta varias entradas do usuario e devolve um dicionario.
# Assim, os dados ficam organizados e podem ser usados depois.

def cadastrar_filme():
    titulo = input("\nDigite o titulo do filme:\n").strip()
    diretor = input("Digite o diretor do filme:\n").strip()
    ano_lancamento = int(input("Digite o ano de lancamento:\n"))
    duracao_minutos = int(input("Digite a duracao em minutos:\n"))

    return {
        "titulo": titulo,
        "diretor": diretor,
        "ano_lancamento": ano_lancamento,
        "duracao_minutos": duracao_minutos,
    }


filme_cadastrado = cadastrar_filme()

print("\nFilme cadastrado:")
print(filme_cadastrado)
