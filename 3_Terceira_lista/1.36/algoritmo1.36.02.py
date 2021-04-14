#algoritmo 1.36 incert
valor=int(input('digite um valor: '))
c_fato=1
fatn=1
c_global=1
d=1
x=2
s=1
y=1
fatd=1
fat=1
while c_fato<=valor:
    fatn=fatn*c_fato
    c_fato=c_fato+1

while c_global<=valor:
    valor=valor-d
    while s<=valor:
        fat=fat*s
        s=s+1
    while y<=x:
        fatd=fatd*y
        y=y+1
    if c_global%2==0:
        fatn=fatn+(fat/fatd)
    else:
        fatn=fatn-(fat/fatd)
    c_global=c_global+1
    x=x+2
    d=d+1
print(fatn)