#algoritmo 1.38
n=1
par=0
impar=0
qpar=0
qimpar=0
parmaior=0
imparmaior=0
while n>=0:
    print("Digite um inteiro negativo para descontinuar.")
    n=int(input('Digite um valor: '))
    if n>=0:
        if n%2==0:
            if n>parmaior:
                parmaior=n
                qpar = qpar + 1
                par = par + n
            else:
                qpar=qpar+1
                par=par+n

        else:
            if n>imparmaior:
                imparmaior=n
                qimpar = qimpar + 1
                impar = impar + n
            else:
                qimpar=qimpar+1
                impar=impar+n

    else:
        mediapar=par/qpar
        mediaimpar=impar/qimpar
print("Media dos valores pares:", mediapar, "media dos impares:", mediaimpar,"maior valor par:", parmaior, 'maior valor impar:', imparmaior)

