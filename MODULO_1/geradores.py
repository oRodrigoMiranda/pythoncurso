#função geradora, nao aloca tudo de uma vez.. ela vai armazenando 
#conforme solicitado.

from pympler.asizeof import asizesof

def dobro():
    i = 0
    while True:
        i += 1
        yield i
    

x = dobro()
print(next(x))
print (f"o próximo é o  {next(x)}")
print(next(x))
print (f"o próximo é o  {next(x)}")



