from p import Pessoa

usuario = []

def cadastro():
    print ("===Cadastro===\n ")

    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    for p in usuario:
        if p.nome == nome:
            print("Nome ja cadastrado!")
            return
        
    novo_usuario =  Pessoa (nome, senha)
    usuario.append(novo_usuario)

    print("Usuario cadastrado com sucesso!")

def login():
    print ("===Login===\n ")
    nome = input ("Digite seu nome: ")
    senha = input ("Digite sua senha: ")

    for p in usuario:
        if p.nome == nome and p.verificar_senha(senha):
            print(f"Seja bem vindo, {nome}!")

            return
        
    print ("Nome ou senha errado!")
    return
    
print("\n1 - Cadastrar")
print("2 - Login")
print("3 - Sair")



while True:
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastro()

    elif opcao == "2":
        login()

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")