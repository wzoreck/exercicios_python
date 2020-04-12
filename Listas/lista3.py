pessoa = list()
turma = list()

for i in range(0, 4):
	pessoa.append(str(input('Informe seu nome: ')))
	pessoa.append(int(input('Informe sua idade: ')))
	turma.append(pessoa[:])
	pessoa.clear()

print(f'\n{turma}')