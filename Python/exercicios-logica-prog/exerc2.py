numero1 = float(input("Insira o 1 numero: "))
numero2 = float(input("Insira o 2 numero: "))
numero3 = float(input("Insira o 3 numero: "))

lista = [numero1, numero2, numero3]
lista.sort(key=float, reverse=True)
print(lista)
