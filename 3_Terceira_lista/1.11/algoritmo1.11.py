#algoritmo 1.11 CC
primeirovalor=int(input("Digite o primeiro valor: "))
segundovalor=int(input("Digite o segundo valor: "))
if primeirovalor>segundovalor:
    print("Erro. O primeiro valor deve ser menor que o segundo.")
elif primeirovalor==segundovalor:
    print("Intervalo, somatório entre eles e os valor pares é zero.")
else:
    somatório=0
    primeirovalor=primeirovalor+1
    while primeirovalor<segundovalor:
        if primeirovalor%2==0:
            print(primeirovalor)
            somatório = somatório + primeirovalor
            primeirovalor=primeirovalor+1
        else:
            primeirovalor=primeirovalor+1
    print("Esses são os valores pares no intervalo aberto definido pelos valores inseridos em ordem crescente.")
    print("E o somatório desses valores pares:", somatório)