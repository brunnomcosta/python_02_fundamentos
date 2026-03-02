# Python - Fundamentos

Repositorio com exemplos e exercicios introdutorios de Python.

Cada arquivo foi pensado para estudar um conceito de cada vez, com scripts pequenos e faceis de executar. A ideia e praticar a base da linguagem antes de avancar para temas mais complexos.

## Como estudar este repositorio

Uma ordem simples e eficiente:

1. Comece pelos arquivos numerados (`01` a `23`), porque eles apresentam os conceitos.
2. Em seguida, rode os arquivos `ex*.py`, que reforcam a pratica com pequenos desafios.
3. Antes de executar, tente prever a saida do programa.
4. Depois, altere os valores e teste novamente para observar o comportamento do Python.

## Mapa dos arquivos

Arquivos de conceito:

- `01-primeiro.py`: primeiros comandos e saida no terminal
- `02-dados.py`: tipos de dados basicos
- `02-dados-exercicio.py`: pratica com tipos de dados
- `03-input.py`: leitura de dados com `input()`
- `04-concatena.py`: concatenacao de textos
- `05-operadores.py`: operadores aritmeticos
- `06-strings.py`: comparacao e busca em strings
- `07-slice.py`: fatiamento de strings com `slice`
- `08-metodos_strings.py`: metodos comuns de string
- `09-lista.py`: introducao a listas
- `10-metodo_lista.py`: metodos de listas
- `11-tupla.py`: introducao a tuplas
- `12-set.py`: introducao a sets
- `13-dicionario.py`: introducao a dicionarios
- `14-dicionario_aninhado.py`: dicionarios dentro de dicionarios
- `15-condicao.py`: estruturas condicionais com `if`, `elif` e `else`
- `16-for.py`: repeticao com `for`, `break`, `continue` e `range()`
- `17-while.py`: repeticao com `while` e controle manual de condicao
- `18-list_comprehension.py`: criacao e filtro de listas com list comprehension
- `19-funcao.py`: introducao a funcoes e retorno de valores
- `20-args_func.py`: parametros, argumentos e `*args`
- `21-funcao_recursiva.py`: recursao com caso base e chamada da propria funcao
- `22-funcoes_args_kwargs.py`: uso de `*args` e `**kwargs`
- `23-lambda_func.py`: funcoes `lambda` e usos simples com expressoes curtas

Arquivos de exercicio:

- `ex1.py`: exercicios simples com strings e formatacao
- `ex2.py`: exercicio introdutorio de pratica
- `ex6.py`: exercicio com listas
- `ex7.py`: exercicio com tupla
- `ex8.py`: exercicio com set
- `ex9.py`: exercicio com dicionario

Outros arquivos:

- `teste.ipynb`: anotacoes e testes em notebook

## Como executar

No terminal, dentro da pasta do projeto, execute:

```powershell
python nome-do-arquivo.py
```

Exemplos:

```powershell
python 11-tupla.py
python 12-set.py
python 13-dicionario.py
python 14-dicionario_aninhado.py
python 15-condicao.py
python 16-for.py
python 17-while.py
python 18-list_comprehension.py
python 19-funcao.py
python 20-args_func.py
python 21-funcao_recursiva.py
python 22-funcoes_args_kwargs.py
python 23-lambda_func.py
python ex8.py
python ex9.py
```

Se o arquivo usar `input()`, digite os valores solicitados e pressione Enter apos cada entrada.

## Observacoes importantes

- `list` preserva a ordem dos elementos e aceita repeticao.
- `tuple` preserva a ordem dos elementos, aceita repeticao e nao pode ser alterada.
- `set` nao garante ordem de exibicao e remove valores repetidos automaticamente.
- `dict` armazena dados no formato `chave: valor` e facilita organizar informacoes nomeadas.
- `if`, `elif` e `else` permitem tomar decisoes diferentes com base em condicoes.
- `for` e `while` sao usados para repetir tarefas.
- funcoes ajudam a organizar o codigo e evitar repeticao.
- `lambda` e util para funcoes curtas e simples.
- Por causa disso, a ordem mostrada ao imprimir um `set` pode variar.

## Requisitos

- Python 3 instalado
- Terminal ou editor com suporte a execucao de scripts Python

## Objetivo de aprendizado

Este repositorio serve para:

- entender a sintaxe basica do Python
- praticar entrada e saida de dados
- estudar strings, listas, tuplas, sets, dicionarios, operadores, condicionais, lacos e funcoes
- reforcar conceitos com exercicios curtos e diretos
