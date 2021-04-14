data=str(input("Digite a data entre barras '/' senão vai dar erro e não vai ter jeito: "))
datas = data.split("/")
data1 = datas[0]
data2 = datas[1]
if int(data2)>=13:
    if int(data2)<=31 and int(data1)<=12:
        print("Data válida. Calendário Americano")
    else:
        print("Data inválida.")
else:
    if int(data2)<=12 and int(data1)<=31:
        print("Data válida, calendário Brasileiro")
    else:
        print("inválido")