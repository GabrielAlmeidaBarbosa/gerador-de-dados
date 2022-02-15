from lib.data import *
from time import sleep
from random import choice


# Funções de texto
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


# Funções de leitura de entrada do usuário
def read_input_option(message):
    while True:
        user_option = str(input(message)).strip().lower()
        if user_option == 'parar':
            return False
        else:
            validate_option = validate_user_input_options(user_option)
            if validate_option != False:
                return validate_option


def read_input_save(message, data):
    for k, v in data.items():
        sleep(1)
        print(f'{k}: {v}')

    print(line())
    while True:
        save = str(input(message)).strip().lower()[0]
        if save in 's':
            print('\033[0;33mSalvando dados...\033[m')
            print()
            status = save_data(data)
            sleep(1)

            if status:
                print('\033[0;32mDados salvos com sucesso!\033[m')
            else:
                print('\033[0;31mErro ao salvar dados.\033[m')

            print()
            sleep(1)
            break
        elif save in 'n':
            print('Você escolheu \033[0;33mnão salvar\033[m!')
            print()
            sleep(1)
            break
        else:
            invalid_option(save)


def validate_user_input_options(inp):
    inp_options = inp.split(',')
    for op in inp_options:
        if len(op) > 1 or len(op) < 1:
            invalid_option(op)
            return False
        if op not in '12345':
            invalid_option(op)
            return False

    data = {}
    for op in inp_options:
        if op == '1':
            data['name'] = choice(names)
        elif op == '2':
            data['email'] = choice(emails)
        elif op == '3':
            data['phone'] = choice(phones)
        elif op == '4':
            data['city'] = choice(citys)
        elif op == '5':
            data['state'] = choice(states)
        else:
            invalid_option(op)
            return False
    return data


# Salvar dados gerados
def save_data(data):
    try:
        archive = open('data.txt', 'a')
        archive.write(f'{data}\n')
        archive.close()
        return True
    except:
        return False


# Função de alerta de opção inválida.
def invalid_option(option=''):
    if option == '':
        print('\033[0;31mOpção inválida! Tente novamente...\033[m')
    else:
        print(
            f'\033[0;31m"{option}" é uma opção inválida! Tente novamente...\033[m')
    print(line())
