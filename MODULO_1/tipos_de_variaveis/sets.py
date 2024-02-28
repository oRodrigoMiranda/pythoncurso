x = {1, 2, 3, 4, 5}
y = {6, 7, 8, 9, 10, 5}
a = ["a", "b", "c", "d", "e", "a", "b"]

b = set(a)  #converte para conjunto, removendo a duplicidade

z = x.union(y)
print(z)

z = x.intersection(y) #tem no x e no y

z = x.difference(y) #retira do x os itens que existem em y
print(z)

z = x.symmetric_difference(y) #mostra a uniao dos conjuntos, sem a intersecção
print(z)