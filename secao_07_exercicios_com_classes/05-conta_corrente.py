#EXERCICIO 5...

#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.

#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.

#Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios

class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

# TESTE DA CLASSE

conta = ContaCorrente(100, 'Tales')
conta.deposito(100)
print(conta.saldo)
conta.saque(200)
print(conta.saldo)

