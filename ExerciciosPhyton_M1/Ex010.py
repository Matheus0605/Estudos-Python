reais = float(input('Quantos dinheiro você tem na carteira? R$'))
dolar = reais / 3.27
print('Com R${:.2f} você pode comprar U${:.2f}'.format(reais, dolar))