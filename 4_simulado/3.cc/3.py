#Algoritmo 3
valor=float(input('digite o valor a ser calculado: '))
sexo= int(input("Digite o sexo: "))
idade=int(input("Digite a idade: "))
if sexo!=1 and sexo!=2:
    print("erro.")
else:
    if idade<18:
        print("Erro.")
    else:
        apITA=valor*0.04
        apBRA=valor*0.06
        if idade<30:
            ap=(30-idade)/100
            apITA=(apITA*ap)+apITA
        elif idade>50:
            ap=(idade-50)/100
            if ap>0.15:
                ap=0.15
            apITA=apITA-(apITA*ap)
        if sexo==2:
            apBRA=apBRA-(apITA*0.05)
        if idade>30:
            apBRA=apBRA-(apBRA*0.10)
        print("Seguro Bradesco:", apBRA)
        print("Seguro Itaú:", apITA)