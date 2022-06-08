cadastro = {}
pessoa = []
mulheres = []
idade = 0

while True:

    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Sexo'] =  str(input('Sexo: [M/F] ')).upper()
    if cadastro['Sexo'] == 'F':

        mulheres.append(cadastro['Nome'])

    while cadastro['Sexo'] not in 'mMfF':

        print('De uma resposta valida!')
        cadastro['Sexo'] = str(input('Sexo: [M/F] ')).upper()

    cadastro['Idade'] = int(input('Idade: '))
    idade += cadastro['Idade']
    pessoa.append(cadastro.copy())

    resp = str(input('Quer continuar? [S/N] '))

    while resp not in 'nNsS':

        print('De uma resposta valida!')
        resp = str(input('Quer continuar? [S/N] '))

        if resp in 'nN':

            break
    
    if resp in 'nN':

            print('-='*30)
            break

media = idade / len(pessoa)
print('-='*30)
print(f'a) Total de pessoas cadastradas: {len(pessoa)}')  
print(f'b) A media de idade é de {media:.0f} anos') 
print(f'c) As mulheres cadastradas foram ', end=' ')
for v in mulheres:

        print(f'{v}',end=' ')
print(f'\nd) Lista das pessoas que estao acima da media:')
for c, v in enumerate(pessoa):

    if pessoa[c]['Idade'] > media:

        print(f'Nome = {pessoa[c]["Nome"]}; Sexo =  {pessoa[c]["Sexo"]}; Idade = {pessoa[c]["Idade"]}')