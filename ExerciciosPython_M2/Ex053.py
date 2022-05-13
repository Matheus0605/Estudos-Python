frase = str(input('Digite uma frase: ')).lower().strip()
separar = frase.split()
junto = ''.join(separar)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'{frase} ////// {frase[::-1]}')
if inverso == junto:
    print('Polindromo')
else:
    print('Nao é Palindromo')