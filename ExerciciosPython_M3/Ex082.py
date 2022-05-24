num = []
impares = []
pares = []

while True:

    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()

    if resp in 'nN':

        break

for v in num:

    if v % 2 == 0:

        pares.append(v)

    else:

        impares.append(v)

print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')