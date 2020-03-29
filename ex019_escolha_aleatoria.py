# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
a1 = str(input('Digite o nome do primeiro aluno: ')) # str não é obrigatório
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4] # criando uma lista, com quem vai participar dela, uma lista em python fica em []
#ex:
#compras = ['pão', 'leite', 'carne']
escolhido = random.choice(lista) # choice randomiza um valor (escolhe um valor)
print('O aluno escolhido foi {}'.format(escolhido))
