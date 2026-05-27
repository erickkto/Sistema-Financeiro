be = float(800) ##bolsa estágio 2000-1200, já descontando aluguel, internet e miojo
sldi = float(1000) ##saldo inicial
gasto= float(0)

sldr = be + sldi - gasto

mes = int(1)

while True:
    if mes == 1:
        a = str(input("Escolha uma destas opções:\n a:"))
        mes = mes + 1
    elif mes == 2:
        print("b")
        mes = mes + 1
    elif mes == 3:
        print("c")
        mes = mes + 1
    elif mes == 4:
        print("d")
        mes = mes + 1
    elif mes == 5:
        print("e")
        mes = mes + 1
    elif mes == 6:
        print("f")
        mes = mes + 1
    elif mes == 7:
        print("g")
        mes = mes + 1
    elif mes == 8:
        print("h")
        mes = mes + 1
    elif mes == 9:
        print("i")
        mes = mes + 1
    elif mes == 10:
        print("j")
        mes = mes + 1
    elif mes == 11:
        print("k")
        mes = mes + 1
    elif mes == 12:
        print("l")
        mes = mes + 1
    else:
        print("fim")
        break