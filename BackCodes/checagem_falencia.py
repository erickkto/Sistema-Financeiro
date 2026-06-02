from fichas import criar_ficha

LIMITE_FALENCIA = -2000

def checar_falencia(saldo, mes, escolha_fatidica):
    if saldo <= LIMITE_FALENCIA:
        print("\n" + "="*50)
        print("Você Faliu!")
        print("="*50)
        print(f"Mês: {mes}")
        print(f"Saldo final: R$ {saldo:.2f}")
        print(f"Última decisão: {escolha_fatidica}")
        print("="*50)

        with open("relatorio.txt", "w", encoding="utf-8") as f:
            f.write("AVISO DE DESPEJO\n")
            f.write("="*50 + "\n")
            f.write(f"Você faliu no mês {mes}.\n")
            f.write(f"Saldo final: R$ {saldo:.2f}\n")
            f.write(f"A escolha que te afundou: {escolha_fatidica}\n")
            f.write("O miojo acabou. De volta pra casa dos pais.\n")

        return True

    return False 