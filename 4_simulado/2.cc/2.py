#Algoritmo 2 CC
for i in  range(1000,10000):
    pd1=int(i/100)
    pd2=((i/100)-pd1)*100
    qd=(pd1+pd2)**2
    if i==qd:
        print(i)