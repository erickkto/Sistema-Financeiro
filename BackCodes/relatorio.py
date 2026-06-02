def gerar_resultado_final(nome_usuario, saldo_final, lista_historico):
    ## Função para salvar o desempenho financeiro do jogador em um arquivo TXT.
    ## Garante a nota na matéria de Manipulação de Arquivos.


    nome_arquivo = f"relatorio_{nome_usuario}.txt"
    

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("==================================================\n")
        arquivo.write("🎮 RELATÓRIO FINANCEIRO: SOBREVIVENDO AO ESTÁGIO\n")
        arquivo.write("==================================================\n\n")

        arquivo.write(f"👤 Estagiário: {nome_usuario}\n")
        arquivo.write(f"💰 Saldo Final Resultante: R$ {saldo_final:.2f}\n")
        

        # Regra de falência do jogo
        if saldo_final <= -2000:
            arquivo.write("🚨 STATUS: Infelizmente você faliu e não passou no estágio!\n")
        else:
            arquivo.write("🎉 STATUS: Parabéns! Você controlou a grana e virou Dev Júnior!\n")
                
                
        arquivo.write("\n📜 HISTÓRICO DE DECISÕES MÊS A MÊS:\n")
         
            
        if len(lista_historico) == 0:
            arquivo.write("- Nenhuma decisão registrada ainda.\n")
        else:
            for acao in lista_historico:
                # Corrigido o f-string e o fechamento do parêntese
                arquivo.write(f" {acao}\n")
                    
    print(f"\n💾 O arquivo '{nome_arquivo}' foi gerado na pasta do projeto!")