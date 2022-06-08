def terreno(larg, comp):

    area = larg * comp 
    print(f'A área de um terreno é {larg:.1f}x{comp:.1f} é de {area:.1f}m²')

print('Controle de Terronos'.center(25))
print('_'*25)
larg = float(input('Largura (m):'))
comp = float(input('Comprimento (m): '))
terreno(larg, comp)