class ContaBancaria:
    def __init__(self,titular='',saldo=0):
        self._titular=titular
        self._saldo = saldo
        self._ativo = False
    def __str__(self):
        return f'Titular: {self.titular} | Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls,conta):
        conta._ativo = True

    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo
    @property
    def ativo(self):
        return self._ativo
    
conta1=ContaBancaria('João',1000)
conta2=ContaBancaria('Maria',2000)

print(conta1)
print(conta2)


conta3 = ContaBancaria("Carlos", 200)
ContaBancaria.ativar_conta(conta3)
print(f"Estado: {conta3._ativo}")

conta4= ContaBancaria('Carlos',900)
print(f'Titular : {conta4.titular}')


class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")