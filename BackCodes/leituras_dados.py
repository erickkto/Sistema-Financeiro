import os

def carregar_regras():
    ## Função para ler as regras do jogo a partir de um arquivo TXT externo.
    ## Demonstra a matéria de LEITURA de arquivos ('r').
    nome_arquivo = "regras.txt"

    #Se o arquivo estiver na pasta ⬇️
    if os.path.exists(nome_arquivo):
        # Abre o arquivo no modo de leitura ('r' de read) com encoding correto
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("\n📜 REGRAS DO JOGO")
            print(conteudo)

    else:
        print(f"\n⚠️ O arquivo '{nome_arquivo}' não foi encontrado. Pulando leitura.")