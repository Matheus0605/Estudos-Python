import random

pc = random.randint(0,10)
print(pc)
player = int(input('Descubra em que numero estou pensando\nDigite o numero: '))
chances = 5

while True:
    player = int(input('Tente novamente: ')) 
    if player == pc:
        print('Voce acertou')
        print(f'Pensei em {pc}')
        break
    if chances == 0:
        print('Suas chances acabaram')
        break
    print('Voce errou')
    print(f'Vidas restantes: {chances}') 
    chances -= 1


