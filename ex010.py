# Crie um programa que leia quanto dinheiro uma pessoa tem na careira
# e mostre quantos dólarees ela pode comprar
reais = float(input('Digite quantos reais você possui: '))
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(reais,reais/3.7))
