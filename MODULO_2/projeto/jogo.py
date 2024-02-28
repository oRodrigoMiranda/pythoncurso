import random
import os
#Personagem: classe mãe. tem td em comum dos personagens
#heroi: derivado de personagem, controlado pelo usuário
#inimigo: derivado de personagem, adversario do usuário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
       
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)                   #self.__nivel * 2
        alvo.receber_ataque(dano)
        print (f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")


    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}"

    def ataque_especial(self,alvo):
        dano = random.randint(self.get_nivel() *5, self.get_nivel() * 8)    #self.get_nivel() * 5 #dano aumentado
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} e causou {dano} de dano")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    """ Classe orquestradora do jogo"""
    
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Ryu",vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Vegetta", vida=80, nivel=5, tipo="Maijyn")

    def iniciar_batalha(self):

        os.system('cls')  or None
        """ Fazer a gestão da batalha em turnos"""
        print("Iniciando a batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print ("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input ("\nPressione ENTER para atacar...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque especial): ")

            if escolha == "1":
                print("\n")
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                print("\n")
                self.heroi.ataque_especial(self.inimigo)
            else:
                print ("Escolha inválida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
            input()
            os.system('cls')  or None

        
        if self.heroi.get_vida() > 0:
            print("\nParabéns, você venceu a batalha!!!")
        else:
            print(f"\nVocê foi derrotado por {self.inimigo.get_nome()}")







#cRIAR INSTANCIA DO JOGO E INICIAR BATALHA
jogo = Jogo()            
jogo.iniciar_batalha()




