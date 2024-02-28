#Snake Case
nome_completo = "Rodrigo Miranda"
nome = "Rodrigo"
sobrenome = "Miranda"
idade = 43

#CamelCase
nomeCompleto = "Rodrigo Miranda"

#quebra de linha
nome_completo_aspas = """Rodrigo
Miranda"""

nome_completo_quebra = "Rodrigo \
Miranda"

#Inteiro
numero_inteiro = 3
print("Inteiro = ", numero_inteiro)


#Real com ponto flutuante
numero_real = 3.14
print("Real com ponto flutuante = ", numero_real)



#Formatação
print ("Nome Completo: ", nome_completo)
print ("Nome Completo: " + nome_completo)
print ("Nome Completo: " + nome + sobrenome)

print ("nome completo aspas: ", nome_completo_aspas)
print ("nome completo quebra: ", nome_completo_quebra)

print ("Nome completo: %s" % nome_completo)
print ("Nome completo: %s %s" % (nome, sobrenome))
print (f"Nome completo: {nome} {sobrenome}")
print ("Nome completo: {} {}".format(nome, sobrenome))

print (nome.upper())
print (nome.lower())

print (nome[0])

#codificar em bytes
nome.encode() 
nome.count("a") #conta as ocorrencia da letra a
nome.find("a") #mostra a localização da primeira ocorrencia da letra a
nome.encode().decode 
nome_completo.replace("b","a") #substitui a letra b por a
telefone = "(21)99875-2254"
telefone.replace("(", "")
telefone.replace("(", "").replace(")", "").replace("-","")

"-".join("Rodrigo")

nomes = nome_completo.split(" ") #o espaço já é o padrao

nome = "xRodrigo Mirandax"
nome.strip("x")
#rstrip #lstrip

nome_completo.startswith("Ro") #começa com?
"dr" in nome_completo
"dr" not in nome_completo


#LISTAS

minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

print (minha_lista)



