class Pessoa:
    def __init__(self,nome='',idade=0,profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade+=1
    def saudacoes(self):
        if self.profissao:
            return f'Olá, me chamo {self.nome} e o meu trabalho é {self.profissao}'
        else:
            return f'Olá, me chamo {self.nome} e estou desempregado'