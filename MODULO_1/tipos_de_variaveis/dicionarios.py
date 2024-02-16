#Coleçao nao ordenada de chave e valor.

pessoa = {"nome":"Joao", "idade":30, "cidade":"Sao Paulo"}
print("meu dicionario: ", pessoa)
print("Nome: ", pessoa["nome"])
pessoa["sobrenome"] = "miranda"
print("sobrenome: ", pessoa["sobrenome"])


#removendo par chave-valor
print(pessoa)
del pessoa["sobrenome"]
print(pessoa)

#método keys(), values(), items()

chaves= pessoa.keys()
print("chaves: ", chaves)

valores= pessoa.values()
print("chaves: ", valores)

itens= pessoa.items()
print("chaves: ", itens)