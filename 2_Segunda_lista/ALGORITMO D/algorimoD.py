#Algoritmo item D
preco = float(input("Digite o preco do produto; "))
if preco<=50:
    preco = (preco*0.05)+preco
    print("Novo preço:", preco)
elif 50<preco<=100:
    preco = (preco*0.1)+preco
    print("Novo preco:", preco)
elif preco>100:
    preco = (preco*0.15)+preco
    print("Novo preco:", preco)
if preco <=80:
    print("Classificacao D.")
elif 80<preco<=120:
    print("Classificacao C.")
elif 120<preco<=200:
    print("Classificacao B.")
elif 200<preco:
    print("Classificacao A.")
