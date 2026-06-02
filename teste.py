import random

be = 800
sldr = 1800


meses = [
    "Janeiro", "Fevereiro", "Março", "Abril",
    "Maio", "Junho", "Julho", "Agosto",
    "Setembro", "Outubro", "Novembro", "Dezembro"
]


def evento_random(opcoes, pesos=None):
    """Sorteia evento com ou sem peso"""
    if pesos:
        return random.choices(opcoes, weights=pesos, k=1)[0]
    return random.choice(opcoes)


# ---------------- DECISÕES ----------------

def get_decisoes(mes, saldo):

    if mes == 0:  # Janeiro
        return {
            "a": ("Cafeteira (400)", -400),
            "b": ("Festival (750)", -750),
            "c": ("Agiota (ganha ou perde 800)", evento_random([800, -800])),
            "d": ("Nada", 0)
        }

    if mes == 1:  # Fevereiro
        return {
            "a": ("Celular (1200)", -1200),
            "b": ("Roupas (300)", -300),
            "c": ("Viagem (600)", -600),
            "d": ("Cripto (±500)", evento_random([500, -500]))
        }

    if mes == 2:  # Março
        return {
            "a": ("Renda fixa +5%", int(saldo * 0.05)),
            "b": ("Videogame (2000)", -2000),
            "c": ("Amigo (200 ou -300)", evento_random([200, -300])),
            "d": ("Nada", 0)
        }

    if mes == 3:  # Abril
        return {
            "a": ("Curso (+150)", 150),
            "b": ("Cachorro (500)", -500),
            "c": ("Aposta (±800)", evento_random([800, -400], [40, 60])),
            "d": ("Vendas (+350)", 350)
        }

    if mes == 4:  # Maio
        return {
            "a": ("PC upgrade (1500)", -1500),
            "b": ("Churrasco (450)", -450),
            "c": ("Freela (+600)", 600),
            "d": ("Curso (-150)", -150)
        }

    # -------- meses finais simplificados --------

    base = {
        "a": ("Opção A", random.randint(-800, 800)),
        "b": ("Opção B", random.randint(-500, 500)),
        "c": ("Opção C", random.randint(-1000, 1000)),
        "d": ("Nada", 0)
    }

    return base


# ---------------- LOOP DO JOGO (TERMINAL) ----------------

def jogar_terminal():
    global sldr

    for i, mes in enumerate(meses):

        print(f"\n=== {mes} ===")
        sldr += be

        print("Saldo:", sldr)

        opcoes = get_decisoes(i, sldr)

        for k, v in opcoes.items():
            print(f"{k}: {v[0]}")

        escolha = input("Escolha: ").lower()

        if escolha in opcoes:
            sldr += opcoes[escolha][1]

        print("Novo saldo:", sldr)


print(jogar_terminal())
# ---------------- FUNÇÃO PARA TKINTER ----------------

def jogar_uma_fase(mes, saldo, escolha):

    opcoes = get_decisoes(mes, saldo)

    if escolha not in opcoes:
        return saldo, "Escolha inválida"

    efeito = opcoes[escolha][1]

    saldo += efeito

    return saldo, f"Saldo atualizado: {saldo}"