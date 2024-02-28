"""arquivo = open("pessoas.txt","a")
for i in range(0,2):
    arquivo.write(input("Digite o nome da pessoa: ") + " " + input("digite a idade: ") + "\n")
"""
arquivo = open("pessoas.txt","r")
resultados = arquivo.readlines()
arquivo.close()
x=[]
for i in resultados:
    x.append(i.split())
#print(x[1][0])

#o read() vai trazer a linha toda como string
#o readline vai trazer os elementos como lista

#gerenciador de contexto.. mantem o arquivo aberto somente no contexto with.
with open("pessoas.txt","r") as arq:
    x = arq.read()
print(x)