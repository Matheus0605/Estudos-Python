from time import sleep


def ajuda():

    while True:
        
        print('~'*25)
        print('SISTEMA DE AJUDA PyHELP'.center(25))
        print('~'*25)

        msg = str(input('Função ou Biblioteca > '))

        if msg in 'FIMfim':

            print('FINALIZANDO')
            sleep(0.3)
            break

        else:

            if msg not in  'FIMfim':

                sleep(0.3)

                print('~'*40)
                print(f' Acessando o manule do comando {msg}'.center(20))
                print('~'*40)

                sleep(0.3)                    
                help(msg)  
    
ajuda()