from math import sqrt, floor
#ctrl + "espaço" mostra todas as funcionalidades

num = int(input('Digite um número: '))
raiz = sqrt(num) # se importar uma funcionalidade pode utiliza-la direto, ñ precisa math.sqrt
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) # mesmo caso aqui
