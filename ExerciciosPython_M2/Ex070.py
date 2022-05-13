print('-'*25)
print('LOJAO'.center(25))
print('-'*25)
contador = 1
soma = maior_prod = menor_prod = 0
nome_prod = ''
while True:

    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$ '))
    soma += preco

    if contador == 1:

        menor_prod = preco
        nome_prod = produto
        contador += 1

    if preco > 1000:

        maior_prod += 1

    if preco < menor_prod:

        nome_prod = produto
        menor_prod = preco
        

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    if cont == 'N':

        break
print('---------- FIM DO PROGRAM ----------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maior_prod} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_prod} que custa R${menor_prod:.2f}')