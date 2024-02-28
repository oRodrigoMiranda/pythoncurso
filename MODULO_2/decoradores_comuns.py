# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10  #atributo de classe
    def __init__(self, nome) -> None:
        self.nome = nome #Atributo da instância

    #requer uma instância pra ser chamado. acessa atributos da classe e da instancia.
    def metodo_instancia(self): 
        return f"Método de instância chamado para {self.nome} {self.valor}"
    
    @classmethod #utilizando ele , recebe a referencia da classe e nao precisa de uma instância para acessar
    def metodo_classe(cls):
        return f"Método da classa chamado para valor={cls.valor}"
    
    @staticmethod #nao recebe argumento. Nao tem acesso nem aos atributos da instancia nem da classe
    def metodo_estatico():
        return "método estático chamado" 
    

obj = MinhaClasse("Classe Exemplo")
print (obj.metodo_instancia())
print (MinhaClasse.valor)
print (MinhaClasse.metodo_estatico())


#EXEMPLO
"""
nesse exemplo usamos o classmethod para criar um método capaz de criar um objeto
com uma configuração diferente. O método criar_carro trata a configuração recebida
como string e retorna uma chamada à classe Carro (que ele recebeu como cls) passando 
as referências no formato esperado.
"""


class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))
    
configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")



#EXEMPLO  static
#permite acessar o método sem precisar criar uma instãncia da classe.
#muito usado por bibliotecas
class Mametica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print (Matematica.somar(a=10, b=15))