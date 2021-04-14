ang=float(input("Digite um angulo: "))
soma=False
cos=1
cont=1
ang=ang/(180/3.14)
def fatorial(num):
	nfat=1
	while num>1:
		nfat=nfat*num
		num=num-1
	return nfat
while cont<=14:
	if soma==True:
		cos+=(ang**(cont*2))/fatorial(cont*2)
		soma=False
	else:
		cos-=(ang**(cont*2))/fatorial(cont*2)
		soma=True
	cont=cont+1
print(cos)
