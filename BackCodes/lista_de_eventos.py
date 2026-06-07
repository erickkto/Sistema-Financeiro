import random

def sortear_imprevisto():
    # Função que sorteia um evento aleatório baseado nos pesos definidos pelo grupo.
    # Utiliza apenas listas sincronizadas por índices (matéria da aula).
    # Retorna o texto do evento e o impacto financeiro.
    
    # Lista apenas com os textos dos eventos (Ordem: 0 a 5)
    eventos_texto = [
        "Sem imprevistos neste mês.",
        "Atenção: Você teve gastos médicos surpresa.",
        "Aviso: Você foi roubado e levaram sua carteira.",
        "Manutenção: Sua geladeira deu defeito e precisou de conserto.",
        "Sorte: Você achou 200 reais perdidos na rua.",
        "Resultado: Você ganhou em uma mini loteria local."
    ]
    
    # Lista com os valores em dinheiro na MESMA ordem da lista de cima
    eventos_valores = [
        0.0,       # Posição 0: Sem imprevistos
        -600.00,   # Posição 1: Gastos médicos
        -300.00,   # Posição 2: Roubo
        -400.00,   # Posição 3: Geladeira
        200.00,    # Posição 4: Achou dinheiro
        1500.00    # Posição 5: Loteria
    ]
    
    # Os pesos exatos que o grupo estipulou para cada posição
    pesos_imprevistos = [60, 5, 20, 4, 10, 1]
    
    # Criamos uma lista de índices de 0 a 5 para o random.choices sortear
    indices = [0, 1, 2, 3, 4, 5]
    
    # Sorteia um índice baseado nos pesos (retorna uma lista com 1 elemento [sub 0])
    indice_sorteado = random.choices(indices, weights=pesos_imprevistos, k=1)[0]
    
    # Usa o mesmo índice sincronizado para pegar o texto e o valor
    texto = eventos_texto[indice_sorteado]
    valor = eventos_valores[indice_sorteado]
    
    return texto, valor