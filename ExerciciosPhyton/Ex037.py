num = int(input('Digite um numero inteiro: '))
print('Escolha uma das opções')
print('[1] Converter para BINÁRIA')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
escolha = int(input('Opção: '))

if escolha == 1:
    print(f'{num} em Binario é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} em Octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} em Hexadecimal é {hex(num)[2:]}')
else:
    print('Essa opção nao existe')