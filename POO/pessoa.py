class Pessoa:

    # __init__ é o metodo construtor da classe, neste caso o parametro adulto já possui um valor padrão,
    # caso não seja informada vai ficar com o valor padrão
    def __init__(self, nome, idade, adulto=False):
        self.nome = nome
        self.idade = idade
        self.adulto = adulto

        # Se for criado sem o self será uma variável local desse escopo, não poderá ser usada mais dentro da classe
        # Já com self se torna um atributo da classe
        teste = 'teste'

    # self é similar ao this no Java, quando falar() for chamado na Main o self irá se referir a instância criada
    def falar(self):
        print(f'{self.nome} está falando')
        #print(f'{nome} está falando')  Não funciona
        #print(f'{teste} não funciona')
    
    def isAdulto(self):
        if self.adulto == True:
            print(f'{self.nome} é adulto')
        else:
            print(f'{self.nome} não é adulto')
    
    def getNome(self):
        return self.nome
