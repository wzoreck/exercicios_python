# Empacotamento permite que vários parâmetros sejam passados por referência sem a necessidade de sobreescrita de função

# Neste caso numeros é uma tupla
def contador(* numeros):
    print(numeros)
    
    soma = 0

    for valor in numeros:
        soma += valor

    print(soma)


contador(1, 2, 3, 4, 5)
contador(2, 4, 6, 8)
contador(1)