numero1 = float(input("Insira o 1 numero: "))
numero2 = float(input("Insira o 2 numero: "))
numero3 = float(input("Insira o 3 numero: "))

lista = [numero1, numero2, numero3]
print(max(lista))

if numero1 >= numero2 and numero1 >= numero3:
    print(numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print(numero2)
elif numero3 >= numero1 and numero3 >= numero2:
    print(numero3)

