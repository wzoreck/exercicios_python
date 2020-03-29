var1 = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(var1)) # sempre vai ser str pois a função input retorna sempre uma string
print('É um valor alfanumérico: ', var1.isalnum())
print('É um valor numérico: ', var1.isnumeric())
print('É um valor alfabético: ', var1.isalpha())
print('É totalmente maiusculo: ', var1.isupper())
print('É totalmente minusculo: ', var1.islower())
print('Tem maiúsculas e minúsculas: ', var1.istitle())
print('Só tem espaços: ', var1.isspace())
