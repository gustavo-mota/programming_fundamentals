#-*-coding:utf8;-*-
from random import randint
vetor=[]

for i in range(1,21):
    vetor.append(randint(1,4))
print(vetor)
for i in range(0,19):
    c=0
    for j in range(i+2,19):
        if (vetor[i],vetor[i+1])==(vetor[j],vetor[j+1]):
            c+=1      
    print("A o segmento %s se repete mais %s vezes" %((vetor[i],vetor[i+1]),c))














