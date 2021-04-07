from pessoa import Pessoa

juca = Pessoa('Juca', 20)
ze = Pessoa('Ze', 30, True)

juca.falar()
ze.isAdulto()

nome = ze.getNome()
print(f'O nome é {nome}')