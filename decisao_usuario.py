import random

class Decisao:
    def __init__(self, escolha, denero):
        self.escolha = escolha
        self.denero = denero


# Funcao para proteger o jogo de erros
def obter_investimento_valido():
    while True:
        print("\n--- OPCOES DE INVESTIMENTO ---")
        print("1 - Poupanca")
        print("2 - Renda Fixa")
        print("3 - Alto Risco")
        
        opcao = input("Escolha uma opcao (1, 2 ou 3): ")
        
        # Se o jogador digitar 1, 2 ou 3, o jogo aceita e avança
        if opcao == "1" or opcao == "2" or opcao == "3":
            return opcao
        
        # Se ele digitar qualquer outra coisa, o jogo avisa e pergunta de novo
        else:
            print("Opcao invalida! Digite apenas 1, 2 ou 3.")