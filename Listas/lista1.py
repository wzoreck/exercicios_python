# Tuplas ()
# Listas []

lanche = ['Pipoca', 'Coxinha', 'Pastel']
#lanche[4] = 'Arroz' # Isso não funciona, é necessário reservar endereço de memória
lanche.append('Arroz')

print(lanche)

lanche.insert(1, 'Coca-Cola') # Inserir no indice 1, o que estava no indice 1 foi para o 2
print(lanche)

# Deletar
del lanche[0]
print(lanche)
lanche.pop(2)
#lanche.pop() Remove o ultimo elemento sempre!
print(lanche)
lanche.remove('Coxinha')
print(lanche)

# Criar Lista com Range
numeros = list(range(0, 100))
#print(numeros)

x = [1, 6, 9, 2, 0]
print('Desordenado {}'.format(x))
x.sort()
print('Ordenado {}'.format(x))
x.sort(reverse=True)
print('Ao contrário {}'.format(x))

'''
if 30 in numeros:
	numeros.remove(30)
else:
	print('Número não encontrado!')
'''

# Forma de printar com For de forma horizintal
for i in x:
	print(f'N: {i} ', end='')