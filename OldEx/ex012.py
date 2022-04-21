#Minha solução
v = float(input('Qual o preço do produto? R$'))
d = (v * 0.05) - v
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(v, d))

#Solução Guanabara
v = float(input('Qual o preço do produto? R$'))
d = v- (v * 5 / 100)