ang=float(input("Digite um angulo: "))
soma=False
sen=1
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
		sen+=(ang**(cont))/fatorial(cont)
		soma=False
	else:
		sen-=(ang**(cont))/fatorial(cont)
		soma=True
	cont=cont+1
print(sen)