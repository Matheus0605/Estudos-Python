from datetime import datetime
maiorIdade = 0
menorIdade = 0

for c in range(1, 8):
    year = int(input(f'{c}° Ano de nascimento: '))
    idade = datetime.today().year - year
    if idade > 18:
        maiorIdade += 1
    else:
        menorIdade += 1

print(f'Temos ao todo {maiorIdade} pessoas maiores de Idade')
print(f'E {menorIdade} pessoas menor de Idade')