from operator import index


num = int(input('Digite um numero: '))
num1 = int(input('Digite outro numero: '))
num2 = int(input('Digite mais um numero: '))
num3 = int(input('Digite o ultimo numero: '))

tupla = (num, num1, num2, num3)

nove = 0

print(f'Voce digitou os numeros {tupla}')

for c in tupla:
    if c == 9:
        nove += 1

print(f'O valor 9 aparece {nove} vez/vezes')

if 3 in tupla:

    print(f'O valor 3 tres esta na {tupla.index(3)+1}° posição')
    
else:  

    print(f'O valor 3 nao foi digitado em nenhuma posição')
    
print('Os valores pares digitados foram ', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
