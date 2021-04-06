def linha():
    print('-' * 30)


linha()
print('Teste 1')
linha()

linha()
print('Teste 2')
linha()

def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('Teste passagem parâmetro função')


def soma(a, b):
    return a + b


print(soma(1, 2))
print(soma(20, 7))