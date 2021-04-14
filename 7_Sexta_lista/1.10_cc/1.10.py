def somatorio(numero):
    somado = 0
    sinal = False
    if numero < 0:
        numero *= -1
        sinal = True
    for i in range(1, numero+1):
        somado = somado + i
    if sinal == True:
        somado = somado * -1
    return somado


num = int(input("Digite um numero: "))
soma = somatorio(num)
print(soma)
