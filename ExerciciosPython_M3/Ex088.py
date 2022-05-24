from random import randint
from time import sleep

matriz = []
colunas = []

num = int(input('Quantos jogos voce quer sortear? '))
print('-='*15)
print(f'Sorteando {num} JOGOS'.center(25))
print('-='*15)

for linha in range(num):

    for coluna in range(num):

        colunas.append(randint(1,60))
        
    colunas.sort()
    sleep(0.5)
    print(f'Jogo {linha+1}: {colunas}')
    matriz.append(colunas[:])
    colunas.clear()

print('-='*5, '< BOA SORTE >', '-='*5)
        