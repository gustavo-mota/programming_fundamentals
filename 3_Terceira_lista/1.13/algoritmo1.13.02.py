#algoritmo 1.13 CC
n=int(input("digite quantos inteiros deseja inserir: "))
pares=0
impares=0
i=1
while i<=n:
    x=int(input('digite um valor: '))
    if x%2==0:
        pares=pares+1
    else:
        impares=impares+1
    i=i+1
print("Sao", pares, "valores pares inseridos.")
print("Sao", impares, "valores impares inseridos.")