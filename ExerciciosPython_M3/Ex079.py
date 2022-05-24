valores = []
while True:

    valor = int(input('Digite um valor: '))

    if valor in valores:

        print('Valor duplicado! Nao vou adicionar')
    
    else:

        valores.append(valor)
    cont = str(input('Quer continuar? [S/N] '))

    if cont in 'nN':

        print('='*25)
        break

valores.sort()
print(f'Voce digitou os valores {valores}')
