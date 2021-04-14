#algoritmo 1.31 CC
m=int(input("digite um inteiro: "))
s=0
n=1
i=0
while i<m:
    s=s+(1/n**n)
    n=n+1
    i=i+1
print("O somatório resultou:",s)