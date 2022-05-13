for c in range(1,6):
    peso = float(input(f'Peso da {c}° Pessoa: '))
    if c == 1:
        maiorP = peso
        menorP = peso

    if peso > maiorP:
        maiorP = peso

    if peso < menorP:
        menorP = peso
print('O maior peso foi {:.1f}\nE o menor peso foi {:.1f}'.format(maiorP, menorP))