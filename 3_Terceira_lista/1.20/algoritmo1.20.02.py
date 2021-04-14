#algoritmo 1.20 CC
n=int(input("digite um valor: "))
while n>0:
    n=n-1
    j=2
    primo=True
    while j<n and primo==True:
        if n%j==0 and primo==True:
            primo=False
        j=j+1
    if primo==True:
        print(n)