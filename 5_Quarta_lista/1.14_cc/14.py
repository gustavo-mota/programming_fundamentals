#-*-coding:utf8;-*-
	
vetor_altura=[]
vetor_nome=[]
vetor_sexo=[]
for i in range(0,3):
    n=str(input("Coloque o nome:"))
    vetor_nome.append(n)
    a=float(input("Coloque a altura:"))
    vetor_altura.append(a)
    s=int(input("Coloque 1 para masculino e 2 para feminino:"))
    vetor_sexo.append(s)
for i in range(0,3):
    for j in range(0,3):
        if vetor_altura[i]<vetor_altura[j]:
            a=vetor_altura[i]
            n=vetor_nome[i]
            s=vetor_sexo
            vetor_altura[i]=vetor_altura[j]
            vetor_nome[i]=vetor_nome[j]
            vetor_sexo[i]=vetor_sexo[j]
            vetor_altura[j]=a
            vetor_nome[j]=n
            vetor_sexo[j]=s
print("\n\n")
for i in range(0,3):
    print(vetor_nome[i],"possui",vetor_altura[i],"de altura")

