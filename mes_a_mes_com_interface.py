import tkinter as tk
from BackCodes.relatorio import gerar_resultado_final
from tkinter import messagebox
import random
import json


def carregar_config():
    with open ("Arquivos_JSON/config.json", "r", encoding ="utf-8") as arq:
        return json.load (arq)

def carregar_opcoes():
    with open ("Arquivos_JSON/opcoes.json", "r", encoding ="utf-8") as arq:
        return json.load (arq)

CONFIG = carregar_config()
TODAS_OPCOES = carregar_opcoes()

def recarregar_dados():
    global CONFIG
    global TODAS_OPCOES
    global BOLSA
    global SALDO_INIT
    global CUSTO_VIDA
    global MESES

    CONFIG = carregar_config()
    TODAS_OPCOES = carregar_opcoes()

    BOLSA = CONFIG["bolsa"]
    SALDO_INIT = CONFIG["saldo_inicial"]
    CUSTO_VIDA = CONFIG["custo_vida"]
    MESES = CONFIG["meses"]

def label_opcao(op):
    t = op["tipo"]
    if t == "fixo":
        v = op["valor"]
        return f"+R${v}" if v >= 0 else f"-R${abs(v)}"
    elif t == "renda_fixa":
        return f"+{op['taxa']*100:.0f}% do saldo atual"
    elif t == "chance":
        return f"Custa R${abs(op['custo'])} | resultado incerto..."
    elif t == "bonus_unico":
        return f"R${abs(op['custo'])} agora + R${op['bonus']} de bônus depois"
    elif t == "bonus_recorrente":
        return f"R${abs(op['custo'])} agora | +R${op['bonus_mensal']}/mês depois"

def sortear_opcoes():
    pool = TODAS_OPCOES.copy()
    random.shuffle(pool)
    resultado = {}
    idx = 0
    for m in range(1, 13):
        resultado[m] = pool[idx:idx+4]
        idx += 4
        if idx + 4 > len(pool):
            random.shuffle(pool)
            idx = 0
    return resultado

def classificacao(saldo):
    if saldo >= 8000: return "💎 Investidor Nato",        "Você soube equilibrar risco e prudência!"
    if saldo >= 5000: return "📈 Planejador Inteligente", "Suas escolhas foram sólidas. Muito bem!"
    if saldo >= 3000: return "👍 No Azul",                "Terminou positivo. Pra estagiário, tá ótimo!"
    if saldo >= 1000: return "😅 Quase Quebrado",         "Sobrou pouquinho. Algumas escolhas foram questionáveis."
    if saldo >= 0:    return "😬 No Limite",              "Zero a zero. Qualquer imprevisto e você tá na rua."
    return             "💀 Falido",                       "Saldo negativo. O agiota tá te ligando."


class Jogo:
    def __init__(self, root, nome_usuario):
        self.root = root
        self.nome_usuario = nome_usuario

        self.root.title("Sobrevivendo ao Mês")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a1a1a")

        self.tela_inicio()
        self.relatorio_gerado = False

    def limpar(self):
        for w in self.root.winfo_children():
            w.destroy()

    def frame(self, **kw):
        return tk.Frame(self.root, bg="#1a1a1a", **kw)

    def label(self, pai, texto, tamanho=11, cor="#f0f0f0", negrito=False, **kw):
        peso = "bold" if negrito else "normal"
        return tk.Label(pai, text=texto, bg="#1a1a1a", fg=cor,
                        font=("Courier", tamanho, peso), **kw)

    def botao(self, pai, texto, cmd, cor_bg="#2d2d2d", cor_fg="#f0f0f0", **kw):
        return tk.Button(pai, text=texto, command=cmd,
                         bg=cor_bg, fg=cor_fg, relief="flat",
                         font=("Courier", 10, "bold"),
                         activebackground="#3d3d3d", activeforeground="#fff",
                         cursor="hand2", padx=12, pady=6, **kw)

    def tela_inicio(self):
        self.limpar()
        f = self.frame()
        f.pack(expand=True)

        self.label(f, "💸 SOBREVIVENDO AO MÊS 💸", 18, "#00e676", negrito=True).pack(pady=(0,20))
        self.label(f, "Você é um estagiário com R$1.800 de saldo inicial.", 10, "#aaa").pack()
        self.label(f, "A cada mês você recebe R$800 de bolsa e enfrenta", 10, "#aaa").pack()
        self.label(f, "uma escolha financeira. Boa sorte...", 10, "#aaa").pack(pady=(0,30))

        self.botao(f, "  ▶  COMEÇAR JOGO  ", self.iniciar,
                   cor_bg="#00e676", cor_fg="#000").pack()

    def iniciar(self):
        recarregar_dados()

        self.saldo         = SALDO_INIT
        self.mes           = 1
        self.bonus_mensal  = 0
        self.historico     = []
        self.meses_opcoes  = sortear_opcoes()
        self.tela_mes()

    def tela_mes(self):
        # Primeiro, verifica se o jogo acabou
        if self.mes > 12:
            self.tela_fim()
            return
        # Só aplica o custo se estiver dentro do período do jogo
        if self.mes > 1 and self.mes <= 12:
            self.saldo += (BOLSA + self.bonus_mensal - CUSTO_VIDA)
            
            self.historico.append({
                "mes": MESES[self.mes-1], 
                "opcao": "Custo de vida (Aluguel/Comida)", 
                "delta": -(CUSTO_VIDA)
            })

        self.limpar()
        opcoes = self.meses_opcoes[self.mes]

        cab = self.frame()
        cab.pack(fill="x", padx=20, pady=(15,0))

        esq = tk.Frame(cab, bg="#1a1a1a")
        esq.pack(side="left")
        self.label(esq, f"Mês {self.mes}/12  —  {MESES[self.mes-1]}", 13, "#f0f0f0", negrito=True).pack(anchor="w")
        if self.bonus_mensal > 0:
            self.label(esq, f"📈 Bônus recorrente: +R${self.bonus_mensal}/mês", 9, "#00e676").pack(anchor="w")

        cor_saldo = "#00e676" if self.saldo >= 0 else "#ff1744"
        self.label(cab, f"💰 R${self.saldo:,.2f}", 13, cor_saldo, negrito=True).pack(side="right")

        barra_frame = tk.Frame(self.root, bg="#1a1a1a")
        barra_frame.pack(fill="x", padx=20, pady=(8,0))
        canvas = tk.Canvas(barra_frame, height=8, bg="#2d2d2d",
                           highlightthickness=0, relief="flat")
        canvas.pack(fill="x")
        canvas.update_idletasks()
        w = canvas.winfo_width() or 660
        fill_w = int(w * (self.mes - 1) / 12)
        canvas.create_rectangle(0, 0, fill_w, 8, fill="#00e676", outline="")

        tk.Frame(self.root, bg="#333", height=1).pack(fill="x", padx=20, pady=8)

        self.label(self.root, "O que você vai fazer este mês?", 11, "#ccc").pack(padx=20, anchor="w")

        letras = ["A", "B", "C", "D"]
        opts_frame = tk.Frame(self.root, bg="#1a1a1a")
        opts_frame.pack(fill="x", padx=20, pady=8)

        for i, op in enumerate(opcoes):
            card = tk.Frame(opts_frame, bg="#2a2a2a", relief="flat", bd=0)
            card.pack(fill="x", pady=4)

            inner = tk.Frame(card, bg="#2a2a2a")
            inner.pack(fill="x", padx=12, pady=10)

            tk.Label(inner, text=letras[i], bg="#444", fg="#fff",
                     font=("Courier", 10, "bold"),
                     width=2, relief="flat").pack(side="left", padx=(0,10))

            txt_frame = tk.Frame(inner, bg="#2a2a2a")
            txt_frame.pack(side="left", fill="x", expand=True)
            tk.Label(txt_frame, text=op["texto"], bg="#2a2a2a", fg="#f0f0f0",
                     font=("Courier", 10), anchor="w", justify="left").pack(anchor="w")

            lbl = label_opcao(op)
            t = op["tipo"]
            cor_lbl = "#00e676" if t in ("fixo",) and op.get("valor",0) >= 0 else \
                      "#ff1744" if t == "fixo" and op.get("valor",0) < 0 else "#ffd600"
            tk.Label(txt_frame, text=lbl, bg="#2a2a2a", fg=cor_lbl,
                     font=("Courier", 9), anchor="w").pack(anchor="w")

            btn = tk.Button(inner, text="Escolher",
                            command=lambda o=op: self.escolher(o),
                            bg="#333", fg="#fff", relief="flat",
                            font=("Courier", 9, "bold"),
                            activebackground="#555", cursor="hand2",
                            padx=10, pady=4)
            btn.pack(side="right")

        tk.Frame(self.root, bg="#333", height=1).pack(fill="x", padx=20, pady=8)

        self.label(self.root, "Histórico recente:", 9, "#666").pack(padx=20, anchor="w")
        hist_frame = tk.Frame(self.root, bg="#1a1a1a")
        hist_frame.pack(fill="x", padx=20, pady=(4,0))

        for h in reversed(self.historico[-4:]):
            sinal = "+" if h["delta"] >= 0 else ""
            cor   = "#00e676" if h["delta"] >= 0 else "#ff1744"
            linha = tk.Frame(hist_frame, bg="#1a1a1a")
            linha.pack(fill="x")
            tk.Label(linha, text=f"{h['mes'][:3]}  {h['opcao'][:38]:<38}",
                     bg="#1a1a1a", fg="#555", font=("Courier", 8), anchor="w").pack(side="left")
            tk.Label(linha, text=f"{sinal}R${abs(h['delta']):,.2f}",
                     bg="#1a1a1a", fg=cor, font=("Courier", 8, "bold")).pack(side="right")



    def escolher(self, op):
        tipo  = op["tipo"]
        delta = 0

        if tipo == "fixo":
            delta = op["valor"]
            self.saldo += delta
            self._popup_resultado(delta, op["texto"])

        elif tipo == "renda_fixa":
            delta = self.saldo * op["taxa"]
            self.saldo += delta
            self._popup_resultado(delta, f"Renda fixa +{op['taxa']*100:.0f}%")

        elif tipo == "chance":
            self.saldo += op["custo"]
            delta += op["custo"]
            ganhou = random.random() < op["prob"]
            if ganhou:
                self.saldo += op["ganho"]
                delta += op["ganho"]
                msg = f"🎉 {op['desc_ganho']}\n\n+R${op['ganho']:,.2f}"
                cor = "#00e676"
            else:
                self.saldo += op["perda"]
                delta += op["perda"]
                msg = f"😢 {op['desc_perda']}"
                if op["perda"] != 0:
                    msg += f"\n\nR${op['perda']:,.2f}"
                cor = "#ff1744"
            self.historico.append({"mes": MESES[self.mes-1], "opcao": op["texto"], "delta": delta})
            self._popup_chance(msg, cor)
            return

        elif tipo == "bonus_unico":
            self.saldo += op["custo"]
            delta += op["custo"]
            self.saldo += op["bonus"]
            delta += op["bonus"]
            msg = f"📚 {op['desc_bonus']}\n\nBônus: +R${op['bonus']:,.2f}"
            self.historico.append({"mes": MESES[self.mes-1], "opcao": op["texto"], "delta": delta})
            self._popup_chance(msg, "#00e676")
            return

        elif tipo == "bonus_recorrente":
            self.saldo += op["custo"]
            delta += op["custo"]
            self.bonus_mensal += op["bonus_mensal"]
            msg = f"📈 {op['desc_bonus']}"
            self.historico.append({"mes": MESES[self.mes-1], "opcao": op["texto"], "delta": delta})
            self._popup_chance(msg, "#ffd600")
            return

        self.historico.append({"mes": MESES[self.mes-1], "opcao": op["texto"], "delta": delta})
        self.mes += 1
        self.tela_mes()

    def gerar_relatorio(self):

        historico_relatorio = []

        for h in self.historico:
            historico_relatorio.append(
                f"{h['mes']} | {h['opcao']} | Impacto: R$ {h['delta']:.2f}"
            )

        gerar_resultado_final(
            self.nome_usuario,
            self.saldo,
            historico_relatorio
        )

        messagebox.showinfo(
            "Relatório",
            f"Relatório do jogador {self.nome_usuario} gerado com sucesso!"
        )
    def _popup_resultado(self, delta, texto):
        win = tk.Toplevel(self.root)
        win.title("Resultado")
        win.geometry("340x180")
        win.configure(bg="#1a1a1a")
        win.grab_set()
        win.resizable(False, False)

        cor   = "#00e676" if delta >= 0 else "#ff1744"
        sinal = "+" if delta >= 0 else ""
        icone = "✅" if delta > 0 else "💸" if delta < 0 else "😐"

        tk.Label(win, text=icone, bg="#1a1a1a", font=("Courier", 28)).pack(pady=(20,4))
        tk.Label(win, text=f"{sinal}R${abs(delta):,.2f}", bg="#1a1a1a", fg=cor,
                 font=("Courier", 18, "bold")).pack()
        tk.Label(win, text=texto[:50], bg="#1a1a1a", fg="#888",
                 font=("Courier", 8), wraplength=300).pack(pady=4)

        def fechar():
            win.destroy()
            self.mes += 1
            self.tela_mes()

        tk.Button(win, text="Continuar →", command=fechar,
                  bg="#2d2d2d", fg="#fff", relief="flat",
                  font=("Courier", 10, "bold"), cursor="hand2",
                  padx=16, pady=6).pack(pady=12)

    def _popup_chance(self, msg, cor):
        win = tk.Toplevel(self.root)
        win.title("Resultado")
        win.geometry("360x220")
        win.configure(bg="#1a1a1a")
        win.grab_set()
        win.resizable(False, False)

        tk.Label(win, text="🎲 Resultado", bg="#1a1a1a", fg=cor,
                 font=("Courier", 13, "bold")).pack(pady=(20,10))
        tk.Label(win, text=msg, bg="#1a1a1a", fg="#f0f0f0",
                 font=("Courier", 10), wraplength=320, justify="center").pack(padx=20)

        def fechar():
            win.destroy()
            self.mes += 1
            self.tela_mes()

        tk.Button(win, text="Continuar →", command=fechar,
                  bg="#2d2d2d", fg="#fff", relief="flat",
                  font=("Courier", 10, "bold"), cursor="hand2",
                  padx=16, pady=6).pack(pady=16)

    def tela_fim(self):
        historico_relatorio = []

        if not self.relatorio_gerado:

            self.limpar()
        rank, desc = classificacao(self.saldo)
        cor = "#00e676" if self.saldo >= 3000 else "#ffd600" if self.saldo >= 1000 else "#ff1744"

        f = tk.Frame(self.root, bg="#1a1a1a")
        f.pack(expand=True, fill="both", padx=30, pady=20)

        self.label(f, "🎊 FIM DO ANO!", 16, "#f0f0f0", negrito=True).pack(pady=(0,6))
        tk.Frame(f, bg="#333", height=1).pack(fill="x", pady=6)
        self.label(f, "Saldo Final:", 10, "#666").pack()
        self.label(f, f"R${self.saldo:,.2f}", 22, cor, negrito=True).pack(pady=4)
        tk.Frame(f, bg="#333", height=1).pack(fill="x", pady=8)
        self.label(f, rank, 13, cor, negrito=True).pack()
        self.label(f, desc, 9, "#aaa").pack(pady=(4,12))

        tk.Label(f, text="Histórico completo:", bg="#1a1a1a", fg="#555",
                 font=("Courier", 9, "bold"), anchor="w").pack(anchor="w")

        frame_hist = tk.Frame(f, bg="#1a1a1a")
        frame_hist.pack(fill="x", pady=4)
        for h in self.historico[-5:]:
            sinal = "+" if h["delta"] >= 0 else ""
            cor_h = "#00e676" if h["delta"] >= 0 else "#ff1744"
            row = tk.Frame(frame_hist, bg="#1a1a1a")
            row.pack(fill="x")
            tk.Label(row, text=f"{h['mes'][:3]}  {h['opcao'][:40]:<40}",
                     bg="#1a1a1a", fg="#555", font=("Courier", 8), anchor="w").pack(side="left")
            tk.Label(row, text=f"{sinal}R${abs(h['delta']):,.2f}",
                     bg="#1a1a1a", fg=cor_h, font=("Courier", 8, "bold")).pack(side="right")

        tk.Frame(f, bg="#333", height=1).pack(fill="x", pady=10)

        btns = tk.Frame(f, bg="#1a1a1a")
        btns.pack()
        self.botao(btns, "  ▶  JOGAR NOVAMENTE  ", self.iniciar,
                   cor_bg="#00e676", cor_fg="#000").pack(side="left", padx=6)
        self.botao(
            btns,
            "📄 GERAR RELATÓRIO",
            self.gerar_relatorio,
            cor_bg="#2196F3",
            cor_fg="#fff"
        ).pack(side="left", padx=6)
        self.botao(btns, "  ✕  SAIR  ", self.root.quit,
                   cor_bg="#2d2d2d", cor_fg="#fff").pack(side="left", padx=6)


def iniciar_jogo(nome_usuario):
    # Cria uma nova janela para o jogo, independente do login
    root_jogo = tk.Tk()
    app = Jogo(root_jogo, nome_usuario)
    root_jogo.mainloop()

if __name__ == "__main__":
    pass
