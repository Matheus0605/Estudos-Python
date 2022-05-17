
from ast import Num


tupla = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


while True:

    num = int(input('Digite um numero entre 0 e 20: '))

    if num < 0 or num > 20:

        print('Numero invalido. Tente Novamente')

    else:

        break
    
print(f'Voce digitou {num} e por extenso {tupla[num]}')