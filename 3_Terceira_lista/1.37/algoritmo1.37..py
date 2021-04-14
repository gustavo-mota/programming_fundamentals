#algoritmo 1.37 CC
somaltura=0
saf=0
j=1
maior=0
menor=2
fem=0
total=0
while j<=50:
    codigo=int(input("digite o código: "))
    if codigo!=1 and codigo!=2:
        print("Código inválido.")
    else:
        altura=float(input("Digite a altura: "))
        if codigo==1:
            somaltura=somaltura+altura
            total=total+1
            if altura>maior:
                maior=altura
            if altura<menor:
                menor=altura
        else:
            somaltura=somaltura+altura
            saf=saf+altura
            fem=fem+1
            total=total+1
            if altura>maior:
                maior=altura
            if altura<menor:
                menor=altura
    j=j+1
mediafem=saf/fem
media=somaltura/total
print("Media de alturas:", media)
print("Média de alturas femininas:", mediafem)
print("Maior altura:", maior)
print("Menor altura:", menor)