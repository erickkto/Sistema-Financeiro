# 🎮 Projeto: Sobrevivendo ao Estágio
**Componente Curricular:** Raciocínio Algorítmico (RA3)

---

## 📝 Sobre o Projeto
O **Sobrevivendo ao Estágio** é um jogo de simulação financeira desenvolvido em Python onde o jogador assume o papel de um estagiário de tecnologia. O grande objetivo é conseguir gerenciar o salário e os gastos ao longo de um ano (12 rodadas/meses) sem deixar o saldo zerar ou falir, buscando acumular capital para ser efetivado como Dev Júnior.

---

## 🛠️ Funcionalidades Principais
* **Controle de Fluxo de Caixa:** Atualização mensal de entradas e gastos fixos do estagiário.
* **Sistema de Investimentos:** Aplicação de capital em Poupança, Renda Fixa ou Alto Risco, utilizando cálculos baseados em **Matrizes (Aula 6)**.
* **Eventos Aleatórios:** Imprevistos cotidianos baseados em sorteios utilizando a biblioteca `random` **(Aula 9)**.
* **Persistência de Dados:** Exportação automática de um relatório final detalhado de desempenho em formato `.txt` **(Manipulação de Arquivos)**.

---

## 🎲 Regras do Jogo
* O jogo possui a duração total de **12 meses**.
* O jogador começa com um saldo financeiro inicial.
* A cada mês, novas escolhas financeiras e imprevistos alteram o saldo.
* **🚨 Condição de Game Over:** Se em qualquer momento o saldo do jogador for igual ou menor que **R$ -2000.00**, o estagiário vai à falência e o jogo termina.

---

## 📂 Estrutura de Arquivos do Sistema
* `projeto final.py`: Arquivo principal que inicia e executa o jogo.
* `tela_login.py` / `tela_inicio.py`: Sistema de autenticação e menus iniciais.
* `mes_a_mes.py`: Gerenciamento do loop principal e passagem dos meses.
* `decisoes.py`: Lógica matemática de rendimento dos investimentos via matrizes.
* `lista_de_eventos.py`: Armazenamento e sorteio dos imprevistos mensais.
* `relatorio.py`: Mecanismo que gera o arquivo `.txt` de desempenho.
* `p.py`: Definição de classes e objetos (como a classe `Pessoa` do jogador).

---

## 👥 Desenvolvedores (Grupo)
* Erick Kenzo Tanaka Okumoto
* Franciele de Souza Santos
* João Victor Alves Benfica
* Eduardo Araujo Steigleder
* Rafael Siqueira Furlan
* Isabela Vieira Mayer