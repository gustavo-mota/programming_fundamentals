#Algoritmo 1.7 CC
contador=1
lista=[]
lista2=[]
soma=0
dia=0
while contador<121:
    temp=float(input("Digite a temperatura: "))
    lista.append(temp)
    soma=soma+temp
    contador=contador+1
media=soma/121
print("a maior temperatura registrada foi",max(lista))
print("A menor temperatura registrada foi",min(lista))
print("Temperatura média:", media)
for elem in lista:
    if elem<media:
        dia=dia+1
print("foram", dia,"dias com temperaturas abaixo da média.")