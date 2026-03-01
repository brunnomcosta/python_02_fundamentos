"""
Módulo de Tipos de Dados em Python (Exemplo: Pythonflix)

Este módulo demonstra o uso de diferentes tipos de dados primitivos em Python:
- str (string/texto)
- int (inteiro)
- float (número decimal)
- bool (booleano - verdadeiro/falso)

Também demonstra como verificar o tipo de uma variável usando a função type().

Exemplo prático: Informações de um filme na plataforma Pythonflix.

Autor: Estudante de Python
Data: 2026
"""

# ===== Dados do Filme =====
# Definição das variáveis com diferentes tipos de dados

name = "Top Gun: Maverick"  # str - Título do filme (texto)
year_launch = 2023           # int - Ano de lançamento (número inteiro)
note_movie = 8.4             # float - Nota do filme (número decimal)
plan_included = False        # bool - Se está incluído no plano (verdadeiro/falso)

# ===== Exibição dos Dados =====
print("\n=== Informações do Filme ===")
print(f"Título: {name}")
print(f"Ano de Lançamento: {year_launch}")
print(f"Nota: {note_movie}")
print(f"Incluído no Plano: {plan_included}")

# ===== Verificação de Tipos =====
print("\n=== Tipos de Dados ===")
print(f"Tipo de '{name}': {type(name)}")
print(f"Tipo de {year_launch}: {type(year_launch)}")
print(f"Tipo de {note_movie}: {type(note_movie)}")
print(f"Tipo de {plan_included}: {type(plan_included)}")