# Tipos primitivos básicos em pythom


# int (números inteiros ...-2,-1,0,1,2,3...)
# float (números quebrados com ponto flutuante "tambem conhecido como real" 4.5, 0.001, -1.5  "Se utiliza ponto pois é o padrão internacional")
# bool (família dos booleanos, aceita somente 2 valores True, False "A primeira letra tem que ser maiúscula e o restante minúscula")
# str (String 'Olá' ou "Olá", '7', '' -string vazia)


# print('texto {}'.format(variável)) # sintaxe nova do python 3, O valor da variável aparecerá na string sem necessidade de ficar agrupando strings e variáveis

# juntar strings chama-se concatenação


# Exemplos type()

n1 = input('Digite um valor: ')
print(type(n1)) # type() indica o tipo da variável

n1 = int(input('Digite um valor: '))
print(type(n1))

# Exemplo .format()

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
# print('A soma entre ', n1, 'e', n2, 'vale', s) # formato antigo do python, mas ainda válido
print('A soma entre {} e {} vale {}'.format(n1, n2, s))


# Exemplo bool

n = bool(input('Digite um valor: '))
print(n) # se receber um valor vai dar True, senão False


# Mandar escrever várias coisas sobre o tipo do valor de entrada ou string

e = input('Digite algo: ')
print('númerico = ',e.isnumeric(),', Alfabético = ', e.isalpha(), ', Alphanumérico = ', e.isalnum()) # .isnumeric "Diz se é numerico", .isalpha "Diz se é letra"
