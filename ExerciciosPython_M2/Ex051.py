print('='*40)
print('10 TERMOS DE UMA PA')
print('='*40)
firstT = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = firstT + (10 - 1) * razao

for c in range(firstT, decimo + razao, razao):
    print(c, end=' -> ')
print('Acabou')