from pessoa import Pessoa
from Produto import Produto

juca = Pessoa('Juca', 20)
ze = Pessoa('Ze', 30, True)

juca.falar()
ze.isAdulto()

nome = ze.getNome()
print(f'O nome é {nome}')

print(f'Tem {Pessoa.getIdade(2000)} anos')

camiseta = Produto('Camiseta', 50)
camiseta.desconto(10)
print(f'O preço com desconto fica {camiseta.preco}')