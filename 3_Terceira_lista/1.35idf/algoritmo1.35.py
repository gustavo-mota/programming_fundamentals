#algoritmo 1.35 without
x=int(input("Digite o valor de x: "))
j=1
fatx=1
e=1+x
i=1
r=2
s=2
while i<=16:
    while j<=s:
        fatx = fatx * j
        j = j + 1
    e=e+((x**r)/fatx)
    r=r+2
    i=i+1
print(e)