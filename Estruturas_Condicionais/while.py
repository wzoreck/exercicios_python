n = int(input('Informe um número: '))

contador = 0

while contador <= n:
	print('contador: {}'.format(contador))
	contador += 1

print('\n')

# loop infinito
# while true:

soma = 0

while True:
	n = int(input('Informe um número: '))
	if n == 123:
		break
	soma += n

print('A soma dos números resulta em {}'.format(soma))
# Utilizando f strings python 3 - apartir da versão 3.6 
print(f'A soma dos números resulta em {soma}')
