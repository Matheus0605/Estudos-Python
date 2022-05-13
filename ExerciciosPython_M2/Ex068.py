import random
print('-='*25)
print('PAR OU IMPAR (GAME)'.center(50))
print('-='*25)

vitoria = 0
while True:

    pc = random.randint(1,10)
    jogador = int(input('Digite um valor: '))
    par_ou_impar = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print('-'*50)
    total = pc + jogador
    print(f'Voce jogou {jogador} e o computador {pc}. ', end='')

    if par_ou_impar == 'I':

        if total % 2 == 0:

            print(f'Total de {total}  DEU PAR ')
            print('-'*50)
            print('Voce PERDEU!')
            print('-='*25) 
            
            break

        else:

            print(f'Total de {total} DEU IMPAR')
            print('-'*50)
            print('Voce GANHOU!')
            print('Vamos jogar novamente..')
            print('-='*25)
            vitoria += 1

    elif par_ou_impar == 'P':

        if total % 2 == 0:

            print(f'Total de {total}  DEU PAR ')
            print('-'*50)
            print('Voce GANHOU!') 
            print('Vamos jogar novamente..') 
            print('-='*25)
            vitoria +=1 

        else:

            print(f'Total de {total} DEU IMPAR')
            print('-'*50)
            print('Voce PERDEU!')
            print('-='*25)
            
            break
print(f'GAMER OVER! Você venceu {vitoria} vezes.')