# gerar nome, gerar email, gerar telefone, gerar cidade, gerar estado
from lib.data import *
from random import choice


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


def validate_user_input_options(inp):
    if inp == 'parar':
        return True

    inp_options = inp.split(',')
    for op in inp_options:
        if len(op) > 1:
            print(
                f'\033[0;31m"{op}" é uma opção inválida! Tente novamente...\033[m')
            print(line())
            return False
        if op not in '12345':
            print(
                f'\033[0;31m"{op}" é uma opção inválida! Tente novamente...\033[m')
            print(line())
            return False

    print(line())
    for op in inp_options:
        if op == '1':
            print(f'Nome: {choice(names)}')
        elif op == '2':
            print(f'Email: {choice(emails)}')
        elif op == '3':
            print(f'Tel: {choice(phones)}')
        elif op == '4':
            print(f'Cid.: {choice(citys)}')
        elif op == '5':
            print(f'Est.: {choice(states)}')
        else:
            print('\033[0;31mOpção inválida! Tente novamente...\033[m')
            print(line())
            return False
    print()
    return True


def validate_user_input_save(inp):
    if inp in 's':
        print('Escolheu salvar.')
        print(line())
        return True
    elif inp in 'n':
        print('Escolheu não salvar.')
        print(line())
        return True
    else:
        print(
            f'\033[0;31m"{inp}" é uma opção inválida!\033[m Digite \033[0;33mS\033[m para sim e \033[0;33mN\033[m para não.')
        print(line())
        return False


title("GERADOR DE DADOS ALEATÓRIOS")
menu('Gerar nome', 'Gerar email', 'Gerar telefone',
     'Gerar cidade', 'Gerar estado')
while True:
    user_option = str(input('Digite sua opção: ')).strip().lower()
    validate_option = validate_user_input_options(user_option)

    if validate_option == True:
        validate_save = False
        while not validate_save:
            user_save_data = str(
                input('Deseja salvar os dados? [S/N] ')).strip().lower()[0]
            validate_save = validate_user_input_save(user_save_data)
        title('Saindo do sistema... até logo!')
        break
