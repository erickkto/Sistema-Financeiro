import random 

imprevistos = [0, 1, 2, 3, 4, 5]
pesos_imprevistos = [60, 5, 20, 4, 10, 1]

imprevistos [0] = "Sem imprevistos"
imprevistos [1] = "Perdeu a perna"
imprevistos [2] = "Foi roubado"
imprevistos [3] = "Geladeira deu defeito"
imprevistos [4] = "Achou 200 reais na rua"
imprevistos [5] = "Ganhou na loteria"

escolha = random.choices(imprevistos, weights=pesos_imprevistos, k = 1)[0] 
print (escolha) 