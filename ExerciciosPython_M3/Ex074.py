from random import randint

num = randint(1,10)
num1 = randint(1,10)
num2 = randint(1,10)
num3 = randint(1,10)
num4 = randint(1,10)
tupla = (num, num1, num2, num3, num4)

print('Os valores sorteados foram: ', end='')

for c in tupla:

    print(c, end=' ')

print(f'\nO menor numero sorteado foi: {sorted(tupla)[0]}')
print (f'O maior numero sorteado foi: {sorted(tupla)[4]}')