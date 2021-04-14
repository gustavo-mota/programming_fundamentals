#algoritmo 1.28 without
x=int(input('Digite um valor: '))
somatorio=x
i=1
j=1
fat=1
while i<20:
    s=j
    while j >= 1:
        fat = fat * j
        j = j - 1
    x=x/fat
    if i%2==0:
        somatorio=somatorio+x
    else:
        somatorio=somatorio-x
    i=i+1
    j=s+1
print(somatorio)