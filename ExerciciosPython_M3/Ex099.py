from time import sleep


def analisa(*numeros):

    cont = maior = 0
    print('-='*30)
    print('Analisando os valores...')
    for v in numeros:

        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:

            maior = v

        else:
            if v > maior:

                maior = v

        cont += 1

    
    print(f'Foram informados {len(numeros)} valores ao todo')
    print(f'O maior numero valor foi {maior}')

analisa(2,9,4,5,7,1)
analisa(4,7,0)
analisa(1,2)
analisa(6)
analisa()