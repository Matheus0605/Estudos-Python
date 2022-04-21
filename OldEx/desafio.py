valor = int(input('Qual valor do produto? '))
p1 = int(input('Quanto de desconto quer aplicar? '))
resultado = valor - (valor * p1 / 100)
print('O valor do prduto de {:.2f} com desconto de {}% ficara {:.2f}'.format(valor,p1,resultado))
