# Cadeia de caracteres é o que conhecemos como frase
# Cadeia de caracteres, string ou cadeia de texto é tudo a mesma coisa
# as strings em python são salvas em vetores com índices


# Fatiamento de string

# variavel['posição do índice']
# variável['posições do índice'] ex: variável[9:13] vai do 9 até o 12, é sempre um a menos no final
# ex: variável[9:21:2] vai do 9 ao 20, e o dois no final significa que vai pulando de 2 em dois
# variável[:'posição indice'] vai do 0 até um a menos que a posição do indice indicada
# variável['posição indice':]  vai da posição indicada até o final da string
# variável['posição'::'posição'] vai da primeira posição até o final, vai pular e mostrar conforme a segunda posição

# Análise de string

# len(variável)  qual o comprimento da frase
# variável.count('o')  conta quantas vezes aparece a letra "o" minúscula
# variável.count('o', 0, 13)  conta quantas vezes aparece a letra "o" minúscula do 0 ao indice 12
# variável.find('deo')  vai dizer quantas vezes encontrou "deo" mostrando aonde começou no indice
# variável.find('deo')  caso o que for procurado não exista na frase vai retornar -1
# 'palavra' in variável  via ver se existe e retornar true ou false


# Trnasformação de string

# variável.replace('test', 'teste')  vai encontrar test e substituir por teste
# variável.upper()  Vai deixar tudo em maúsculas, o que já está em maiúsculo mantem
# variável.lower()  Vai deixar tudo em minúsculo
# variável.capitalize()  Vai jogar tudo para minúsculo e só o primeiro vira maiúsculo
# variável.title()  Vai analisar quantas palavras tem e vai fazer igual o anterior só que a cada palavra vai iniciar com maiúscula

# variável.strip()  Vai remover espaços inúteis no inicio e no fim
# variável.rstrip()  Vai remover espaços inúteis no fim(direita) "r de right"
# variável.lstrip()  Vai remover espaços inúteis no inicio(esquerda) "l de left"


#  Divisão de string

# variável.split()  onde tiver espaço vai criar uma divisão, cada palavra recebe indexação nova (indices novos), cada palvra é colocada dentro de uma outra lista (0,1,2..)

# Junção de string
# '-'join(variável)  vai juntar todos elementos e juntalos com - ao invés  dos espaços, pode-se utilizar logo após o split


# Prática

frase = '   O gato roeu a roupa do rei de Roma  '
print(frase)

print(frase[30]) # vai mostrar a letra na posição de indice 30

print(frase[0:30]) # vai do indice 0 até o 29

print(frase[0:29:2]) # vai do 0 até o 28, pulando de  2 em 2

print(frase[::2 ]) # vai pulando de 2 em 2 em todo o texto

print("""\nkjegbawkjgbsgnsdgbsdnga
gsakdngaskdgnasdfhg
akãksdnfbgaçldfkg]alkg
sçaash]asçlçasdlfmhçalsdmfh
WEGJWEPIORUGHTPQWEUIRBGT[W  OJ
G OPEJGB[PEOAGREHG\n""")

print('Dentro da frase existem isso de letras o minúsculas: ',frase.count('o')) # count conta

print('\nDentroda frase existem isso de letras O maiúsculas: ',frase.upper().count('O')) #com upper deixamos toda a string maiúscula

print('\n', len(frase)) # ver o tamanho da frase (quantos indices existem)

print('\n', frase.strip()) # tira os espaços indesejáveis no início e fim

print('\n', len(frase.strip()))

print(frase.replace('gato', 'camundongo')) # troca a palavra gato por camundongo

nova_frase = frase.replace('gato', 'camundongo') # mesma anterior só que salva em uma variável com as alterações, já que em python a string é imutável
print(nova_frase)

print('\n', 'gato' in frase) # vai verificar se a palavra gato está dentro da variável frase, True ou False

print('\n', frase.find('gato')) # vai dizer em que indice se encontra a letra g de gato, caso não exista retorna -1

print('\n', frase.split()) # cria uma lista onde cada frase é separada
dividido = frase.split() # recebe a frase splitada
print(dividido[4]) # vai mostrar  o indice 4 (palavra) da frase que foi dividida

print(dividido[4][0]) # mostrar a primeira letra da palavra no indice 4