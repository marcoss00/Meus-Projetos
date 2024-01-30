valor_emprestado = float(input("Quanto voce que emprestar do banco?"))
valor_pago_mensal = float(input("Quanto voce vai pagar a cada mes?"))
juros = float(input("Quanto é o juros mensais (em %)?"))

pago_de_juros = valor_pago_mensal * juros / 100
valor_pago_mensal_real = valor_pago_mensal - pago_de_juros
juros_total_pago = 0
quant_meses = 0
valor_pago_total = 0

print("Voce vai pagar todo mes R$" + str(pago_de_juros) + " de juros")

while valor_emprestado > valor_pago_mensal_real:
    quant_meses = quant_meses + 1
    valor_emprestado = valor_emprestado - valor_pago_mensal_real
    juros_total_pago = juros_total_pago + pago_de_juros
    valor_pago_total = valor_pago_total + valor_pago_mensal
    print("Depois do mes "+str(quant_meses)+" ainda restam pagar: R$"+str(valor_emprestado) + " e voce ja pagou R$" + str(juros_total_pago) + " de juros até o momento")

pago_de_juros = valor_emprestado*juros/100
valor_pago_total = valor_pago_total + pago_de_juros + valor_emprestado
juros_total_pago = juros_total_pago + pago_de_juros
quant_meses = quant_meses + 1
print("Serao necessarios " + str(quant_meses) + " meses para pagar o emprestimo")
print("O valor da ultima prestacao vai ser de R$" + str(valor_emprestado) + " + juros de R$" + str(pago_de_juros))
print("Ao final voce vai ter pago R$" + str(juros_total_pago) + " de juros no total")
print("Ao final voce vai ter pago R$" + str(valor_pago_total) + " no total")


