x = (1, 2, 3, 2, 5, 6, 2, 2, 9)
y = (100, 200, 300)
z = x + y # Não soma! Gera uma tupla concatenada
c = y + x
print(z)
print(c)
print(len(z)) # Total de posições
print("Quantas vezes o número 2 aparece: {}".format(x.count(2))) # Quantas vezes o número 2 está aparecendo na tupla x
print("Indice do número 9: {}".format(x.index(9))) # Em que posição "indice" está o numero 9
print("Indice do número 2: {}".format(x.index(2))) # Só informa do primeiro que encontrar
print("Indice do número 2 ignorando o primeiro: {}".format(x.index(2, 2))) # procurando o indice do número 2, apartir indice 2

# Uma Tupla pode ser composta por vários tipos de dados EX:
comida = ('Pastel', 5.50, '"Quente', 100)
print(comida)
del(comida) # Deletando a tupla da memória
