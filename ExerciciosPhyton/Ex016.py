'''Metodo #1'''
import math
num = float(input('Digite um numero: '))
print('O valor digitado foi de {} e sua porção inteira é {}'.format(num, math.trunc(num)))

'''Metodo #2'''
num = float(input('Digite um numero: '))
print('O valor digitado foi de {} e sua porção inteira é {}'.format(num, int(num)))