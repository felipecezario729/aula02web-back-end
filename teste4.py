funcionariosParaCadastrar = [

    {"nome": "Pablo", "sobrenome": "Araujo", "idade": 34, "altura": 1.71, "temHabilitacao": True},​

    {"nome": "Ana", "sobrenome": "Silva", "idade": 28, "altura": 1.65, "temHabilitacao": False},​

    {"nome": "Carlos", "sobrenome": "Souza", "idade": 40, "altura": 1.80, "temHabilitacao": True}​

]

cadastrosParaEnviarParaOBanco = []
class pessoas:
    def __init__(self, nome, sobrenome, idade, altura, habilitacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.altura = altura
        self.habilitacao =  habilitacao


    def informacao(self):
        print(f"O usuario{self.nome} {self.sobrenome} foi salvo com sucesso.")

