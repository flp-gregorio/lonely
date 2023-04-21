#Felipe Alves Gregorio - 2022008250

from abc import ABC, abstractmethod
import datetime as dt
from datetime import date

class Transacao:
    def __init__(self, data, valor, descricao):
        self.data = data
        self.valor = valor
        self.descricao = descricao

class Conta(ABC):
    def __init__(self, nome, numC, saldo):
        self.__nome = nome
        self.__numC = numC
        self.__saldo = saldo
        self.__listaTrans = []
    @property
    def nome(self):
        return self.__nome
    
    @property
    def numC(self):
        return self.__numC
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novoSaldo):
        self.__saldo = novoSaldo

    @saldo.getter
    def saldo(self):
        return self.__saldo
    
    @abstractmethod
    def imprimirExtrato(self):
        pass

    def depositar(self, valor):
        self.saldo += valor
        transacao = Transacao(date.today(), valor, 'Depósito recebido. Valor: ')
        self.__listaTrans.append(transacao)
        print("Transação Aprovada.")
    
    def retirar(self, valor):
        if(self.saldo > valor):
            self.saldo -= valor
            print("Transação Aprovada.")
            transacao = Transacao(date.today(), valor, 'Débito Realizado. Valor: ')
            self.__listaTrans.append(transacao)
        else:
            print("Transação Negada.")

class ContaCorrente(Conta):
    def __init__(self, nome, numC, saldo):
        super().__init__(nome,numC, saldo)
        self.__listaTrans = []
    
    def imprimirExtrato(self):
        print("\nConta Corrente")
        print("Número da Conta:", self.numC)
        print("Nome do Correntista:", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__listaTrans:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)

class ContaLimite(Conta):
    def __init__(self, nome, numC, saldo, limite):
        super().__init__(nome,numC, saldo)
        self.__listaTrans = []
        self.__limite = limite

    def retirar(self, valor):
        if(self.saldo - valor > -1 * (self.__limite)):
            self.saldo -= valor
            print("Transação Aprovada.")
            transacao = Transacao(date.today(), valor, 'Débito Realizado. Valor: ')
            self.__listaTrans.append(transacao)
        else:
            print("Transação Negada.")

    def imprimirExtrato(self):
        print("\nConta Limite")
        print("Número da Conta:", self.numC)
        print("Nome do Correntista:", self.nome)
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__listaTrans:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)

class ContaPoupança(Conta):
    def __init__(self, nome, numC, saldo, dataAni):
        super().__init__(nome,numC, saldo)
        self.__listaTrans = []
        self.__diaAniversario = dataAni

    @property
    def diaAniversario(self):
        return self.__diaAniversario
    
    def getAniversario(self):
        return self.__diaAniversario.strftime("%m/%d")

    
    def imprimirExtrato(self):
        print("\nConta Poupança")
        print("Número da Conta:", self.numC)
        print("Nome do Correntista:", self.nome)
        print(f"Dia do Aniversário: ", self.getAniversario())
        print("Saldo:", self.saldo)
        print("Transações:")
        for abb in self.__listaTrans:
            print(abb.data.strftime("%d/%m/%Y"), abb.descricao, abb.valor)
        print("\n")

if __name__ == "__main__":
    conta1 = ContaPoupança("Carla", 1551, 200, date(2000, 8, 30))
    conta2 = ContaCorrente("Tomas", 1763, 1000)
    conta3 = ContaLimite("Jorge", 1993, 40000, 400)

    contas = [conta1, conta2, conta3]

    for conta in contas:
        conta.depositar(100)
        conta.imprimirExtrato()
        conta.retirar(430)
        conta.imprimirExtrato()
