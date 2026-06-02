def criar_ficha(usuario):

    ficha = {
        "nome": usuario.nome,
        "saldo_inicial": 1800.00,
        "saldo_atual": 1800.00,
        "inventario": [],
        "historico": []
    }

    return ficha