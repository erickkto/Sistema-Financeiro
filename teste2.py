import tkinter as tk
from teste import Jogo


jogo = Jogo()

janela = tk.Tk()
janela.title("Simulador Financeiro")
janela.geometry("500x400")


lbl_mes = tk.Label(
    janela,
    font=("Arial", 18, "bold")
)
lbl_mes.pack(pady=10)


lbl_saldo = tk.Label(
    janela,
    font=("Arial", 14)
)
lbl_saldo.pack()


lbl_msg = tk.Label(
    janela,
    font=("Arial", 12)
)
lbl_msg.pack(pady=10)


frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)


def atualizar_tela():

    if jogo.acabou():

        lbl_mes.config(text="Fim de Jogo")

        lbl_saldo.config(
            text=f"Saldo Final: R$ {jogo.saldo}"
        )

        lbl_msg.config(
            text="Obrigado por jogar!"
        )

        for widget in frame_botoes.winfo_children():
            widget.destroy()

        return

    lbl_mes.config(
        text=f"Mês: {jogo.nome_mes()}"
    )

    lbl_saldo.config(
        text=f"Saldo: R$ {jogo.saldo}"
    )

    for widget in frame_botoes.winfo_children():
        widget.destroy()

    for chave, dados in jogo.opcoes_atuais.items():

        botao = tk.Button(
            frame_botoes,
            text=f"{chave.upper()} - {dados[0]}",
            width=35,
            command=lambda c=chave: escolher(c)
        )

        botao.pack(pady=3)


def escolher(opcao):

    sucesso, mensagem = jogo.escolher(opcao)

    lbl_msg.config(text=mensagem)

    atualizar_tela()


atualizar_tela()

janela.mainloop()