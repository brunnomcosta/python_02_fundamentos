num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))

# Exemplo de operadores aritmeticos e relacionais em Python.
# Fluxo do exercicio:
# 1. Ler dois numeros com input()
# 2. Calcular operacoes matematicas basicas
# 3. Comparar os dois valores com operadores relacionais
# input() retorna string, por isso os valores acima foram convertidos com int().
# Os dois numeros lidos no inicio sao reutilizados em todos os exemplos abaixo.

# Operadores aritmeticos:
# + soma
# - subtracao
# * multiplicacao
# / divisao
# % modulo (resto da divisao)
# ** exponenciacao (potencia)
# Cada variavel abaixo guarda o resultado de uma dessas operacoes.
sum            = num1 + num2
subtraction    = num1 - num2
multiplication = num1 * num2
division       = num1 / num2
mod            = num1 % num2
exponentiation = num1 ** num2

# Exibe cada resultado usando f-strings.
print(f"A soma de {num1} e {num2} é: {sum}")
print(f"A subtração de {num1} e {num2} é: {subtraction}")
print(f"A multiplicação de {num1} e {num2} é: {multiplication}")
print(f"A divisão de {num1} e {num2} é: {division}")   
print(f"O módulo de {num1} e {num2} é (Resto da divisão): {mod}")
print(f"A exponenciação de {num1} e {num2} é: {exponentiation}")

#Comparação de números
# Operadores relacionais:
# > maior que
# < menor que
# == igual a
# != diferente de
# >= maior ou igual a
# <= menor ou igual a
# Cada variavel abaixo guarda o resultado de uma comparacao.
bigger            = num1 > num2
smaller           = num1 < num2
equal             = num1 == num2
different         = num1 != num2
bigger_or_equal   = num1 >= num2
smaaller_or_equal = num1 <= num2
# Primeiro, as comparacoes sao exibidas usando as variaveis acima.

print(f"{num1} é maior que {num2}? {bigger}")
print(f"{num1} é menor que {num2}? {smaller}")
print(f"{num1} é igual a {num2}? {equal}")
print(f"{num1} é diferente de {num2}? {different}")
print(f"{num1} é maior ou igual a {num2}? {bigger_or_equal}")                                         
print(f"{num1} é menor ou igual a {num2}? {smaaller_or_equal}")


print(f"{num1} é igual a {num2}? {num1 == num2}")
print(f"{num1} é diferente de {num2}? {num1 != num2}")
print(f"{num1} é maior que {num2}? {num1 > num2}")
print(f"{num1} é menor que {num2}? {num1 < num2}")
print(f"{num1} é maior ou igual a {num2}? {num1 >= num2}")
print(f"{num1} é menor ou igual a {num2}? {num1 <= num2}")     
