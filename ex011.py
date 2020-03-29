# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, cobre uma área de 2m².
largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
qtinta = area / 2
print('A área da parede é {}m^2 será nescessário {}L de tinta'.format(area, qtinta))
