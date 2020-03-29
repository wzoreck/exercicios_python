# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
# com 5% de desconto
preco = float(input('Digite o preço de um produto: '))
desconto = preco * 0.05
valor_f = preco - desconto
print('O valor digitado foi R${} com 5% de desconto fica R${:.2f}'.format(preco, valor_f))
