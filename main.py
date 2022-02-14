# gerar nome, gerar email, gerar telefone, gerar cidade, gerar estado
def line():
    return '-' * 50


def title(message):
    print(line())
    print(f'|{message:^48}|')
    print(line())


def menu(*options):
    for index, option in enumerate(options):
        print(f'[ \033[0;33m{index + 1}\033[m ] - \033[0;33m{option}\033[m')
    print()
    print('Digite "\033[0;33mparar\033[m" para fechar o programa.')
    print(line())


title("GERADOR DE DADOS ALEATÓRIOS")
menu('Gerar nome', 'Gerar email', 'Gerar telefone',
     'Gerar cidade', 'Gerar estado')
