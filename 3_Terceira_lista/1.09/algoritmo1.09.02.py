#algoritmo 1.09 CC
n=int(input("Digite quantos alunos existem na classe: "))
r=0
i=1
soma=0
while i<=n:
    nota=float(input("digite a nota: "))
    if r<nota:
        maiornota=nota
        segundamaior=r
        r=nota
        soma=soma+nota
    else:
        maiornota=r
        segundamaior=nota
        soma=soma+r
    i=i+1
media=soma/n
print("maior nota", maiornota)
print("segundamaior", segundamaior)
print('media:', media)