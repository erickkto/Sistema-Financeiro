import random


class Jogo:

    def __init__(self):

        self.beneficio = 800
        self.saldo = 1800
        self.mes_atual = 0

        self.meses = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril"
        ]

        self.opcoes_atuais = {}

        self.gerar_opcoes_mes()

    def evento_random(self, opcoes, pesos=None):

        if pesos:
            return random.choices(opcoes, weights=pesos, k=1)[0]

        return random.choice(opcoes)

    def gerar_opcoes_mes(self):

        if self.mes_atual == 0:

            aposta = self.evento_random([800, -800])

            self.opcoes_atuais = {
                "a": ("Cafeteira (-400)", -400),
                "b": ("Festival (-750)", -750),
                "c": (f"Aposta ({aposta:+})", aposta),
                "d": ("Nada", 0)
            }

        elif self.mes_atual == 1:

            cripto = self.evento_random([500, -500])

            self.opcoes_atuais = {
                "a": ("Celular (-1200)", -1200),
                "b": ("Roupas (-300)", -300),
                "c": ("Viagem (-600)", -600),
                "d": (f"Cripto ({cripto:+})", cripto)
            }

        elif self.mes_atual == 2:

            rendimento = int(self.saldo * 0.05)
            amigo = self.evento_random([200, -300])

            self.opcoes_atuais = {
                "a": (f"Renda fixa (+{rendimento})", rendimento),
                "b": ("Videogame (-2000)", -2000),
                "c": (f"Amigo ({amigo:+})", amigo),
                "d": ("Nada", 0)
            }

        elif self.mes_atual == 3:

            aposta = self.evento_random([800, -400], [40, 60])

            self.opcoes_atuais = {
                "a": ("Curso (+150)", 150),
                "b": ("Cachorro (-500)", -500),
                "c": (f"Aposta ({aposta:+})", aposta),
                "d": ("Vendas (+350)", 350)
            }

        else:
            self.opcoes_atuais = {}

    def escolher(self, opcao):

        if self.acabou():
            return False, "Jogo encerrado"

        if opcao not in self.opcoes_atuais:
            return False, "Opção inválida"

        efeito = self.opcoes_atuais[opcao][1]

        self.saldo += efeito

        self.mes_atual += 1

        if not self.acabou():

            # Recebe benefício do próximo mês
            self.saldo += self.beneficio

            self.gerar_opcoes_mes()

        return True, f"Efeito aplicado: {efeito:+}"

    def acabou(self):
        return self.mes_atual >= len(self.meses)

    def nome_mes(self):

        if self.acabou():
            return "Fim de jogo"

        return self.meses[self.mes_atual]