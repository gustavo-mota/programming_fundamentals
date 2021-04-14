#algoritmo 1.19 CC
n=int(input("digite um valor: "))
contador=1
r=1
while contador<=n:
    if n%r==0:
        print(r)
    r=r+1
    contador=contador+1