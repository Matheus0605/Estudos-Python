numeros = []

while True:

    num = int(input('Digite um valor: '))
    numeros.append(num)
    resp = str(input('Quer continuar: [S/N]')).strip().upper()

    if resp in 'N':

        break

print(f'Voce digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os numeros em ordem decrescente {numeros}')

if 5 in numeros:

    print('O valor 5 FAZ parte da lista')

else:

    print('O valor 5 NÃO faz parte da lista')