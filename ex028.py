from random import randint
from time import sleep
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
n = int(input('Em que numero eu pensei? '))
print('Processando...')
sleep(2)
num = randint(0,5)
if n == num:
    print('Parabens! Voce conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no numero {} e nao no {}'.format(num,n))