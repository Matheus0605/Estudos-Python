dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
total = (60 * dia) + (0.15 * km)
print('O total a pagar é de {:.2f}'.format(total))