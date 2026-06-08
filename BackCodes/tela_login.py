import tkinter as tk
from p import Pessoa
from fichas import criar_ficha


# Importe diretamente, sem o prefixo 'BackCodes.'
from mes_a_mes_com_interface import iniciar_jogo
from mes_a_mes_com_interface import Jogo

usuarios = []
usuario_logado = None


# ---------------- FICHA (NOVA TELA) ----------------

def abrir_ficha(ficha):

    tela_ficha = tk.Toplevel(janela)
    tela_ficha.title("Ficha do Jogador")
    tela_ficha.geometry("800x600")
    tela_ficha.configure(bg="black")
    tk.Button(
        tela_ficha,
        text="INICIAR JOGO",
        command=lambda: [tela_ficha.destroy(), iniciar_jogo(ficha["nome"])],
        bg="green",
        fg="white",
        font=("Arial", 12, "bold")
    ).pack(pady=20)

    introducao = """
====================================================

Olá, Jogador! Seja bem vindo ao seu jogo de gerenciamento financeiro.
Vamos ver se com sua habilidades de gestão monetária,
você conseguirá se virar nesse mundo em 1 ano!

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
        text=f"Jogador: {ficha['nome']}",
        bg="black",
        fg="white",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
            tela_ficha,
            text=f"Saldo: R$ {ficha['saldo_atual']:.2f}",
            bg="black",
            fg="gold",
            font=("Arial", 14)
        ).pack(pady=5)

    tk.Label(
        tela_ficha,
        text=f"Inventário: {', '.join(ficha['inventario']) if ficha['inventario'] else 'Nenhum'}",
        bg="black",
        fg="cyan",
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        tela_ficha,
        text="Histórico:\n" + ("\n".join(ficha["historico"]) if ficha["historico"] else "Jogo Iniciado"),
        bg="black",
        fg="white",
        justify="left"
    ).pack(pady=5)

    tk.Button(
        tela_ficha,
        text="Fechar Ficha",
        command=tela_ficha.destroy,
        bg="red",
        fg="white",
        font=("Arial", 12)
    ).pack(pady=20)

# ---------------- CADASTRO ----------------

def cadastro():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if not nome or not senha:
        resultado.config(
            text="Preencha todos os campos!",
            fg="red"
        )
        return

    for p in usuarios:
        if p.nome == nome:
            resultado.config(
                text="Nome já cadastrado!",
                fg="red"
            )
            return

    novo_usuario = Pessoa(nome, senha)
    usuarios.append(novo_usuario)

    resultado.config(
        text="Usuário cadastrado com sucesso!",
        fg="green"
    )
    entrada_nome.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)


# ---------------- LOGIN ----------------

def login():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if not nome or not senha:
        resultado.config(
            text="Preencha todos os campos!",
            fg="red"
        )
        return

    global usuario_logado

    for p in usuarios:
        if p.nome == nome and p.verificar_senha(senha):

            resultado.config(
                text=f"Bem-vindo, {nome}!",
                fg="green"
            )

            entrada_nome.delete(0, tk.END)
            entrada_senha.delete(0, tk.END)

            usuario_logado = p

            fichas = criar_ficha(usuario_logado)

            janela.withdraw()

            abrir_ficha(fichas)  # <<< AQUI abre a nova tela

            return

    resultado.config(
        text="Nome ou senha incorretos!",
        fg="red"
    )
    entrada_nome.delete(0, tk.END)
    entrada_senha.delete(0, tk.END)


# ---------------- JANELA PRINCIPAL ----------------

# ---------------- JANELA PRINCIPAL ----------------

janela = tk.Tk()
janela.title("💸 Sobrevivendo ao Mês")
janela.geometry("550x450")
janela.resizable(False, False)
janela.configure(bg="#1a1a1a")

# Frame principal
frame_principal = tk.Frame(
    janela,
    bg="#1a1a1a"
)
frame_principal.pack(expand=True)

# Título
titulo = tk.Label(
    frame_principal,
    text="💸 SOBREVIVENDO AO MÊS 💸",
    bg="#1a1a1a",
    fg="#00e676",
    font=("Courier", 20, "bold")
)
titulo.pack(pady=(20, 10))

# Subtítulo
subtitulo = tk.Label(
    frame_principal,
    text="Gerencie seu dinheiro e sobreviva por 12 meses",
    bg="#1a1a1a",
    fg="#aaaaaa",
    font=("Courier", 10)
)
subtitulo.pack(pady=(0, 25))

# Linha decorativa
linha = tk.Frame(
    frame_principal,
    bg="#333333",
    height=2,
    width=400
)
linha.pack(pady=(0, 25))

# Nome
label_nome = tk.Label(
    frame_principal,
    text="👤 Usuário",
    bg="#1a1a1a",
    fg="#ffffff",
    font=("Courier", 11, "bold")
)
label_nome.pack(anchor="w")

entrada_nome = tk.Entry(
    frame_principal,
    width=35,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Courier", 11)
)
entrada_nome.pack(pady=(5, 15), ipady=5)

# Senha
label_senha = tk.Label(
    frame_principal,
    text="🔒 Senha",
    bg="#1a1a1a",
    fg="#ffffff",
    font=("Courier", 11, "bold")
)
label_senha.pack(anchor="w")

entrada_senha = tk.Entry(
    frame_principal,
    show="*",
    width=35,
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Courier", 11)
)
entrada_senha.pack(pady=(5, 25), ipady=5)

# Frame dos botões
frame_botoes = tk.Frame(
    frame_principal,
    bg="#1a1a1a"
)
frame_botoes.pack()

# Botão Login
botao_login = tk.Button(
    frame_botoes,
    text="▶ LOGIN",
    command=login,
    bg="#00e676",
    fg="black",
    relief="flat",
    font=("Courier", 11, "bold"),
    activebackground="#00c853",
    activeforeground="black",
    cursor="hand2",
    padx=20,
    pady=8
)
botao_login.pack(side="left", padx=8)

# Botão Cadastro
botao_cadastro = tk.Button(
    frame_botoes,
    text="➕ CADASTRAR",
    command=cadastro,
    bg="#2d2d2d",
    fg="white",
    relief="flat",
    font=("Courier", 11, "bold"),
    activebackground="#444444",
    activeforeground="white",
    cursor="hand2",
    padx=20,
    pady=8
)
botao_cadastro.pack(side="left", padx=8)

# Resultado
resultado = tk.Label(
    frame_principal,
    text="",
    bg="#1a1a1a",
    fg="white",
    font=("Courier", 10, "bold")
)
resultado.pack(pady=20)

# Rodapé
rodape = tk.Label(
    frame_principal,
    text="Sistema Financeiro v1.0",
    bg="#1a1a1a",
    fg="#555555",
    font=("Courier", 8)
)
rodape.pack(side="bottom", pady=10)

janela.mainloop()