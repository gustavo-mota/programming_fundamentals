import random
captcha = []
cap_sol = []
cap_re = []
x = 0
while x<=1:
    captcha.append(random.randint(65,90))
    captcha.append(random.randint(97,122))
    captcha.append(random.randint(48,57))
    x += 1
captcha = sorted(captcha)
for i in range(0,len(captcha)):
    cap_sol.append(captcha[i])
cap_sol[2] = cap_sol[2]+32
cap_sol[3]= cap_sol[3]+32
#embaralha e cria a solução
random.shuffle(captcha)
#printa e pega resposta, criando vetor para comparar depois:
for element in captcha:
    print(chr(element),end="")
print(" ")
resposta = input("Digite os caracteres acima: ")
if len(resposta)!=len(captcha):
    print("Errou.")
else:
    captcha = sorted(captcha)
for caractere in resposta:
    cap_re.append(ord(caractere))
cap_re = sorted(cap_re)
cap_sol = sorted(cap_sol)
#padroniza o ascii dos caracteres para minuscula
for y in range(0,len(cap_re)):
    if cap_re[y]>=65 and cap_re[y]<=90:
        cap_re[y] = cap_re[y] + 32
#veirifca igualdade
acerto = True
for indice in range(0,len(cap_re)):
    if cap_re[indice]!=cap_sol[indice]:
        acerto =False
if acerto == True:
    print("Acertou.")
else:
    print("Errou.")