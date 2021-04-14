#algoritmo 1.24 CC
quantidade=int(input("Digite quantos termos deseja imprimir: "))
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))
contador=1
valor3=0
print(valor1)
print(valor2)
while contador<=quantidade:
    if contador%2==0:
        valor3=valor2-valor1
        print(valor3)
    else:
        valor3=valor1+valor2
        print(valor3)
    valor1=valor2
    valor2=valor3
    contador=contador+1