#-*-coding:utf8;-*-
from random import randint
vetor=[]
maior=[]
com=[]
for i in range(1,10):
    vetor.append(randint(-10,10))
print("Série: ",vetor)
for i in range(0,len(vetor)):
    com.append(vetor[i])
    for j in range(i+1,len(vetor)):
        com.append(vetor[j])
        if sum(maior)<sum(com):
            maior=list(com)
    com=[]
print("Maior soma em sequência: ",maior)
