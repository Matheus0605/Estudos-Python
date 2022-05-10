'''import math'''

num = int(input('Digite um numero para\ncalcular seu Fatorial: '))
c = num
fatorial = 1
print(f'Calculando {num}!: ',end='')
while c > 0:
    if c > 1:
        print(c,end=' x ')
    else:
        print(c, end=' = ')
    fatorial *= c
    c -= 1
print(fatorial)

'''
while c > 0 :
    if c != 1:
        print(c,end=' x ')
    else:
        print(c, end=' = ')
    c -= 1
print(math.factorial(num))'''

