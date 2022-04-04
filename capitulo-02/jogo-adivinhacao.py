NUMERO_SECRETO = 42


def main():
    print('\n')
    print('\t*******************************')
    print('\t**     JOGO DA ADVINHAÇÃO    **')
    print('\t*******************************')
    print('\n')

    chute_numero_informado = int(input('\tTente advinhar o número: '))
    print('\tNúmero informado: {}'.format(chute_numero_informado))

    acertou_numero_secreto = NUMERO_SECRETO == chute_numero_informado
    numero_secreto_eh_maior = NUMERO_SECRETO > chute_numero_informado
    numero_secreto_eh_menor = NUMERO_SECRETO < chute_numero_informado

    print('\n')

    if acertou_numero_secreto:
        print('\t*** ACERTOOOUUUu!! ***')

    if numero_secreto_eh_maior:
        print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MAIOR que {}'
              .format(chute_numero_informado))

    if numero_secreto_eh_menor:
        print('\t)-: )-: ErrrooouuuU!! Número secreto é -> MENOR que {}'
              .format(chute_numero_informado))

    print('\n')


if __name__ == '__main__':
    main()
