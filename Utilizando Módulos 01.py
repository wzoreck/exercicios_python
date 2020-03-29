# Módulos seria melhorias que fariamos no python, ex: carro popular que vc vai
# adicionando acessórios

# O python e outras linguagens trabalham apartir de Pacotes / Módulos instalaveis, e outros já pré definidos
# Quando vc cria um programa em python ele vem com o básico

# Ex: corpo  humano, vc adiciona alguns módulos durante o dia como bebida, comida, doce... podemos chamar cada um desses
# grupos como bibliotecas, em progrmação podemos fazer importações de bibliotecas

# PARA INCLUIRMOS ALGUMA COISA USAMOS O COMANDO     import "nome da biblioteca"   , e assim podemos usar tudo o que vem
# com a biblioteca

# Se quiser importa apenas algo da biblioteca para não importala toda usamos o comando from "nome da biblioteca" import "nome do que vc quer da biblioteca"

# ex:  de bibliotecas
#
# math - matemática, traz algumas funcionalidades matemáticas extras
  # ceil - faz um arredondamento para cima de números
  # floor - faz um arredondamento para baixo
  # trunc - truncate, elimina da virgula para frente
  # pow - potência funciona similar a **
  # sqrt - square root, raiz quadrada
  # factorial - fatorial
# ex: importar
#
# import math - importa todas as funcões da biblioteca
# from math import sqrt - importa somente a função de raiz quadrada
# from math import sqrt, pow - importa as duas funções

# PRÁTICA

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)  # ao importar "math" e usar "math."  aparece todas as funcionalidades de biblioteca
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) # o math.ceil(raiz) é para aredondar para cima o valor de raiz

