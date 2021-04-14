#algortimo 1.17 CC
A = int(input("Valor A: "))
B  = int(input("Valor B: "))
if B<0:
    B=B*-1
if A<0:
    A=A*-1
if A<B:
    S=A-B
    print("Não se divide.")
r=A
while r>B:
    r=r-B

quociente=r+5
print("Quociente eh:", quociente)
print("O resto eh:", r)