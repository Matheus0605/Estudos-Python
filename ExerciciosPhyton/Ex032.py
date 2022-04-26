year = int(input('Digite um ano (yyyy): '))

if year % 4 == 0 and year % 100 != 0 or year % 100 == 0:
    print(f'O ano {year} é BISSEXTO!')
else:
    print(f'O ano {year} não é BISSEXTO!')