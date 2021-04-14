#algoritmo 1.26 CC
N = int(input("Digite quantos termos deseja na lista: "))
i=0
lista=[1,4,4]
s=1
j=4
N=N-3
while i<N:
    s=s+1
    j=j+1
    lista.append(s)
    lista.append(j)
    lista.append(j)
    i=i+1
#print("Sua lista gerada:", lista) //Para ver a lista completa gerada.
N=N+3
print(lista[0:N])