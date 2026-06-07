import random

def sortear_imprevisto():
    # Funcao que sorteia um evento aleatorio baseado nos pesos definidos pelo grupo.
    # Utiliza apenas listas sincronizadas por indices (materia da aula).
    # Retorna o texto do evento e o impacto financeiro.
    
    # Lista apenas com os textos dos eventos (Ordem: 0 a 5)
    eventos_texto = [
        "Sem imprevistos neste mes.",
        "Atencao: Voce teve gastos medicos surpresa.",
        "Aviso: Voce foi roubado e levaram sua carteira.",
        "Manutencao: Sua geladeira deu defeito e precisou de conserto.",
        "Sorte: Voce achou 200 reais perdidos na rua.",
        "Resultado: Voce ganhou em uma mini loteria local."
    ]
    
    # Lista com os valores em dinheiro na MESMA ordem da lista de cima
    eventos_valores = [
        0.0,       # Posicao 0: Sem imprevistos
        -600.00,   # Posicao 1: Gastos medicos
        -300.00,   # Posicao 2: Roubo
        -400.00,   # Posicao 3: Geladeira
        200.00,    # Posicao 4: Achou dinheiro
        1500.00    # Posicao 5: Loteria
    ]
    
    # Os pesos exatos que o grupo estipulou para cada posicao
    pesos_imprevistos = [60, 5, 20, 4, 10, 1]
    
    # Criamos uma lista de indices de 0 a 5 para o random.choices sortear
    indices = [0, 1, 2, 3, 4, 5]
    
    # Sorteia uma posicao (de 0 a 5) usando os pesos. O [0] serve para extrair o numero de dentro da lista gerada pelo choices.
    indice_sorteado = random.choices(indices, weights=pesos_imprevistos, k=1)[0]
    
    # Puxa o texto e o valor usando o mesmo indice sorteado
    texto = eventos_texto[indice_sorteado]
    valor = eventos_valores[indice_sorteado]
    
    return texto, valor