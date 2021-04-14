milhar = [" ","mil","dois mil","três mil","quatro mil","cinco mil","seis mil","sete mil","oito mil","nove mil"]
centena = [" ","cento","duzentos","trezentos","quatrocentos","quinehntos","seiscentos","setecentos","oitocentos","novecentos"]
dezena = [" ","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"]
dezena_especial = ["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessette","dezoito","dezenove"]
unidade = [" ","um","dois","três","quatro","cinco","seis","sete","oito","nove"]
ano = str(input("digite o ano: "))
if len(ano)!=4:
    print("Erro.")
elif int(ano)<=0:
    print("Inválido.")
else:
    m = int(ano[0])
    c = int(ano[1])
    d = int(ano[2])-1
    u = int(ano[3])
    extenso = []
    extenso.append(milhar[m])
    if c!=0:
        extenso.append(centena[c])
    extenso.append("e")
    if d>1:
        extenso.append(dezena[d])
        if u!=0:
            extenso.append("e")
            extenso.append(unidade[u])
    elif int(ano[2])==1:
        if u!=0:
            extenso.append(dezena_especial[u])
        else:
            extenso.append("dez")
    print(extenso)