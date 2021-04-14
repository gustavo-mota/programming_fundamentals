#algoritmo 1.16 CC
A = int(input("Valor A: "))
B  = int(input("Valor B: "))
if B<0:
    B=B*-1
if A<0:
    A=A*-1
if A<B:
    print("Resto", A)
r=A
while r>B:
    r=r-B

print(r)