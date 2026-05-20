def operacoes():
    opcao = int(input("Digite a operação desejada\n 1-Soma\n 2-Subtração\n 3-Multiplicação\n 4-divisao"))
    if opcao == 1:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print (f"A soma dos números {num1} e {num2} é {soma}")
    elif opcao == 2:
        num1 = int (input("Digite o primeiro numero"))
        num2 = int (input("Digite o segundo numero: "))
        sub = num1 - num2
        print (f"A subtração dos numeros {num1} e {num2} é {sub}")

operacoes()

decisao = input ("Deseja realizar outra operação?")

if decisao == "Sim":
    operacoes()
else:
    print ("Adeus!")
