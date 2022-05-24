dados = []
pessoas = []
maior_peso = menor_peso = peso = 0

while True:

    dados.append(str(input('Nome: ')).strip().upper())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()

    if peso == 0:

        maior_peso = menor_peso = dados[1]
        peso += 1

    if dados[1] > maior_peso:

        maior_peso = dados[1] 

    if dados[1] < menor_peso:

        menor_peso = dados[1]

    if resp in 'nN':

        break

    
    dados.clear()
   
print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for i, v in pessoas:

    if v == maior_peso:

        print(f'[{i}] ', end='')
    
print(f'\nO menor peso foi de {menor_peso}Kg. Peso de ', end='')
for i, v in pessoas:

    if v == menor_peso:

        print(f'[{i}] ', end='')
