import os
import time

NUMERO_SECRETO = 42


def main():
    print('\n')
    print('\t*******************************')
    print('\t**     JOGO DA ADVINHAÇÃO    **')
    print('\t*******************************')
    print('\n')

    nivel_jogo = int(
        input(
            '\t{}\n\t{}\n\t{}\n\t{}\n\t{}'
            .format(
                'Escolha o nível do jogo',
                'Nível 1) 3 Tentativas',
                'Nível 2) 6 Tentativas',
                'Nível 3) 9 Tentativas',
                'Nível: ',
            )
        )
    )

    total_tentativas = nivel_jogo * 3
    total_pontos = 1000

    for numero_da_rodada in range(1, (total_tentativas + 1)):
        print('\t-------- RODADA: {} -----------'.format(numero_da_rodada))
        print('\t-------- TOTAL PONTOS: {} -----------'.format(total_pontos))
        print('\n')

        chute_numero_informado = int(input('\tTente advinhar o número: '))
        print('\tNúmero informado: {}'.format(chute_numero_informado))

        acertou_numero_secreto = NUMERO_SECRETO == chute_numero_informado
        numero_secreto_eh_maior = NUMERO_SECRETO > chute_numero_informado
        numero_secreto_eh_menor = NUMERO_SECRETO < chute_numero_informado

        print('\n')

        if acertou_numero_secreto:
            print('\t*** ACERTOOOUUUu!! ***')
            print('\t-------- PONTUAÇÃO FINAL: {} -----------'.format(total_pontos))
            print('\n')
            break

        if numero_secreto_eh_maior:
            print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MAIOR que {}'
                  .format(chute_numero_informado))
            total_pontos = abs(chute_numero_informado - NUMERO_SECRETO)
            time.sleep(2)

        if numero_secreto_eh_menor:
            print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MENOR que {}'
                  .format(chute_numero_informado))
            total_pontos = abs(chute_numero_informado - NUMERO_SECRETO)
            time.sleep(2)

        print('\n')
        os.system('clear')


if __name__ == '__main__':
    main()
