# Exemplo de estruturas condicionais em Python.
# Este arquivo mostra dois usos comuns de condicoes:
# 1. tomar uma decisao com base em mais de uma regra
# 2. escolher uma acao entre varias opcoes com if, elif e else

# ---------------------------------
# Exemplo 1: recomendacao de filme
# ---------------------------------
# O programa le informacoes basicas sobre um filme e decide se ele
# sera recomendado. Para isso, usamos o operador logico "and":
# as duas condicoes precisam ser verdadeiras ao mesmo tempo.

nome_filme     = input("Digite o nome do filme:\n")
ano_lancamento = int(input("Digite o ano de lancamento:\n"))
nota_filme     = float(input("Digite a nota de avaliacao do filme:\n"))

# O filme sera considerado "muito bom" se:
# - tiver nota maior que 8.0
# - e tiver sido lancado depois de 2015
if nota_filme > 8.0 and ano_lancamento > 2015:
    print(f"O filme {nome_filme} e muito bom. Recomendo assisti-lo.")
else:
    print(f"O filme {nome_filme} ainda nao atingiu uma boa nota.")


# --------------------------------
# Exemplo 2: calculadora simples
# --------------------------------
# O programa le dois numeros e uma operacao matematica.
# Depois, usa if/elif para descobrir qual calculo deve ser feito.

numero_1 = float(input("Digite um numero:\n"))
numero_2 = float(input("Digite outro numero:\n"))
operacao = input("Digite a operacao desejada (+, -, *, /):\n")

if operacao == "+":
    resultado = numero_1 + numero_2
    print(f"O resultado da soma e: {resultado}")
elif operacao == "-":
    resultado = numero_1 - numero_2
    print(f"O resultado da subtracao e: {resultado}")
elif operacao == "*":
    resultado = numero_1 * numero_2
    print(f"O resultado da multiplicacao e: {resultado}")
elif operacao == "/":
    # Antes de dividir, verificamos se o segundo numero e diferente de zero.
    # Isso evita erro de divisao por zero.
    if numero_2 != 0:
        resultado = numero_1 / numero_2
        print(f"O resultado da divisao e: {resultado}")
    else:
        print("Erro: divisao por zero nao e permitida.")
else:
    # Este bloco e executado quando a operacao digitada nao e valida.
    print("Operacao invalida. Use apenas +, -, * ou /.")
