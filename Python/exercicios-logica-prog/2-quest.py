salario = float(input("Qual salario do funcionario?\n"))

percentual = float(input("Qual o percentual que o salario irá aumentar?\n"))

percentual = (percentual/100) + 1

salario = salario * percentual

print("O novo salario é de R$" + str(salario))
