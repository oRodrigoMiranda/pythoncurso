#LISTAS

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]
minha_lista[0] = "python"

print (minha_lista[0]) 
print (minha_lista[1:6]) #fatiando do elemento 1 até o quinto elemento
print (minha_lista[2:]) #começa a mostrar do elemento 2 até o fim
print (minha_lista[:6]) #começa a mostrar do inicio até o elemento 5

#métodos de lista

#Append: adiciona um elemento ao final da lista

minha_lista.append("Rodrigo")
print(minha_lista)

#Index = retorna o índice do primeiro elemenbto especificado
print(minha_lista.index("Rodrigo"))

#Insert = insere o elemento em um índice específico

minha_lista.insert(2, 10)
print(minha_lista)

#metodo pop - remove e retorna  o elemebto removido
elemento_removido = minha_lista.pop(3)
print("elemento removido:",elemento_removido)
print(minha_lista)

#metodo remove= remove o primeiro elemento encontrado na lista
minha_lista.remove(True)
print(minha_lista)

#metodo Sort = ordena a lista
lista2=  [6, 8, 9, 7, 5, 1]
lista2.sort()
lista2.sort(reverse = True) #ordena reverso
print(lista2)

lista3 = sorted(lista2) #cria uma nova lista ordenada

print(lista2)
print(lista3)




