#abstração, encapsulamento, herança e polimorfismo


#Exemplo de herança

class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

    def andar(self):
        print(f"O animal {self.nome} andou")
        pass


class Cachorro(Animal):
    def emitir_som(self):
        return "Au, au"

class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


print ("\nExemplo de encapsulamento")

class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #atributo privado. Acessível somente pela classe

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo


conta = ContaBancaria(saldo=1000)
print (f"saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print (f"saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print (f"saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print (f"saldo da conta bancária: {conta.consultar_saldo()}")


#numa classe abstrata nao permite criar objetos a partir dela. ela é somente um molde
print ("\n\nExemplo de Abstraçaõ")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod    
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro ligado usando a chave"

carro_amarelo = Carro()    
print(carro_amarelo.ligar())