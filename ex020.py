# O mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos. Faça um programa que leia o nomedos quatro
# alunos e mostre a ordem sorteada
from random import choice, shuffle
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]

'''p = choice(lista)
s = choice(lista)
t = choice(lista)
q = choice(lista)
print('Será {}, {}, {} e {}'.format(p, s, t, q))'''

shuffle(lista) # embaralha a lista
print('Será {}'.format(lista))
