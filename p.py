class Pessoa:
    def __init__ (self, nome, senha):
        self.nome = nome
        self.senha = senha
    
    def informacoes (self):
        print(f"Nickname: {self.nome}\n Senha: {self.senha}")