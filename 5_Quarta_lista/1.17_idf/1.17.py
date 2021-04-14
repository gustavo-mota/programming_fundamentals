#Algoritmo 1.17 CC
x=[]
y=[]
n=int(input("Digite quantos elementos há nos vetores: "))
for i in range(1,n+1):
    X=int(input("Digite um termo: "))
    x.append(X)
for j in range(1,n+1):
    Y=int(input("Digite um termo: "))
    y.append(Y)
somavetor=0
for s in range(0,n):
    p=x[s]*y[s]
    somavetor=somavetor+p
print(somavetor)