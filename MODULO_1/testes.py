palavra_antes = lambda s, w: s.split()[s.split().index(w)-1] if w in s else None 
sentenca = 'Rato Roeu Roupa Rei Roma'
print(palavra_antes(sentenca,'Roma')) # Rei