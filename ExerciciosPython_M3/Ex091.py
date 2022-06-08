from operator import itemgetter
from random import randint
from time import sleep

num1 = randint(1,6)
num2 = randint(1,6)
num3 = randint(1,6)
num4 = randint(1,6)
numeros = {'Jogador1': num1, 'Jogador2': num2, 'Jogador3': num3, 'Jogador4': num4}
ranking = list()

print('Valores sorteados no dado: ')
for k, v in numeros.items():

    print(f'{k} tirou {v:>1} no dado.')
    sleep(1)

ranking = sorted(numeros.items(), key=itemgetter(1), reverse=True)

print('-='*30)
print('== RANK ==')
for i , v in enumerate(ranking):

    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)


