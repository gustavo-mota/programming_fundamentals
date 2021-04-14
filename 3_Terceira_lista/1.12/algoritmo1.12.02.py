#algoritmo 1.12 CC
n=int(input("digite um valor: "))
j=1
print("Os seguintes valores são os multiplos de 3 e 5 ao mesmo tempo.Se nenhum surgir, significa que não nenhum há naquele intervalo")
while j<=n:
    if j%3==0 and j%5==0:
        print(j)
    j=j+1
