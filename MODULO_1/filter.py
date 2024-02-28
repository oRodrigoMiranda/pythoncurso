"""
Perceba que a principal diferença está na função, no caso do filter o resultado é somente dos valores que atendem a condição → true e 
mesmo atendendo a condição o valor é exibido sem alteração.

Essas duas funções são muito úteis para quando estamos trabalhando com um volume grande de informações, listas, dicionários, tuplas, 
podemos usar para filtrar por tipo ou aplicar diversas edições usando o map.

Resumo:

Quando queremos a lista completa editando as informações que temos dentro dela, vamos usar o map.
Quando queremos filtrar essa lista para pegar os itens que correspondem a uma condição vamos usar o filter.
Ambas percorrem toda a lista como o For teria feito, mas, mais rápido.
"""

idades = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

a = list(filter (lambda x: x < 18, idades))

#print(a)


precos_produtos = [5000, 9000, 2000, 15000]

def aplicar_aumento_map(preco):
    if preco > 6000:
        return preco * 1.1
    else:
        return preco
    
def aplicar_aumento_filter(preco):
    if preco > 6000:
        return True
    else:
        return False

precos_novos_m = list(map(aplicar_aumento_map, precos_produtos))
precos_novos_f = list(filter(aplicar_aumento_filter, precos_produtos))
print (f"MAP, aplicando valores: {precos_novos_m}")
print (f"FILTER, somente mostrando os valores: {precos_novos_f}")


precos_novos_l = list(filter(lambda x: x>6000, precos_produtos))
precos_novos_m = list(map(lambda x: x*1.1 if x > 6000 else x, precos_produtos))

                      
a = list(filter (lambda x: x < 18, idades))
print(a)
print(precos_novos_l)
print(precos_novos_m)



#########################

x = [{"nome":"celso", "idade":43}, {"nome":"rodrigo", "idade":15},{"nome":"pedro", "idade":10}]

x = list(map(lambda x: {"nome":x["nome"],"idade":22} if x["idade"] < 18 else(x),x)) 
print(x)