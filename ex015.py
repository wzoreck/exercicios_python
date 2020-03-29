# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R%60 por dia e R$0,15 por Km rodado
Km = float(input('Digite quantos Km foram rodados com o carro: '))
dias = int(input('Digite quantos dias o carro ficou alugado: '))
p_dia = dias * 60
p_km = Km * 0.15
total = p_dia + p_km
print('O veiculo ficou {} dias alugados e rodou {}Km, o total a pagar é R${:.2f}'.format(dias, Km, total))
