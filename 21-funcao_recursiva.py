# Exemplo de funcao recursiva em Python.
# Uma funcao recursiva e uma funcao que chama a si mesma.
# Esse tipo de solucao e util quando um problema pode ser
# dividido em partes menores e semelhantes.
#
# Toda recursao precisa de:
# 1. caso base: condicao que encerra as chamadas
# 2. passo recursivo: parte em que a funcao chama a si mesma
#
# Sem caso base, a funcao entraria em repeticao infinita.


# --------------------------------
# Exemplo 1: fatorial
# --------------------------------
# Fatorial de 5:
# 5! = 5 * 4 * 3 * 2 * 1
#
# Regras importantes:
# - 0! = 1
# - 1! = 1

def calcular_fatorial(numero):
    if numero < 0:
        raise ValueError("O fatorial nao existe para numeros negativos.")

    # Caso base: encerra a recursao.
    if numero == 0 or numero == 1:
        return 1

    # Passo recursivo: reduz o problema ate chegar ao caso base.
    return numero * calcular_fatorial(numero - 1)


print("Exemplo 1: fatorial")
print(f"Fatorial de 5: {calcular_fatorial(5)}")


# --------------------------------
# Exemplo 2: soma acumulada
# --------------------------------
# Esta funcao soma todos os numeros de 1 ate o valor informado.
# Exemplo:
# soma_ate(4) = 4 + 3 + 2 + 1 = 10

def somar_ate(numero):
    if numero < 1:
        return 0

    # Caso base: quando chegar a 1, a soma termina.
    if numero == 1:
        return 1

    return numero + somar_ate(numero - 1)


print("\nExemplo 2: soma acumulada")
print(f"Soma de 1 ate 5: {somar_ate(5)}")


# --------------------------------
# Exemplo 3: contagem regressiva
# --------------------------------
# Nem toda recursao precisa retornar um numero.
# Aqui, a funcao apenas imprime os valores ate chegar a zero.

def contagem_regressiva(numero):
    if numero < 0:
        print("Fim da contagem!")
        return

    print(numero)
    contagem_regressiva(numero - 1)


print("\nExemplo 3: contagem regressiva")
contagem_regressiva(3)
