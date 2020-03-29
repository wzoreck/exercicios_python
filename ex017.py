# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um trângulo retângulo, calcule e mostre a hipotenusa
'''co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2) # matemática pura
print('A hipotenusa vai medir {}'.format(hi))'''

from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = hypot(co, ca) # hypot calcula a hipotenusa basta indicar o cateto oposto e adjacente
print('A hipotenusa vai medir {:.2f}'.format(hi))
