#Exemplo
def saudacao(nome):
    print("Seja bem vindo,",nome)

print("\nChamando a função saudacao")
saudacao("Rodrigo")
saudacao("Tiane")



def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:",resultado_quadrado)


#funcao com multiplos parametros
def soma(n1, n2):
    resultado = n1 + n2
    return resultado

numero1=10
numero2=8

print("\nChamando funcao Soma")
resultado_soma = soma(numero1,numero2)
print("A soma dos numeros %s e do numero %s é %s" % (numero1, numero2, resultado_soma))
