#algoritmo 1.22 without. obs: prefiro fazer com lista
p=1
s=1
r=2
j=0
n=int(input("digite um inteiro: "))
print(p)
print(s)
while r<n:
    j=p+s
    p=s
    s=j
    print(s)
    r=r+1