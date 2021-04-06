# Neste caso c funciona como um parâmetro opicional, caso não seja passado um parâmetro para c ele valerá 0
def somar(a, b, c=0):
    s = a + b + c
    print(s)


somar(1, 2, 3)
somar(2, 5)

# Podemos setar diretamente a variável presente na assinatura do método
somar(a=3, b=3)

# Este não funciona pois b é um parâmetro obrigatório 
somar(a=3, c=3)