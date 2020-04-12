aluno = dict()
turma = list()

for i in range(0, 3):
	aluno['nome'] = str(input('\nInforme seu nome: '))
	aluno['idade'] = int(input('Informe sua idade: '))
	turma.append(aluno.copy())

for i in turma:
	print(i)

for i in turma:
	for k, v in i.items():
		print(f'Campo: {k} valor: {v}')