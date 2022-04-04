def obter_dados_cadastrais():
    print('*** DDOS CADASTRAIS ***')

    nome = input('Nome: ')
    idade = input('Idade: ')
    cpf = input('CPF: ')
    data_nascimento = input('Data de Nascimento (aa/mm/aaaa): ')

    print('Nome: {}\nIdade: {}\nCPF:{}\nData Nascimento: {}'.format(
        nome,
        idade,
        cpf,
        data_nascimento
    ))

    return input('### CONFIRME SEUS DADOS (S/N): ')


def main():
    dados_corretos = obter_dados_cadastrais()

    if dados_corretos == 'S':
        print('Dados Corretos!')
    else:
        obter_dados_cadastrais()


if __name__ == '__main__':
    main()
