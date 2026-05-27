be = float(800) ##bolsa estágio 2000-1200, já descontando aluguel, internet e miojo
sldi = float(1000) ##saldo inicial
gasto = float(0)

sldr = be + sldi - gasto ##Saldo resultante

mes = int(1)

while True:
    if mes == 1:
        print("Janeiro")
        a = str(input("Escolha uma destas opções:\n a:Gastar 400RS com uma cafeteira\n b:Gastar 750RS em um festival de música\n c:Arriscar 800RS no agiota seguro(pode dobrar ou sumir com o dinheiro)\n d:Não gastar nada\n resposta: ")).lower() ##a: chance de bônus no futuro, b:traz prejuízo com ressaca depois
        ag = 400
        bg = 750
        cg = 800
        dg = 0
        if a == 'a':
            sldr = sldr - ag
            print(sldr)
        elif a == 'b':
            sldr = sldr - bg
            print(sldr)
        elif a == 'c':
            sldr = sldr - cg
            print(sldr)
        elif a == 'd':
            sldr = sldr - dg
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 2:
        print("Fevereiro")
        mes = mes + 1
    elif mes == 3:
        print("Março")
        mes = mes + 1
    elif mes == 4:
        print("Abril")
        mes = mes + 1
    elif mes == 5:
        print("Maio")
        mes = mes + 1
    elif mes == 6:
        print("Junho")
        mes = mes + 1
    elif mes == 7:
        print("Julho")
        mes = mes + 1
    elif mes == 8:
        print("Agosto")
        mes = mes + 1
    elif mes == 9:
        print("Setembro")
        mes = mes + 1
    elif mes == 10:
        print("Outubro")
        mes = mes + 1
    elif mes == 11:
        print("Novembro")
        mes = mes + 1
    elif mes == 12:
        print("Dezembro")
        mes = mes + 1
    else:
        print("fim")
        break