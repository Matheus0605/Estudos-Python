divisivel = 0
num = int(input('Digite um numero: '))

for c in range(1, num + 1):
    
    if num % c == 0:
        divisivel += 1
        print(f'->{c}', end=' ')
    else:
         print(c, end=' ')
       
print(f'\nO numero {num} foi divisivel {divisivel} vezes')
if divisivel == 2:
    print('E por isso ele É PRIMO')
else: 
    print('E por isso ele NÃO É PRIMO')
