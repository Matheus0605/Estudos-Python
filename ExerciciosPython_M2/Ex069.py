maior_18 = man = woman = 0
while True:

    print('-'*25)
    print('CADASTRE UMA PESSOA'.center(25))
    print('-'*25)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-'*25)
    
    if idade >= 18 :

        maior_18 += 1
    
    if sexo == 'M':

        man += 1

    if idade < 20 and sexo == 'F':

        woman += 1

    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if cont == 'N':

        break
    
print(f'Total de pessoas com mais de 18 anos: {maior_18}')
print(f'Ao todo temos {man} homens cadastrados')
print(f'E temos {woman} mulheres com menos 20 anos')