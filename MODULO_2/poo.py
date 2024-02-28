# POO

#Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
          self.nome = nome
          self.idade = idade 

    def saudacao(self):
         return f"Olá, meu nome é {self.nome}"

#Objetos
pessoa1 = Pessoa("Alice", 30)
          
print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.saudacao())

pessoa2 = Pessoa("Rodrigo", 32)
print(pessoa2.saudacao())
     