matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
total = 0
coluna3 = 0

for l in range(0,3):

    for c in range(0,3):

        matriz[l][c] = int(input(f'Valor [{l}, {c}]:'))
            
        if matriz[l][c] % 2 == 0:

            total += matriz[l][c]
            
        if matriz[l][c] == matriz[l][2]:

            coluna3 += matriz[l][2]

print('='*30)
for l in range(0,3):

    for c in range(0,3):
        
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    
if matriz[1][0] >= 0:

    maior = matriz[1][0]

if matriz[1][1] > maior:

    maior = matriz[1][1]

if matriz[1][2] > maior:

    maior = matriz[1][2]

'''for linha in range(3):

    for coluna in range(3):

        if matriz[1][0] >= 0:

            maior = matriz[1][0]

        if matriz[1][coluna] > maior:

            maior = matriz[1][coluna]'''
           

print('='*30)
print(f'A soma dos valores  pares é {total}')
print(f'A soma dos valores da terceira coluna é {coluna3}')
print(f'O maior valor da segunda linha é {maior}')