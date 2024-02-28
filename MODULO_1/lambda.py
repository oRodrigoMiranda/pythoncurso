a = lambda : 10
b = lambda nome, idade: print (f"nome: {nome} \nidade: {idade}")
c = lambda *idade: print(idade) #args.. empacota os argumentos numa tupla

def teste():
    return lambda *idade: print(idade)


x = teste()

x('caio')




palavra_antes = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None 
sentenca = 'Rato Roeu Roupa Rei Roma'
print(palavra_antes(sentenca,'Roma')) # Rei