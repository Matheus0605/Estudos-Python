tupla = (('Lápis', 1.75), ('Borracha', 2.00), ('Caderno', 15.90), ('Estoujo', 25.00), ('Transferidor', 4.20), ('Compasso', 9.99), ('Mochila', 120.32), ('Canetas', 22.30), ('Livro', 34.90))

print('='*50)
print('Lista de Preço'.center(50))
print('='*50)

for c in tupla:
    print(f'{c[0]:.<30}', end='')
    print(f'R$ {c[1]:>7.2f}')

