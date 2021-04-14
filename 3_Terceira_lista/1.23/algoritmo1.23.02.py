#algoritmo 1.23 CC
n=int(input("Digite quantos termos deseja: "))
valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))
print(valor1)
print(valor2)
contador=1
while contador<=n:
    valor3=valor1+valor2
    print(valor3)
    valor1=valor2
    valor2=valor3
    contador=contador+1