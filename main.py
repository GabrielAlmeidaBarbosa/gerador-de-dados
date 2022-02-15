from lib import *
from os import system

try:
    while True:
        title("GERADOR DE DADOS ALEATÓRIOS")
        menu('Gerar nome', 'Gerar email', 'Gerar telefone',
             'Gerar cidade', 'Gerar estado')

        validate_option = read_input_option('Digite sua opção(ões): ')
        if validate_option == False:
            title('Saindo do programa... até logo!')
            break

        print()
        read_input_save(
            'Deseja salvar os dados? [\033[0;33mS\033[m/\033[0;33mN\033[m] ', validate_option)

        resp = input(
            'Pressione \033[0;32mEnter\033[m para continuar ou\nDigite "\033[0;33mparar\033[m" para fechar o programa. ')
        if resp == 'parar':
            title('Saindo do programa... até logo!')
            break
        else:
            system('cls')
except KeyboardInterrupt:
    print()
    title('Saindo do programa... até logo!')
