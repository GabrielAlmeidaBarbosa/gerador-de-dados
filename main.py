# gerar nome, gerar email, gerar telefone, gerar cidade, gerar estado
from lib.data import *
from random import choice
from time import sleep
from os import system


def line():
    return '-' * 60


def title(message):
    print(line())
    print(f'|{message:^58}|')
    print(line())


def menu(*options):
    for index, option in enumerate(options):
        print(f'[ \033[0;33m{index + 1}\033[m ] - \033[0;33m{option}\033[m')
    print()
    print('Digite "\033[0;33mparar\033[m" para fechar o programa.')
    print(line())


def validate_user_input_options(inp):
    inp_options = inp.split(',')
    for op in inp_options:
        if len(op) > 1 or len(op) < 1:
            invalid_option(op)
            return False
        if op not in '12345':
            invalid_option(op)
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
            invalid_option()
            return False
    print(line())
    return True


def invalid_option(option=''):
    if option == '':
        print('\033[0;31mOpção inválida! Tente novamente...\033[m')
    else:
        print(
            f'\033[0;31m"{option}" é uma opção inválida! Tente novamente...\033[m')
    print(line())


def validate_user_input_save(inp):
    message = ''
    if inp in 's':
        message = 'Salvando...'
    elif inp in 'n':
        message = 'Finalizando...'
    else:
        invalid_option(inp)
        return False
    print(message)
    sleep(2)
    print(line())
    return True


def read_input_option(message):
    while True:
        user_option = str(input(message)).strip().lower()
        if user_option == 'parar':
            return False
        else:
            validate_option = validate_user_input_options(user_option)
            if validate_option:
                return True


while True:
    title("GERADOR DE DADOS ALEATÓRIOS")
    menu('Gerar nome', 'Gerar email', 'Gerar telefone',
         'Gerar cidade', 'Gerar estado')

    validate_option = read_input_option('Digite sua opção(ões): ')
    if validate_option == False:
        title('Saindo do sistema... até logo!')
        break

    validate_save = False
    while not validate_save:
        user_save_data = str(
            input('Deseja salvar os dados? [S/N] ')).strip().lower()[0]
        validate_save = validate_user_input_save(user_save_data)

    input('Pressione Enter para continuar...')
    system('cls')
