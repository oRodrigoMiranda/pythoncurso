
"""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

try:
    print (n1/n2)
except:
    print ("Nao consegui realizar a operação")
finally:
    print ("Beleza.")    #sempre é executado!


#especificando a exceção
try:
    x = int(input("digite um numero: "))
    print (5/x)
except ValueError:
    print("Digite um numero inteiro!")    
except ZeroDivisionError:
    print('Nao digite 0!')    
"""

try:
    x = int(input("digite um numero: "))
    print (5/x)
except Exception as e:   #captura a exceção pra variável
    print(e)
