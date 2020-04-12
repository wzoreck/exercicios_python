nome = list()

nome.append('Daniel')
nome.append('Pafuncio')
print(nome)

print('---------------------')
# As "listas" variaveis apontam para um mesmo endereço de memória
x = [1, 2, 3, 4]
y = x
print(x)
print(y)
y[1] = 9 # A alteração feita em qualquer um altera a lista
print(x)
print(y)

print('---------------------')
# Fazer uma cópia dos valores
y = x[:] # Desta forma y recebe uma cópia de todos os valores da lista
y[1] = 7
print(x)
print(y)

# Listas compostas são listas dentro de listas
print('\nLISTAS COMPOSTAS\n')
teste = [['Daniel', 19], ['João', 30], ['Maria', 20], ['Ana', 30]]
print(teste)
print(teste[0])
print(teste[1])
print(teste[2])
print(teste[3])
print(teste[0][0])
print(teste[0][1])
print(teste[1][0])
print(teste[1][1])
print(teste[2][0])
print(teste[2][1])
print(teste[3][0])
print(teste[3][1])

print('---------------------')
# Forma mais prática
for p in teste:
	print(f'{p[0]} tem {p[1]} anos')