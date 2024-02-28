#raise obriga que seja levantada uma exceção no programa



"""
def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("N1 e N2 nao podem ser negativos")
    return n1+n2

print(soma(2,-2))
"""

#assert força com que algo seja verdade. o código só segue se for verdade

x = 2
assert x > 0, "deu merda"
print(x)