cont = 'Ss'
media = 0
c = 0
soma = 0
maior = menor = 0


while cont in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    c += 1   
    if c == 1:
        maior = num
        menor = num 
    else:
        if num > maior:
            maior = num
        if num < menor :
            menor = num
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]   
media = soma / c
print(f'Voce digitou {c} numeros e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

