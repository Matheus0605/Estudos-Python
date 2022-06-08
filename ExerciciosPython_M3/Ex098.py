from time import sleep


def contador():

    print('-='*20)
    print('Contagen de 1 até 10 de 1 em 1')
    for c in range(1,10):

        sleep(0.5)
        print(f'{c} ', end='',flush=True)
    print('FIM!')

    print('-='*20)
    print('Contagen de 10 até 0 de 2 em 2')
    for c in range(10,-1,-2):

        sleep(0.5)
        print(f'{c} ', end='',flush=True)
    print('FIM!')

    print('-='*20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio: '))
    final = int(input('Final: '))
    passo = int(input('Passo: '))
    for c in range(inicio, final, passo):

        sleep(0.5)
        print(f'{c} ', end='',flush=True)
    print('FIM!') 



contador()
