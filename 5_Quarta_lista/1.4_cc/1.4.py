maior=0
soma=0
lista=[]
lista2=[]
for i in range(1,11):
    a=float(input("Digite a altura: "))
    soma=soma+a
    lista.append(a)
media=soma/10
for j in lista:
    if j>media:
        lista2.append(j)
print(media)
print(lista2)