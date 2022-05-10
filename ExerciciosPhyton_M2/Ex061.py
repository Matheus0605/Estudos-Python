print('Gerando 10 termos de PA')
print('-='*15)
firstT = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
decimo = firstT + (10 - 1) * razao

print(firstT, end=' -> ')
while firstT < decimo:
    firstT += razao
    print(firstT, end=' -> ')
    
print('Fim!')
