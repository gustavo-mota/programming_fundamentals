string = str(input("Digite(desculpa, acentuação será levada em consideração): "))
string2 = string.split()
prefixos = []
x=1
print(string2)
for palavra_separada in string2:
    for letra in palavra_separada:
        prefixos.append(palavra_separada[0:x])
        x += 1
    x=1
    pre = prefixos
    print(pre)
    prefixos=[]