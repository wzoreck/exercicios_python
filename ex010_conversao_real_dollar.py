# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
reais = float(input('Digite quantos reais você possui: '))
print('Com R${:.2f} você consegue comprar US${:.2f}'.format(reais,reais/3.7))
