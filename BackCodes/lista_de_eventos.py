import random 


# Função que sorteia um evento aleatório baseado nos pesos definidos pelo grupo.
# Retorna o texto do evento e o impacto financeiro (dinheiro) para o saldo.
def sortear_imprevisto():
    eventos_texto = [
        "Sem imprevistos neste mes.",
        "Atencao: Voce teve gastos medicos surpresa.",
        "Aviso: Voce foi roubado e levaram sua carteira.",
        "Manutencao: Sua geladeira deu defeito e precisou de conserto.",
        "Sorte: Voce achou 200 reais perdidos na rua.",
        "Resultado: Voce ganhou em uma mini loteria local."
    ]

    eventos_valores = [
        0.0,       # Posição 0: Sem imprevistos
        -600.00,   # Posição 1: Gastos médicos
        -300.00,   # Posição 2: Roubo
        -400.00,   # Posição 3: Geladeira
        200.00,    # Posição 4: Achou dinheiro
        1500.00    # Posição 5: Loteria
    ]


    pesos_imprevistos = [60, 5, 20, 4, 10, 1]

    # Lista de índices de 0 a 5 para o random.choices sortear
    indices = [0, 1, 2, 3, 4, 5]

    # Sorteia qual POSIÇÃO (índice) vai ser escolhido com base nos pesos
    indice_sorteado = random.choices(indices, weights=pesos_imprevistos, k=1)[0]

    