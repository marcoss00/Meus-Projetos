print('\t\t\tAssistente virtual para calouros')
print('Seja bem vindo! Como posso ajudar ? ')
repeticao2 = True


while(repeticao2):
    palavras_encontradas = 0
    encontrou_palavra_chave = True
    repeticao2 = False
    duvida = input()
    palavra_chave = 'login'
    palavra_chave2 = 'login?'
    repeticao = True
    lista = duvida.split()

    for palavra in lista:
        if palavra == palavra_chave or palavra == palavra_chave2:
            encontrou_palavra_chave = False
            print("Você quer ajuda  no seu primeiro login em laboratorios da argo ?")
            while (repeticao):

                repeticao = False
                escolha = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                if escolha == 1:
                    print('Voce quer informações sobre:')
                    inf_login = int(input('Digite 1 (login)\nDigite 2 (senha)\n'))
                    if inf_login == 1:
                        print("Para fazer o login você deve usar a sua matrícula como nome de usuário.")
                        print('Posso ajudar em mais alguma coisa?')
                        escolha4 = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                        if escolha4 == 1:
                            repeticao2 = True
                            print('Como posso ajudar?')
                    elif inf_login == 2:
                        print("Sua senha padrão é sua data de nascimento (no formato: dd/mm/aaaa)")
                        print('\n\nVocê gostaria de saber como alterar a sua senha?')
                        escolha2 = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                        if escolha2 == 1:
                            print('Para alterar a sua senha acesse: http://www2.cesupa.br/TIA/aluno-on.asp e clique em "alteração de senha"')
                            print('Posso ajudar em mais alguma coisa?')
                            escolha3 = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                            if escolha3 == 1:
                                repeticao2 = True
                                print('Como posso ajudar?')
                        elif escolha2 == 2:
                            print('Posso ajudar em mais alguma coisa?')
                            escolha5 = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                            if escolha5 == 1:
                                repeticao2 = True
                                print('Como posso ajudar?')
                elif escolha == 2:
                    print('Não entendi a sua dúvida! Explique melhor, por favor!')
                    repeticao2 = True
                else:
                    print('Opção invalida!')
                    repeticao = True

        elif palavra == 'laboratorio' or palavra == 'laboratório' or palavra == 'encontrar' or palavra =='localizar' or palavra == 'laboratórios' or palavra == 'laboratorios' or palavra == 'encontro' or palavra == 'acho' or palavra == 'fica':
            palavras_encontradas= palavras_encontradas + 1
            if palavras_encontradas >= 2:
                repeticao3 = True
                print("Você quer ajuda para localizar o laboratório no qual você vai ter aula ?")
                while (repeticao3):
                    repeticao3 = False
                    encontrou_palavra_chave = False
                    escolha_lab = int(input('Digite 1 (sim)\nDigite 2 (não)\n'))
                    if escolha_lab == 1:
                        print('De qual disciplina você quer saber o laboratório?')
                        disciplina = int(input('Digite 1 (Programação)\nDigite 2 (Arquitetura de computadores)\n'))
                        if disciplina == 1:
                            print('Você terá aula no laboratório 301, 3º andar')
                        elif disciplina == 2:
                            print('Você terá aula no laboratório 405, 4º andar')
                    elif escolha_lab == 2:
                        print('Não entendi a sua dúvida! Explique melhor, por favor!')
                        repeticao2 = True
                    else:
                        print('Opção invalida!')
                        repeticao3 = True
    if(encontrou_palavra_chave):
        print('Não sei nada sobre a sua dúvida!')

print('\n\n\t\t\tSeja bem vindo ao cesupa! Até a proxima.')