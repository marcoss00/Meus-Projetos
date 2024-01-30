quant = int(input("De quantos funcionarios vc quer calcular o salario?"))
nome = []
salario = []
novo_salario = []
for i in range(0, quant):
    nome_aux = input("Qual o nome do funcionario " + str(i+1) + "?")
    nome.append(nome_aux)
    salario_aux = float(input("Qual o salario desse funcionario?"))
    salario.append(salario_aux)

    if salario[i] <= 1500:
        novo_salario_aux = salario[i] * 1.25
        novo_salario.append(novo_salario_aux)
    elif 1500 < salario[i] <= 3000:
        novo_salario_aux = salario[i] * 1.20
        novo_salario.append(novo_salario_aux)
    elif 3000 < salario[i] <= 6000:
        novo_salario_aux = salario[i] * 1.15
        novo_salario.append(novo_salario_aux)
    else:
        novo_salario_aux = salario[i] * 1.10
        novo_salario.append(novo_salario_aux)

    print("O funcionario chamado " + str(nome[i]) + " ganha R$"+ str(salario[i]) + " e terá um novo salario de R$" + str(novo_salario[i]))

print("A soma dos salarios reajustados é de: R$" + str(sum(novo_salario)))
print("A soma dos salarios é de: R$" + str(sum(salario)))
print("A diferença entre eles é de: R$" + str(sum(novo_salario) - sum(salario)))

