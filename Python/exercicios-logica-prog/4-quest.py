racao_comprada = float(input("Quanto Pedro comprou de racao em Kg?"))

racao_comprada = racao_comprada*1000

racao_fornecida = float(input("Quanto Pedro deu de racao para cada gato em gramas?"))

racao_fornecida = racao_fornecida*2

restou = racao_comprada - racao_fornecida*5

print("Restaram " + str(restou) + "g de racao depois de 5 dias")

