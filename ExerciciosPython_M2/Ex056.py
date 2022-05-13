maiorIdade = 0
media = 0
woman = 0
for c in range(1,5):
    print(f'-------- {c}° Pessoa --------')
    name = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M\F]: ')).strip().upper()
    media += idade
    if idade > maiorIdade:
        maiorIdade = idade
        nomeVelho = name

    if sexo == 'F' and idade < 20:
        woman += 1

media /= 4 
print(f'A media de idade do grupo é de {media} anos')
print(f'O homen mais velho tem {maiorIdade} e se chama {nomeVelho}')
print(f'Ao todo sao {woman} mulheres com menos de 20 anos')
