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


def validate_user_input(inp):
    if inp == 'parar':
        return True

    inp_options = inp.split(',')
    for op in inp_options:
        if len(op) > 1:
            print('\033[0;31mOpção inválida! Tente novamente...\033[m')
            return False
        if op not in '12345':
            print('\033[0;31mOpção inválida! Tente novamente...\033[m')
            return False

    for op in inp_options:
        if op == '1':
            print('Escolheu a opção 1')
        elif op == '2':
            print('Escolheu a opção 2')
        elif op == '3':
            print('Escolheu a opção 3')
        elif op == '4':
            print('Escolheu a opção 4')
        elif op == '5':
            print('Escolheu a opção 5')
        else:
            print('\033[0;31mOpção inválida! Tente novamente...\033[m')
            return False
    return True


title("GERADOR DE DADOS ALEATÓRIOS")
menu('Gerar nome', 'Gerar email', 'Gerar telefone',
     'Gerar cidade', 'Gerar estado')
while True:
    user_option = str(input('Digite sua opção: ')).strip().lower()
    validate = validate_user_input(user_option)
    if validate == True:
        title("Saindo do sistema... até logo!")
        break
