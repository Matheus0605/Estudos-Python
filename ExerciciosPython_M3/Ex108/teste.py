import moeda

p = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(p)} é R$ {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentanddo 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
