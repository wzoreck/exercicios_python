# adição________________|  +  |
# subtração_____________|  -  |
# multiplicação_________|  *  |
# divisão_______________|  /  |
# potência______________|  ** |
# divisão inteira (div)_|  // |
# resto  divisão (mod)__|  %  |
# recebe________________|  =  |
# igual_________________|  == |

# Ordem de Precedência
# 1_____|       ()      |
# 2_____|       **      |
# 3_____|  *, /, //, %  |
# 4_____|      +, -     |


# Alinhamento

# vai utilizar 20 espaços para escrever a variável
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome))

# vai utilizar 20 espaços para escrever a variável, e alinhar o nome a direita
print('Prazer em te conhecer {:>20}!'.format(nome))

# vai utilizar 20 espaços para escrever a variável, e colocar '=' a direita e esquerda
print('Prazer em te conhecer {:=^20}!'.format(nome))


# EXEMPLOS Operadores Aritméticos
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
# print('A soma vale {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {0}, O produto é {1}, a Divisão é {2:.3f}'.format(s, m, d)) # ":.3f" formatação para aparecer 3 casas após a virgula
print('Divisão inteira {} e potência {}'.format(di, e))

print('\n ')

# para não haver quebra de linha "end=''"
print('A soma é {0}, O produto é {1}, a Divisão é {2:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))

print('\n ')

# quebra de linha "\n"
print('A soma é {0}, \n O produto é {1}, \n a Divisão é {2:.3f}'.format(s, m, d)) # ":.3f" formatação para aparecer 3 casas após a virgula
print('Divisão inteira {} e potência {}'.format(di, e))
