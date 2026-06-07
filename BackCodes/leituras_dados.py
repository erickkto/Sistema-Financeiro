import os

def carregar_regras():
    ## Função para ler as regras do jogo a partir de um arquivo TXT externo.
    ## Demonstra a matéria de LEITURA de arquivos ('r').
    
    # 1. Descobre o caminho da pasta onde este arquivo de código está salvo
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Cria o caminho padrão assumindo que o regras.txt está na mesma pasta do código
    caminho_regras = os.path.join(pasta_atual, "regras.txt")
    
    # 3. Se não achar na mesma pasta (ex: o código está em 'BackCodes' e o arquivo na raiz),
    # ele tenta buscar o arquivo na pasta de cima (usando "..")
    if not os.path.exists(caminho_regras):
        caminho_regras = os.path.join(pasta_atual, "..", "regras.txt")

    # Agora faz a leitura usando o caminho dinâmico que sempre funciona!
    if os.path.exists(caminho_regras):
        with open(caminho_regras, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            print("\nREGRAS DO JOGO")
            print(conteudo)
    else:
        print(f"\n⚠️ O arquivo 'regras.txt' não foi encontrado em nenhum dos caminhos. Pulando leitura.")