import tkinter as tk
janela = tk.Tk()
from mes_a_mes_com_interface import iniciar_jogo

def abrir_ficha(fichas):

    tela_ficha = tk.Toplevel(janela)
    tela_ficha.title("Ficha do Jogador")
    tela_ficha.geometry("850x650")
    tela_ficha.resizable(False, False)
    tela_ficha.configure(bg="#1a1a1a")

    # ==========================
    # TÍTULO
    # ==========================

    tk.Label(
        tela_ficha,
        text="📋 FICHA DO JOGADOR",
        bg="#1a1a1a",
        fg="#00e676",
        font=("Courier", 20, "bold")
    ).pack(pady=(20, 10))

    tk.Frame(
        tela_ficha,
        bg="#333333",
        height=2
    ).pack(fill="x", padx=30)

    # ==========================
    # INTRODUÇÃO
    # ==========================

    introducao = """
Bem-vindo ao Sobrevivendo ao Mês!

Você inicia sua jornada com R$ 1.800,00.

Durante 12 meses, precisará tomar decisões financeiras,
investir com sabedoria e evitar gastos desnecessários.

Ao final do período, seu saldo deverá ser superior ao
saldo inicial para alcançar a vitória.

Boa sorte!
"""

    tk.Label(
        tela_ficha,
        text=introducao,
        bg="#1a1a1a",
        fg="#aaaaaa",
        font=("Courier", 10),
        justify="left"
    ).pack(padx=30, pady=20)

    # ==========================
    # DADOS DO JOGADOR
    # ==========================

    frame_info = tk.Frame(
        tela_ficha,
        bg="#2a2a2a"
    )
    frame_info.pack(fill="x", padx=30, pady=10)

    tk.Label(
        frame_info,
        text=f"👤 Jogador: {fichas['nome']}",
        bg="#2a2a2a",
        fg="#f0f0f0",
        font=("Courier", 12, "bold")
    ).pack(anchor="w", padx=15, pady=10)

    tk.Label(
        frame_info,
        text=f"💰 Saldo Inicial: R$ {fichas['saldo']:.2f}",
        bg="#2a2a2a",
        fg="#ffd600",
        font=("Courier", 12)
    ).pack(anchor="w", padx=15, pady=5)

    inventario = (
        ", ".join(fichas["inventario"])
        if fichas["inventario"]
        else "Nenhum item"
    )

    tk.Label(
        frame_info,
        text=f"🎒 Inventário: {inventario}",
        bg="#2a2a2a",
        fg="#00bcd4",
        font=("Courier", 11)
    ).pack(anchor="w", padx=15, pady=(5, 10))

    # ==========================
    # HISTÓRICO
    # ==========================

    tk.Label(
        tela_ficha,
        text="📜 Histórico",
        bg="#1a1a1a",
        fg="#f0f0f0",
        font=("Courier", 13, "bold")
    ).pack(anchor="w", padx=30, pady=(20, 5))

    historico_frame = tk.Frame(
        tela_ficha,
        bg="#2a2a2a"
    )
    historico_frame.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=(0, 20)
    )

    if fichas["historico"]:

        for item in fichas["historico"]:

            tk.Label(
                historico_frame,
                text=f"• {item}",
                bg="#2a2a2a",
                fg="#cccccc",
                font=("Courier", 10),
                anchor="w",
                justify="left"
            ).pack(anchor="w", padx=15, pady=2)

    else:

        tk.Label(
            historico_frame,
            text="Nenhuma ação registrada.",
            bg="#2a2a2a",
            fg="#777777",
            font=("Courier", 10)
        ).pack(anchor="w", padx=15, pady=10)

    # ==========================
    # BOTÕES
    # ==========================

    frame_botoes = tk.Frame(
        tela_ficha,
        bg="#1a1a1a"
    )
    frame_botoes.pack(pady=(0, 20))

    def iniciar():
        tela_ficha.destroy()
        iniciar_jogo(fichas["nome"])

    tk.Button(
        frame_botoes,
        text="▶ INICIAR JOGO",
        command=iniciar,
        bg="#00e676",
        fg="#000000",
        relief="flat",
        font=("Courier", 11, "bold"),
        cursor="hand2",
        padx=20,
        pady=8
    ).pack(side="left", padx=8)

    tk.Button(
        frame_botoes,
        text="✕ FECHAR",
        command=tela_ficha.destroy,
        bg="#2d2d2d",
        fg="#ffffff",
        relief="flat",
        font=("Courier", 11, "bold"),
        cursor="hand2",
        padx=20,
        pady=8
    ).pack(side="left", padx=8)