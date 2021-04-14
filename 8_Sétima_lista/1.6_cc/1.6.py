string = str(input("Digite: "))
string2 = string.split()
sufixos = []
string3=[]
print(string2)
for palavra in string2:
    x = len(palavra)-1
    while x>=0:
        sufixos.append(palavra[x::1])
        x -= 1
    suf = sufixos
    string3.append(suf)
    sufixos = []
print(string3)