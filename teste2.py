import tkinter as tk
from teste import jogar_uma_fase, get_decisoes, meses


saldo = 1800
mes_atual = 0


def atualizar():

    global opcoes

    texto_mes.config(text=meses[mes_atual])

    opcoes = get_decisoes(mes_atual, saldo)

    # atualiza texto dos botões corretamente
    botoes["a"].config(text=f"A - {opcoes['a'][0]}")
    botoes["b"].config(text=f"B - {opcoes['b'][0]}")
    botoes["c"].config(text=f"C - {opcoes['c'][0]}")
    botoes["d"].config(text=f"D - {opcoes['d'][0]}")


def escolher(op):

    global saldo, mes_atual

    saldo, msg = jogar_uma_fase(mes_atual, saldo, op)

    resultado.config(text=msg)
    saldo_label.config(text=f"Saldo: {saldo}")

    mes_atual += 1

    if mes_atual >= 12:
        resultado.config(text="Fim do jogo!")
        return

    atualizar()


janela = tk.Tk()
janela.title("Jogo Financeiro")


texto_mes = tk.Label(janela, text="")
texto_mes.pack()

saldo_label = tk.Label(janela, text="Saldo: 1800")
saldo_label.pack()

resultado = tk.Label(janela, text="")
resultado.pack()


botoes = {}

for op in ["a", "b", "c", "d"]:
    botoes[op] = tk.Button(
        janela,
        command=lambda x=op: escolher(x)
    )
    botoes[op].pack()


atualizar()

janela.mainloop()