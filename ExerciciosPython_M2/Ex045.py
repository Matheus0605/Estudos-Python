import random

pc = random.randint(1,3)
print('[1]Pedra\n[2]Papel\n[3]Tesoura')
player = int(input('Escolha: '))

if pc == 1:
    if player == 1:
       print('Empate')
    elif player == 2:
        print('Jogador Ganhou!')
    elif player == 3:
        print('Pc Ganhou!')
    else:
        print('Jogada Invalida')

if pc == 2:
    if player == 2:
       print('Empate')
    elif player == 3:
        print('Jogador Ganhou!')
    elif player == 1:
        print('Pc Ganhou!')
    else:
        print('Jogada Invalida')

if pc == 3:
    if player == 3:
       print('Empate')
    elif player == 1:
        print('Jogador Ganhou!')
    elif player == 2:
        print('Pc Ganhou!')
    else:
        print('Jogada Invalida')