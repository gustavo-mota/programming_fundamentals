#algoritmo 1.10
somaZe = 0
somaGil = 0
somaGal = 0
voto=1
while voto!=0:
    voto=int(input("digite o valor equivalente ao voto: "))
    if voto==1:
        somaZe=somaZe+1
    elif voto==2:
        somaGal=somaGal+1
    elif voto==3:
        somaGil=somaGil+1
    elif voto==0:
        print('Votação encerrada.')
    else:
        print('Voto inválido')
print("Resultado:")
print("Votos para Zé:", somaZe)
print("votos para Gal:", somaGal)
print("Votos para Gil:", somaGil)