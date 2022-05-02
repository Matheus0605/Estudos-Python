produto = float(input('Qual o valor do produto? R$'))
desc = produto - (produto * 5 / 100)
print('O produto que custva R${:.2f}, com desconto de 5% vai custa R${:.2f}'.format(produto,desc))