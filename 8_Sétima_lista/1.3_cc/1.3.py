string = str(input("Digite a palavra com todas minusculas ou todas maiusculas: "))
string2 = str(input("Digite a palavra com todas minusculas ou todas maiusculas: "))
if len(string) != len(string2):
    print("Não são.")
else:
    anagrama = True
    vetor =[]
    vetor2 = []
    for i in string:
        vetor.append(ord(i))
    for n in string2:
        vetor2.append(ord(n))
    vetor.sort()
    vetor2.sort()
    for s in range(0,len(vetor)):
        if vetor[s] != vetor2[s]:
            anagrama = False
    if anagrama == True:
        print("São anaggramas.")
    else:
        print("Não são.")