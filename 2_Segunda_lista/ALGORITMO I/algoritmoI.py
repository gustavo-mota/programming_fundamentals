#Algoritmo item I
print("Calcular raizes de equacoes de segundo grau")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
delta = b**2-4*a*c
delta = delta**1/2
raiz2 = (b-delta)/2*a
raiz1 = (b+delta)/2*a
print("As raizes sao:", raiz1, raiz2)
