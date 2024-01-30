ano_atual = int(input("Qual o ano atual?"))

ano_de_nascimento = int(input("Qual o seu ano de nascimento?"))

print("A sua idade em anos é: " + str(ano_atual - ano_de_nascimento))
print("A sua idade em meses é: " + str((ano_atual - ano_de_nascimento) * 12))
print("A sua idade em dias é: " + str((ano_atual - ano_de_nascimento) * 12 * 30))
