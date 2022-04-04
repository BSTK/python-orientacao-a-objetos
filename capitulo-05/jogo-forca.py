def main():
    print('\t************************************')
    print('\t*        JOGO DA FORCA             *')
    print('\t************************************')

    enforcado = False
    acertou_palavra = False
    total_erros = 0

    palavra_secreta = 'banana'
    letras_corretas = ['_', '_', '_', '_', '_', '_']

    print('\t{}'.format(letras_corretas))

    while not acertou_palavra and not enforcado:
        letra_informada = input('\n\tInforme uma letra? ')
        posicao = 0

        if letra_informada in palavra_secreta:
            for letra in palavra_secreta:
                if letra.upper() == letra_informada.upper():
                    letras_corretas[posicao] = letra_informada

                posicao += 1
        else:
            total_erros += 1

        print('\t{}'.format(letras_corretas))

        acertou_palavra = '_' not in letras_corretas
        enforcado = total_erros == 6

        print('\n')

    if acertou_palavra:
        print('\t************************************************')
        print('\t*** PARABÉNS! VC ACERTOU A PALAVRA SECRETA!! ***')
        print('\t*** PALAVRA: {}                          ***'.format(palavra_secreta))
        print('\t************************************************')
        print('\n')
    else:
        print('\t*** )-: NÃO FOI DESSA VEZ! TENTE NOVAMENTE!! ***')
        print('\n')


if __name__ == '__main__':
    main()
