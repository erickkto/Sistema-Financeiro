from p import Pessoa
from fichas import criar_ficha

usuarios = []
usuario_logado = None


def cadastrar_usuario(nome, senha):

    if not nome or not senha:
        return False, "Preencha todos os campos!"

    for p in usuarios:
        if p.nome == nome:
            return False, "Nome já cadastrado!"

    novo_usuario = Pessoa(nome, senha)
    usuarios.append(novo_usuario)

    return True, "Usuário cadastrado com sucesso!"


def fazer_login(nome, senha):

    global usuario_logado

    if not nome or not senha:
        return False, "Preencha todos os campos!", None

    for p in usuarios:

        if p.nome == nome and p.verificar_senha(senha):

            usuario_logado = p

            ficha = criar_ficha(usuario_logado)

            return True, f"Bem-vindo, {nome}!", ficha

    return False, "Nome ou senha incorretos!", None