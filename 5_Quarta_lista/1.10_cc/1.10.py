merc=[]
faturamento=0
for i in range(1,101):
    print("Digite quantas unidades da mercadoria",i,"foram vendidas:")
    var1=int(input("Digite aqui: "))
    var2=float(input("Digite o preço: "))
    merc.append([var1,var2])
    faturamento=faturamento+var1*var2
for j in range(0,100):
    print("Mercadoria",j,".Venda(s) e Preço da unidade(respectivamente):",merc[j],".")
print("Faturamento(R$):", faturamento)