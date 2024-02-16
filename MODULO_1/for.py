lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)    
for elemento in tupla:
    print(elemento)

pessoa = {"nome":"joao", "idade":30,"cidade":"São Paulo"}    

print("\nFor utilizando dicionário-chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionário-valores")
for chave in pessoa.values():
    print(chave)    

print("\nFor utilizando dicionário-itens")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")


#range() - retorna um intervalo numérico em formato de lista

lista = list(range(0,10))
print(lista)        

print("\nUsando a função range")
for numero in range(5):
    print("Numero: ", numero)

print("\nUsando a função range com len")
for numero in range(len(lista)):
    print("Numero: ", numero)


print("\nUsando a função enumerate")
#enumerate() - já separa o indice e o valor sem precisar usar o items()
lista_enumerate = ["a","b","c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}:{valor}")

    