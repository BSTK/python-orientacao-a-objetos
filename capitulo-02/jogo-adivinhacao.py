import os
import time

NUMERO_SECRETO = 42


def main():
    total_tentativas = 3
    numero_da_rodada = 1

    while numero_da_rodada <= total_tentativas:
        print('\n')
        print('\t*******************************')
        print('\t**     JOGO DA ADVINHAÇÃO    **')
        print('\t*******************************')
        print('\n')

        print('\t-------- RODADA: {} -----------'.format(numero_da_rodada))
        print('\n')

        chute_numero_informado = int(input('\tTente advinhar o número: '))
        print('\tNúmero informado: {}'.format(chute_numero_informado))

        acertou_numero_secreto = NUMERO_SECRETO == chute_numero_informado
        numero_secreto_eh_maior = NUMERO_SECRETO > chute_numero_informado
        numero_secreto_eh_menor = NUMERO_SECRETO < chute_numero_informado

        print('\n')

        if acertou_numero_secreto:
            print('\t*** ACERTOOOUUUu!! ***')
            break

        if numero_secreto_eh_maior:
            print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MAIOR que {}'
                  .format(chute_numero_informado))
            numero_da_rodada += 1
            time.sleep(2)

        if numero_secreto_eh_menor:
            print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MENOR que {}'
                  .format(chute_numero_informado))
            numero_da_rodada += 1
            time.sleep(2)

        print('\n')
        os.system('clear')


if __name__ == '__main__':
    main()
