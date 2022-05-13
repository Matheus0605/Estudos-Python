import time
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:
    time.sleep(1)
    print('-='*10)
    print('[1] Somar\n[2] Mutiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    escolha = int(input('Faça sua escolha: '))
    if escolha == 1:
        total = num1 + num2
        print(f'A soma entre {num1} e {num2} é {total}')
    
    elif escolha == 2:
        total = num1 * num2
        print(f'Mutiplicando {num1} por {num2} da {total}')

    elif escolha == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'O maior número entre {num1} e {num2}  é {maior}')

    elif escolha == 4:
        print('Informe os números novamente')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))

    elif escolha > 5:
        print('Numero invalido. Digite novamente')    
print('Saindo....')
time.sleep(1)
print('Programa finalizado!')