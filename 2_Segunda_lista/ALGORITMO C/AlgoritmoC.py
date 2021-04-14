#Algortimo item C
#Gustavo Antonio Sousa Paz E Mota
saldomedio = float(input("Digite o saldo medio do ano anterior de determinado cliente: "))
if saldomedio <= 200:
    credito = (saldomedio*0.1)
    print("Credito =", credito)
elif 200<saldomedio<=300:
    credito = (saldomedio * 0.2)
    print("Credito =", credito)
elif 300<saldomedio<=400:
    credito = (saldomedio * 0.25)
    print("Credito =", credito)
elif 400<saldomedio :
    credito = (saldomedio * 0.3)
    print("Credito =", credito)
print("Seu saldo anterior era:", saldomedio)