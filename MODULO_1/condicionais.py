

idade = int(input("Qual a sua idade? "))

print ("Exemplo de comando if")

if idade >= 18:
    print("você é maior de idade")
elif idade >=12:
    print("você é adolescente")
else:
    print("você é menor de idade")



mensagem = "Pode tirar a carteira" if idade >= 18 else "Você nãõ pode tirar a carteira"
print(mensagem)