#algoritmo 1.32 CC
i=1
s=1
x=1
denominador=3
while i<=51:
   if i%2==0:
        s=s+(1/(denominador**3))
   else:
        s=s-(1/(denominador**3))
   i=i+1
   denominador=denominador+2

s=(s*32)**1/3
print("Valor de pi e:", s)
