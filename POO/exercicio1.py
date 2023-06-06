class Humano:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    def __str__(self):
        return f"nome: {self.nome}idade: {self.idade} cpf: {self.cpf}"
alexa = Humano('Ana', 20, 252525)

print(alexa)
