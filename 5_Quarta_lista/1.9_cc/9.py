#-*-coding:utf8;-*-
	
lista=[]
j=0
serie=0
for k in range(1,101):
    lista+=[k]
for i in range(99,49,-1):
    serie=serie+(lista[j]-lista[i])**3
    j=j+1
print("serie=",serie)