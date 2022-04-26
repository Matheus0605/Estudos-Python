number = int(input('Digite um numero: '))
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))