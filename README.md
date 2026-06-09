# Sobrevivendo ao Estágio

Projeto desenvolvido para a disciplina de Raciocínio Algorítmico (RA3). Este software consiste em um simulador de gestão financeira pessoal que utiliza o ciclo de vida de um estagiário de tecnologia como cenário principal.

## Descrição
O objetivo é gerenciar as finanças ao longo de 12 meses de estágio, equilibrando renda, custos fixos e investimentos. O desafio é acumular capital suficiente para a efetivação no cargo de Desenvolvedor Júnior, enquanto se evita a falência financeira.

## Arquitetura do Sistema
O sistema foi estruturado de forma modular para garantir organização e facilidade na manutenção do código:

* **Ponto de Entrada:** `projeto_final.py` (Script de inicialização).
* **Interface:** Interface gráfica desenvolvida com `tkinter` para interação do usuário (`mes_a_mes_com_interface.py`).
* **Núcleo (BackCodes):**
    * `decisoes.py`: Engine de cálculos de investimentos baseada em estruturas matriciais.
    * `lista_de_eventos.py`: Gerenciador de eventos aleatórios e probabilidade.
    * `relatorio.py`: Módulo de exportação de dados para persistência em arquivo.
    * `p.py`: Definição dos objetos de negócio (POO).
    * `tela_login.py` e `tela_inicio.py`: Módulos de controle de fluxo de tela.
* **Documentação:** `regras.txt` (Arquivo de diretrizes do simulador).

## Tecnologias e Conceitos Aplicados
* **Python 3.x:** Linguagem principal do projeto.
* **Tkinter:** Framework para interface gráfica.
* **POO (Programação Orientada a Objetos):** Utilizada na estruturação dos dados do usuário.
* **Estruturas de Dados:** Implementação de matrizes para o sistema de juros e listas sincronizadas para eventos.
* **Persistência de Dados:** Manipulação de arquivos de texto para registro de histórico.

## Condições de Jogo
* **Duração:** 12 meses (rodadas).
* **Objetivo:** Manter a saúde financeira até o final do período de estágio.

## Equipe
* Eduardo Araujo Steigleder
* Erick Kenzo Tanaka Okumoto
* Franciele de Souza Santos
* Isabela Vieira Mayer
* João Victor Alves Benfica
* Rafael Siqueira Furlan
