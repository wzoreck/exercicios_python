try:
    print('1' + 2)
except:
    print('Ocorreu uma exceção')


try:
    print('1' + 2)
except Exception as erro:
    # Mensagem personalizada para visualizar melhor o erro
    print(f'A exceção encontrada foi {erro.__class__}')


try:
    print('1' + 2)
except (ValueError, TypeError):
    print('Ocorreu uma exceção com o tipo ou valor informado')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
    # Pode-se ter mais except...


try:
    print('1' + '2')
except:
    print('Ocorreu uma exceção')
else:
    print('Funcionou')


try:
    print('1' + 5)
except:
    print('Ocorreu uma exceção')
else:
    print('Funcionou')
finally:
    print('Independente se deu certo ou errado!')