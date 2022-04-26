import random

number = int(input('Estou pensando em um numero!\nAdivinhe qual: '))
pc = random.randint(0,5)

if pc == number:
    print('Acertou!')
    print('Joguemos novamente!')
else:
    print(f'Errou! pensei em {pc}')
    print('Tente Novamente!')