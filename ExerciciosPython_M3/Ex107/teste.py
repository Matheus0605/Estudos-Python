import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {p} é R$ {moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentanddo 10%, temos R${moeda.aumentar(p, 10)}')
