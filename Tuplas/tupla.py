'''
Existem 3 tipos de variáveis compostas em Python: Tuplas, Listas e Dicionários

tupla ()
lista []
dicionário {}

Tupla - Similar a um vetor, posições são acessadas por índices 0, 1, 2...
As tuplas são imutáveis, se declaradas e atribuidas valores uma vez, não é possível alterar
'''

# Toda tupla é entre parênteses, nas versões mais novas do Python não é necessário, mas é uma boa prática.
# Declaração e atribuição:
pessoa = ('João', 'Maria', 'Juca', 'Ana', 'Pedro')

# Outra forma de declarar uma tupla
comida = 'Arroz', 'Feijão', 'Batata', 'Macarrão'

# Printar a tupla e todos os seus valores
print(pessoa)

# Printar por índice
print(pessoa[0])
print(pessoa[1])
print(pessoa[2])
print(pessoa[3])
print(pessoa[4])

print('----------------------------')

# Outras formas úteis quando não se sabe o índice extato da ultima ou penúltima posição
print(comida[-1]) # Macarrão
print(comida[-2]) # Batata

print('----------------------------')
# Print apartir da 3ª pessoa até o final da tupla (há varias formas de fazer essas manipulações)
print(pessoa[2:])

# 
print(comida)

# Organizado
print('Sorted: ',sorted(comida))

print('----------------------------')
# A variável i receberá um valor da tupla por vez!
for i in comida:
	print(i)


print('----------------------------')
for i in pessoa:
	if i == 'Ana':
		print('Encontramos a Ana!!!!!!!')

for i in range(0, len(pessoa)):
	if pessoa[i] == 'Ana':
		print(f'Posição índice onde Ana está alocada {i}')

print('----------------------------')
# Outra forma
for i, c in enumerate(comida):
	print(f'Comida: {c}, posição: {i}')


print('----------------------------')
# Teste de atribuição em por índice na tupla, para mostrar que não funciona!!
pessoa[1] = 'Daniel'
print(pessoa)
