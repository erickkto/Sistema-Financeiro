import random

# =========================================================================
# MATRIZ
# Cada linha representa um investimento, e as colunas são os juros possíveis.
# Linha 0: Poupança (Rendimento fixo/seguro)
# Linha 1: Renda Fixa (Rendimento moderado)
# Linha 2: Alto Risco / Apostas (Ou perde tudo, ou dobra)
# =========================================================================

matriz_juros = [
    [0.01, 0.02], #Linha 0
    [0.03, 0.05], #Linha 1
    [-1.00, 1.00] #Linha 2
]

def calcular_investimento(opcao_escolhida, valor_investido):
    # Função isolada para processar os rendimentos do saldo.
    # Retorna o valor do prejuízo.

    if opcao_escolhida == "1": # Poupança
        taxa = random.choice([matriz_juros[0][0], matriz_juros[0][1]])
        rendimento = valor_investido * taxa
        print(f"📊 Poupança rendeu {taxa * 100:.1f}%! Retorno +R$ {rendimento:.2f}")
        return rendimento
    
    elif opcao_escolhida == "2":
        taxa = random.choice([matriz_juros[1][0], matriz_juros[1][1]])
        rendimento = valor_investido * taxa
        print(f"Renda Fixa rendeu {taxa * 100:.1f}%! Retorno +R$ {rendimento:.2f}")
        return rendimento

    elif opcao_escolhida == "3": # Alto risco
        # Criando taxa e o rendimento específicos para a opção 3
        # Sorteia uando a Linha 2 da matriz (perde tudo -1.00 ou dobra 1.00)
        taxa = random.choice([matriz_juros[2][0], matriz_juros[2][1]])
        rendimento = valor_investido * taxa

        if taxa < 0:
            print(f"🚨 Deu ruim! O investimento de risco falhou. Prejuízo: -R$ {abs(rendimento):.2f}")
        else:
            print(f"💰 Sorte grande! O investimento dobrou! Retorno: +R$ {rendimento:.2f}")
            
        return rendimento
        
    return 0.0