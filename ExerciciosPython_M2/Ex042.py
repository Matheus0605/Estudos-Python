r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento acima PODE FORMAR um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')

    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')

    else:
        print('ISÓCELES!')

else:
    print('O segmento acima NÃO PODE FORMAR um triangulo')