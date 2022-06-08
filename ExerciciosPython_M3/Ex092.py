from datetime import datetime

trabalhadores = {}
ano = datetime.now().year

trabalhadores['Nome'] = str(input('Nome: '))
trabalhadores['Idade'] = int(input('Ano de Nascimento: '))
trabalhadores['Idade'] = ano - trabalhadores['Idade']
trabalhadores['NumeroCtps'] = int(input('Carteira de Trabalho (0 nao tem): '))

if trabalhadores['NumeroCtps'] == 0:

        print('-='*30)
        for k, v in trabalhadores.items():

            print(f' - {k} tem o valor {v}')

else:

    trabalhadores['Contrataçao'] = int(input('Ano de Contratação: '))
    trabalhadores['Salario'] = float(input('Salário: R$'))
    trabalhadores['Aposentadoria'] = trabalhadores['Idade'] + ((trabalhadores['Contrataçao'] + 30) - datetime.now().year)
    print('-='*30)
    for k, v in trabalhadores.items():

        print(f' - {k} tem o valor {v}')


