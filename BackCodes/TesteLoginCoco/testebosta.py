from BackCodes.TesteLoginCoco.loginbosta import cadastrar_usuario, fazer_login

while True:

    print("\n1 - Cadastro")
    print("2 - Login")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        senha = input("Senha: ")

        ok, msg = cadastrar_usuario(nome, senha)

        print(msg)

    elif opcao == "2":

        nome = input("Nome: ")
        senha = input("Senha: ")

        ok, msg, ficha = fazer_login(nome, senha)

        print(msg)

        if ok:
            print(ficha)

    elif opcao == "3":
        break