from time import sleep
import sistema

pessoa = []

while True:

    print()
    sistema.menu()
    resp = int(input('Sua Opção: '))

    if resp == 3:

        print('Saindo do Sistema.. Até logo!')
        sleep(0.5)
        break

    elif resp == 1:

        print('-'*40)
        print('PESSOAS CADASTRADAS'.center(40))
        print('-'*40)
        sistema.opcao1(resp)

    elif resp == 2:

        print('-'*40)
        print('Cadastrar Pessoa'.center(40))
        print('-'*40)
        sistema.opcao2(resp)

    else:

        print('Digite um valor valido')

 

