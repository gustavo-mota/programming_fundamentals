#algoritmo 1.39 CC
a=5000000
b=7000000
ano=1
while a<=b:
    a=(a*0.03)+a
    b=(b*0.02)+b
    ano=ano+1
print('Necessário cerca de:',ano, "anos")