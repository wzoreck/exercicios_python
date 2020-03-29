cor = str(input('Informe uma cor (vermelho, verde, azul): '))

if cor == 'vermelho':
	print('Vermelho em inglês é red')
elif cor == 'verde':
	print('Verde em inglês é green') # else if em python é representado por elif
elif cor == 'azul':
	print('Azul em inglês é blue')

# outra forma

if cor == 'vermelho':
	print('É a cor da logo do YouTube')
elif cor == 'verde' or cor == 'azul':
	print('A bandeira do Brasil possui essa cor')
else:
	print('A cor informada é diferente de vermelho, verde e azul')

nome = str(input('Informe um nome comum: '))

# Usando uma lista

if nome == 'Daniel':
	print('Este é meu nome tbm!')
elif nome in 'João Ana Maria Jose Pedro':
	print('É um nome comum')
else:
	print('Não é um nome comum')