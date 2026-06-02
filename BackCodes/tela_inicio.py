import tkinter as tk
from p import Pessoa
from tela_login import login
from fichas import criar_ficha

janela = tk.Tk()
# ---------------- FICHA (NOVA TELA) ----------------

def abrir_ficha(fichas):

    tela_ficha = tk.Toplevel(janela)
    tela_ficha.title("Ficha do Jogador")
    tela_ficha.geometry("800x600")
    tela_ficha.configure(bg="black")

    introducao = """
====================================================

Olá, Jogador! Seja bem vindo ao seu jogo de gerenciamento financeiro.
Vamos ver se com sua habilidades de gestão monetária,
Você conseguirá se virar nesse mundo em 1 ano!
Você começa com um saldo inicial de 1.800 reais,
Ao fim dos 12 meses, 
O saldo final deve ser acima do saldo inicial para obter vitoria
====================================================
"""

    tk.Label(
            tela_ficha,
            text=introducao,
            bg="black",
            fg="lime",
            font=("Courier", 10),
            justify="left"
        ).pack(pady=10)

    tk.Label(
            tela_ficha,
            text=f"Jogador: {fichas['nome']}",
            bg="black",
            fg="white",
            font=("Arial", 14)
        ).pack(pady=5)

    tk.Label(
            tela_ficha,
            text=f"Saldo: R$ {fichas['saldo']:.2f}",
            bg="black",
            fg="gold",
            font=("Arial", 14)
        ).pack(pady=5)

    tk.Label(
            tela_ficha,
            text=f"Inventário: {fichas['inventario']}",
            bg="black",
            fg="cyan"
        ).pack(pady=5)

    tk.Label(
            tela_ficha,
            text=f"Histórico:\n" + "\n".join(fichas["historico"]),
            bg="black",
            fg="white",
            justify="left"
        ).pack(pady=5)



