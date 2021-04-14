#algortimo 1.15 CC
A = int(input("Valor A: "))
B  = int(input("Valor B: "))
n=0
p=1
if B<0:
    B=B*-1
while n<B:
    p = p*A
    n = n+1
print(p)