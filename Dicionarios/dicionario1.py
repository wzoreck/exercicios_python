# Criando um dicionário
turma = dict()
# ou
pessoa = {'nome':'Daniel', 'idade':19} # 'nome' e 'idade' agora são os "indices"
print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])

# No caso do dicionário, para adicionar mais dados o apend não funciona
# Para adicionar novo dado pode ser feito da seguinte forma
pessoa['sexo'] = 'M'
print(pessoa)

# Excluir dado
del pessoa['idade']
print(pessoa)

print('-------------------')

# titulo, ano, diretor são elementos, o python chama eles de "chaves" "keys"
filme = { 'titulo':'Senhor dos Anéis',
					'ano':2002,
					'diretor':'Peter Jackson'
				}

print(f'Valores: {filme.values()}')
print(f'Chaves: {filme.keys()}')
print(f'Todos itens: {filme.items()}\n')

for chave, valor in filme.items():
	print(f'O {chave} é {valor}')