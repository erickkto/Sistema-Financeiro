be = float(800) ##bolsa estágio 2000-1200, já descontando aluguel, internet e miojo
sldi = float(1000) ##saldo inicial
gasto = float(0)

sldr = be + sldi - gasto ##Saldo resultante

mes = int(1)

while True:            
    if mes == 1:
        print("Janeiro")
        a = str(input("Escolha uma destas opções:\n a:Gastar 400RS com uma cafeteira\n b:Gastar 750RS em um festival de música\n c:Arriscar 800RS no agiota seguro(pode dobrar ou sumir com o dinheiro)\n d:Não gastar nada\n Resposta: ")).lower() ##a: chance de bônus no futuro, b:traz prejuízo com ressaca depois
        aa = 400
        ba = 750
        ca = 800
        da = 0
        if a == 'a':
            sldr = sldr - aa
            print(sldr)
        elif a == 'b':
            sldr = sldr - ba
            print(sldr)
        elif a == 'c':
            sldr = sldr - ca
            print(sldr)
        elif a == 'd':
            sldr = sldr - da
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 2:
        sldr = sldr + 800
        print("Fevereiro")
        ab = 1200
        bb = 300
        cb = 600
        db = 500
        b = str(input("Escolha uma destas opções:\n a:Comprar celular novo de 1200RS\n b:Comprar 300RS em roupas\n c:Fazer uma viagem de 600RS\n d:Investir 500RS em criptomoedas\n Resposta: ")).lower() ##d: 50% de chance de dobrar
        if b == 'a':
            sldr = sldr - ab
            print(sldr)
        elif b == 'b':
            sldr = sldr - bb
            print(sldr)
        elif b == 'c':
            sldr = sldr - cb
            print(sldr)
        elif b == 'd':
            sldr = sldr - db
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 3:
        sldr = sldr + 800
        print("Março")
        ac = 0.05
        bc = 2000
        cc = 200
        dc = 0
        c = str(input(f"Escolha uma destas opções:\n a:Aplicar {sldr}RS em renda fixa\n b:Comprar um vídeo game de 2000RS\n c:Emprestar 200RS para um amigo\n d:Não gastar nada\n Resposta: ")).lower() ##a: +5% no saldo, c: 50% de chance de +200RS ou -300RS
        if c == 'a':
            sldr = sldr + (sldr * ac)
            print(sldr)
        elif c == 'b':
            sldr = sldr - bc
            print(sldr)
        elif c == 'c':
            sldr = sldr - cc
            print(sldr)
        elif c == 'd':
            sldr = sldr - dc
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 4:
        sldr = sldr + 800
        print("Abril")
        ad = 250
        bd = 500
        cd = 400
        dd = 350
        d = str(input("Escolha uma destas opções:\n a:Comprar um curso de 250RS\n b:Comprar um cachorro de 500RS\n c:Apostar 400RS e um campeonato de futebol\n d:Vender 350RS de coisas usadas\n Resposta: ")).lower() ## a: +400RS, c: 40% de chance de ganhar 800RS e 60% de perder 400RS
        if d == 'a':
            sldr = sldr - ad
            print(sldr)
        elif d == 'b':
            sldr = sldr - bd
            print(sldr)
        elif d == 'c':
            sldr = sldr - cd
            print(sldr)
        elif d == 'd':
            sldr = sldr + dd
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 5:
        sldr = sldr + 800
        print("Maio")
        ae = 1500
        be = 450
        ce = 600
        de = 150
        e = str(input("Escolha uma destas opções:\n a:Dar um upgrade de 1500RS no computador\n b:Fazer um churrasco para os amigos de 450RS\n c:Trabalhar como freelancer e ganhar 600RS\n d:Comprar um curso de investimentos por 150RS\n Resposta:")).lower() ##d: começa a ganhar 150RS todos os meses
        if e == 'a':
            sldr = sldr - ae
            print(sldr)
        elif e == 'b':
            sldr = sldr - be
            print(sldr)
        elif e == 'c':
            sldr = sldr + ce
            print(sldr)
        elif e == 'd':
            sldr = sldr - de
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 6:
        sldr = sldr + 800
        print("Junho")
        af = 500
        bf = 500
        cf = 800
        df = 0
        f = str(input("Escolha uma destas opções:\n a:Fazer uma tatuagem de 500RS\n b:Comprar 500RS em ações\n c:Comprar um drone de 800RS\n d:Não gastar nada\n Resposta: ")).lower() ##b:-10% a 15% do valor investido
        if f == 'a':
            sldr = sldr - af
            print(sldr)
        elif f == 'b':
            sldr = sldr - bf
            print(sldr)
        elif f == 'c':
            sldr = sldr - cf
            print(sldr)
        elif f == 'd':
            sldr = sldr - df
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 7:
        sldr = sldr + 800
        print("Julho")
        ag = 900
        bg = 750
        cg = 1100
        dg = 500
        g = str(input("Escolha uma destas opções:\n a:Comprar ingresso para um show internacional de 900RS\n b:Revender produtos pela internet e ganhar 750RS\n c:Fazer uma viagem com amigos por 1100RS\n d:Vender o celular antigo por 500RS\n Resposta: ")).lower()
        if g == 'a':
            sldr = sldr - ag
            print(sldr)
        elif g == 'b':
            sldr = sldr + bg
            print(sldr)
        elif g == 'c':
            sldr = sldr - 1100
            print(sldr)
        elif g == 'd':
            sldr = sldr + dg
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 8:
        sldr = sldr + 800
        print("Agosto")
        ah = 100
        bh = 700
        ch = 1500
        dh = 0
        h = str(input("Escolha uma destas opções:\n a:Participar de um torneio de videogame por 100RS\n b:Comprar uma bicicleta por 700RS\n c:Montar um setup gamer por 1500RS\n d:Economizar\n Resposta: ")).lower() ##a: chance de 50% de ganhar 800RS
        if h == 'a':
            sldr = sldr - ah
            print(sldr)
        elif h == 'b':
            sldr = sldr - bh
            print(sldr)
        elif h == 'c':
            sldr = sldr - ch
            print(sldr)
        elif h == 'd':
            sldr = sldr - 0
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 9:
        sldr = sldr + 800
        print("Setembro")
        ai = 250
        bi = 400
        ci = 200
        di = 800
        i = str(input("Escolha uma destas opções:\n a:Trabalhar como entregador no fim de semana e ganhar 250RS\n b:Comprar um curso de programação por 400RS\n c:Participar de um sorteio de um notebook por 200RS\n d:Fazer uma reforma no quarto por 800RS\n Resposta: ")).lower() ##c: chance de 5% de ganhar um notebook de 4500
        if i == 'a':
            sldr = sldr + ai
            print(sldr)
        elif i == 'b':
            sldr = sldr - bi
            print(sldr)
        elif i == 'c':
            sldr = sldr - ci
            print(sldr)
        elif i == 'd':
            sldr = sldr - di
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 10:
        sldr = sldr + 800
        print("Outubro")
        aj = 300
        bj = 150
        cj = 120
        dj = 1000
        j = str(input("Escolha uma destas opções:\n a:Comprar uma caixa de itens colecionáveis por 300RS\n b:Cortar a grama do vizinho por 150RS\n c:Assinar vários serviços de streaming por 120RS\n d:Comprar uma impressora 3d por 1000RS\n Resposta: ")).lower() ##a: 50% de chance de +500RS
        if j == 'a':
            sldr = sldr - aj
            print(sldr)
        elif j == 'b':
            sldr = sldr + bj
            print(sldr)
        elif j == 'c':
            sldr = sldr - cj
            print(sldr)
        elif j == 'd':
            sldr = sldr - dj
            print(sldr)
        else:
            print("liso")
        mes = mes + 1
    elif mes == 11:
        sldr = sldr + 800
        print("Novembro")
        mes = mes + 1
    elif mes == 12:
        sldr = sldr + 800
        print("Dezembro")
        mes = mes + 1
    else:
        print("fim")
        break