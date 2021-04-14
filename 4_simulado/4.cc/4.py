#Algoritmo 4 CC
triangulo=False
i=1
num=int(input("Digite o valor: "))
if num<=5:
    print("Não.")
else:
    while i<num:
        ap=i*(i+1)*(i+2)
        if ap==num:
            triangulo=True
        i=i+1
    if triangulo==False:
        print("Não.")
    elif triangulo==True:
        print("Sim.")