palavra = str(input('Informe uma palavra: '))

if palavra == 'ola mundo':
	print('Acertou!')
else:
	print('Errou!')
	
print('-----------------------')

print('Você é fera' if palavra == 'ola mundo' else  'Não foi dessa vez')