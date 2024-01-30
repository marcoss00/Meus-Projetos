pares = []
impares = []
todos = []
valor = 4
while valor != 0:
    valor = int(input("Qual numero voce quer adicionar?"))
    if valor == 0:
        break
    todos.append(valor)
    if valor%2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("A quantidade de numeros pares é: " + str(len(pares)))
print("A quantidade de numeros impares é: " + str(len(impares)))
print("A media dos numeros pares é: " + str(sum(pares) / len(pares)))
print("A media de todos os numeros é: " + str(sum(todos) / len(todos)))

