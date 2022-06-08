from random import randint

def soma(num):

    soma = 0
    print(f'Somando os valores pares de {num}, temos ', end='')
    for v in num:

        if v % 2 == 0:

            soma += v
    print(soma)


def sorteio():

    numeros = []
    print('Sorteando 5 valores da lista: ',end='')
    for v in range(1,6):

        numeros.append(randint(1,10))
    
    for v in numeros:

        print(f'{v} ', end='')
    
    print('PRONTO!')
    soma(numeros)
sorteio()



