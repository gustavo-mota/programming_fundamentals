#algoritimo item i
anoatual = int(input("Digite o ano atual: "))
anonascimento = int(input("Digite o ano de nasciemnto: "))
idade = anoatual-anonascimento
idademeses = idade*12
x = (idade/4)+1 #numero de anos bissextos
idadedias = idade*365+x #cada ano bissexto acrescenta um dia
y = x/7 #semanas usando os dias bissextos
idadesemanas = idade*52+y
print("A idade em anos, meses, dias e semanas respectivamente: ", idade,",", idademeses,",", idadedias,",",idadesemanas)