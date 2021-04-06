valores = [1, 2, 3, 4, 5]
print(valores)

def dobrar(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1


dobrar(valores)
print(valores)