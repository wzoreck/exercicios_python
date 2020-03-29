# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input('\nDigite um número:'))
#dobro = n1 * 2
#triplo = n1 * 3
#raiz = n1 ** (1/2)
#print('\nO dobro de {} é {} \n'.format(n1, dobro))
#print('O triplo de {} é {}\n'.format(n1, triplo))
#print('A raiz de {} é {:.2f}'.format(n1, raiz))

print('\nO dobro de {} é {}\n'.format(n1, (n1*2)))
print('O triplo de {} é {}\n'.format(n1, (n1*3)))
print('A raiz de {} é {}'.format(n1, (n1**(1/2))))
