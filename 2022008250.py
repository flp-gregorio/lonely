#Felipe Alves Gregorio - 2022008250

from abc import ABC, abstractmethod

class Domestica(ABC):
    def __init__(self, nome, telefone):
        self._nome = nome
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome

    @nome.getter
    def nome(self):
        return self._nome

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, novoTele):
        self._telefone = novoTele

    @telefone.getter
    def telefone(self):
        return self._telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class Horista(Domestica):
    def __init__(self, nome, telefone):
        super().__init__(nome,telefone)

    @property
    def horasTrabalhadas(self):
        return self.__horasTrabalhadas
    
    @horasTrabalhadas.setter
    def horasTrabalhadas(self, horas):
        self.__horasTrabalhadas = horas
    
    @property
    def valorPorHora(self):
        return self.__valorPorHora
    
    @valorPorHora.setter
    def valorPorHora(self, valor):
        self.__valorPorHora = valor
    
    def getSalario(self):
        salario = self.__valorPorHora * self.__horasTrabalhadas
        return salario
    
class Diarista(Domestica):
    def __init__(self, nome, telefone):
        super().__init__(nome,telefone)

    @property
    def diasTrabalhados(self):
        return self.__diasTrabalhados
    
    @diasTrabalhados.setter
    def diasTrabalhados(self, dias):
        self.__diasTrabalhados = dias
    
    @property
    def valorPorDia(self):
        return self.__valorPorDia
    
    @valorPorDia.setter
    def valorPorDia(self, valor):
        self.__valorPorDia = valor
    
    def getSalario(self):
        salario = self.__diasTrabalhados * self.__valorPorDia
        return salario
    
class Mensalista(Domestica):
    def __init__(self, nome, telefone):
        super().__init__(nome,telefone)
        
    @property
    def valorPorMes(self):
        return self.__valorPorMes
    
    @valorPorMes.setter
    def valorPorMes(self, valor):
        self.__valorPorMes = valor
    
    def getSalario(self):
        salario = self.__valorPorMes
        return salario

if __name__ == "__main__":
    domes1 = Mensalista('Maria', "(31) 62446-1551")
    domes2 = Diarista('Claudete', "(31) 62904-8010")
    domes3 = Horista('Suzana', "(31) 20209-5391")
    domes1.valorPorMes = 1200
    domes2.valorPorDia = 65
    domes2.diasTrabalhados = 20
    domes3.valorPorHora = 12
    domes3.horasTrabalhadas = 160
    domes = [domes1, domes2, domes3]
    
    menorSalario = 999999

    for dome in domes:
        print ('Nome: {} - Telefone: {} - Salario: {}'.format(dome.nome, dome.telefone, dome.getSalario()))
        if(dome.getSalario() < menorSalario):
            menorSalario = dome.getSalario()
            melhorOp = dome


    print ('\nA melhor opcao eh:')    
    print ('Nome: {} - Telefone: {} - Salario liquido: {}'.format(melhorOp.nome, melhorOp.telefone, melhorOp.getSalario()))
