reta1 = int(input('Primeira reta: '))
reta2 = int(input('Segunda reta: '))
reta3 = int(input('Terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Formam um triangulo!')
else:
    print('NÃO formam um triangulo!')