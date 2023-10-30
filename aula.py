class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class AnalistaSistemas:
    def __init__(self, nome, idade, linguagem):
        super().__init__(nome, idade)
        self.linguagem = linguagem
