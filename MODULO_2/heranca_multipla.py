class Animal:
    def  __init__(self, nome) -> None:
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Emitindo sons ultrassônicos"
    
morcego = Morcego("Batman")
print(morcego.emitir_som()    )