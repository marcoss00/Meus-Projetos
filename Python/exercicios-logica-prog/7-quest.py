quant = int(input("Quantos numeros voce quer que a sua sequencia tenha?"))
sequencia = []
for i in range(0 , quant):
    if i == 0:
        sequencia.append(1)
    elif i == 1:
        sequencia.append(1)
    elif i > 1:
        sequencia.append(sequencia[i - 2] + sequencia[i - 1])

print(sequencia)
if quant in sequencia:
    print(str(quant) + " pertence a sequencia")
