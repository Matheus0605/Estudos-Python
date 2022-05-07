soma = 0
num = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        num += 1
print(f'A soma dos {num} numeros fica {soma}')