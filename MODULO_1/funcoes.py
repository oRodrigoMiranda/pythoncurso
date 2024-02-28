#Exemplo
def saudacao(nome):
    print("Seja bem vindo,",nome)

print("\nChamando a função saudacao")
saudacao("Rodrigo")
saudacao("Tiane")

def soma_args(*args):
    soma=0
    for i in args:
        soma += i
    return soma

def soma_kwargs(**kwargs):
    return sum(kwargs.values())



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

print(soma_args(1,2,3,4,5,6,7,9,10))
print(soma_kwargs(n1 =1, n2 = 5, n3 = 8))