def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada!")
        func()
        print("Depois da função ser chamada!")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada!")

minha_funcao()


#####################
#vamos definir um decorador que conta o tempo gasto pela função para execução.
import time 
  
  
def timeis(func): 
    
  
    def wrap(*args, **kwargs): 
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
        print(func.__name__, end-start) 
        return result 
    return wrap 
  
@timeis
def countdown(n): 
    
    while n > 0: 
        n -= 1

countdown(5) 
countdown(100000) 





#Decorador de classe
print("\n\n\n")

class MeuDecoradorDeClasse:
    def __init__(self, func) -> None:
        self.func = func
    
    def __call__(self) -> any:
        print("Antes da função ser chamada!")
        self.func()
        print("Depois da função ser chamada!")

@MeuDecoradorDeClasse
def segunda_funcao():
    print("Segunda funcao foi chamada!")        

segunda_funcao()    