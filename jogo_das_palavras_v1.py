
import os

palavras_secretas = ['perfume', 'desodorante', 'aromas', 'sabor']

def reset() :
    while True:
        palavra_formada = 0
        palavra_secreta = ''
        escolher_palavra = ''
        letras_acertadas = ''
        tentativas = 0
        max_tentativas = 5

        while True:

            retornar_escolher_palavra = 0
            print(60 * '-')
            escolher_palavra = input('Escolha a palavra que deseja advinha ([1] [2] [3] [4]): ')
            print(60 * '-')

            if len(escolher_palavra) == 1:
                escolher_palavra = int(escolher_palavra)
            else:
                os.system('cls')
                print('Voce deve escolher apenas uma opção e digitar apenas os numerais como indicado no enunciado.')
                continue


            if palavras_secretas[escolher_palavra - 1]:
                palavra_secreta = palavras_secretas[escolher_palavra - 1]
                print(f'A escolhida foi a palavra {escolher_palavra}')
            else:
                os.system('cls')
                print('Esta opção ainda não esta disponivel para escolha.')
                continue 

            while True:

                os.system('cls')
                print('Palavra foi escolhida com sucesso.')
                print(60 * '-')
                print(f'A escolhida foi a palavra número: {escolher_palavra}')
                print(60 * '-')
                confirmar_escolha_palavra = input('Deseja manter sua escolha: [S] / [N]: ').lower()
                print(60 * '-')
                os.system('cls')

                if confirmar_escolha_palavra.startswith('s'):
                    print('Então vamos nessa!!!')
                    retornar_escolher_palavra = 1
                    break
                elif confirmar_escolha_palavra.startswith('n'):
                    print('Então...')         
                    print(60 * '-')
                    retornar_escolher_palavra = 0
                    break
                else:
                    print('Desculpe, esta opção não existe.')
                    print(60 * '-')
                    continue

            if retornar_escolher_palavra == 1 : 
                break
            elif retornar_escolher_palavra == 0 :
                continue
            else:
                print('Não deveria chegar aqui!')

            break

        while True:
            
            letras_digitada = input('Digite a letra: ').lower()

            if len(letras_digitada) > 1:
                os.system('cls')
                print('Voce deve digitar apenas uma letra.')
                print(10 * '-')
                continue

            if letras_digitada in palavra_secreta:
                letras_acertadas += letras_digitada

            palavra_formada = ''
            for letras_secreta in palavra_secreta:
                if letras_secreta in letras_acertadas:
                    palavra_formada += letras_secreta
                else:
                    palavra_formada += '*'

            print(f' Palavra formada: {palavra_formada}')

            if palavra_formada == palavra_secreta: 
                os.system('cls')
                print(60 * '-')
                print('Parabens voce conseguiu desvendar a palavra!!!!!!')
                print(60 * '-')
                print(f'A palavra secreta é {palavra_secreta}')
                print(60 * '-')
                break 

        reiniciar_jogo_teste = 0
        if palavra_formada in palavra_secreta:
            reiniciar_jogo = input('Deseja iniciar novamente [S] / [N]: ').lower()
            os.system('cls')
            if reiniciar_jogo.startswith('s'):
                reiniciar_jogo_teste = 1
                os.system('cls')
                print('Reiniciando jogo...')
                continue
            elif reiniciar_jogo.startswith('n'):
                reiniciar_jogo_teste = 0
                os.system('cls')
                print('Jogo finaizado..., Volte sempre.')
                break
            else:
                os.system('cls')
                print('Esta opção nao é valida')
                continue

        if reiniciar_jogo_teste == 1 :
            palavra_formada = 0
            continue
        elif reiniciar_jogo_teste == 0 :
            break

        break

reset()