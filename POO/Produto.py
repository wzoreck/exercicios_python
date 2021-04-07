class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    # Com esses decoradores os metodos abaixo são chamados até na passagem de parâmetro do construtor, é uma
    # diferença existente entre Python e outras linguagens

    # Decorador @property usado para informar um prioridade
    @property
    def preco(self):
        # Para evitar problemas com loop coloca-se um _ antes do nome do atributo
        return self._preco

    # Criação de metodo setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$',''))
        self._preco = valor

