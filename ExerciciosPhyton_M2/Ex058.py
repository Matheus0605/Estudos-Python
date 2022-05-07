import random
tentativas = 1
jogar_ou_nao = str(input('Vamos jogar? [S/N]')).strip().upper()
if jogar_ou_nao == 'S':
    pc = random.randint(0,10)
    print('Estou pensando em um numero entre 0 e 10.')
    player = int(input('De seu palpite: '))
    while player != pc:
        if player < pc:
            print('Mais... Tente Novamente! ')
            player = int(input('De seu palpite: '))
        elif player > pc:
             print('Menos... Tente Novamente! ')
             player = int(input('De seu palpite: '))
        tentativas += 1
    else:
        print(f'Acertou! Pensei em {pc}')
else:
    print('OK! Aproveite seu tempo!')
print(f'Acertou com {tentativas} tentativas')