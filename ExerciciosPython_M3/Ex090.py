alunos = {}

alunos['Nome'] = str(input('Nome: '))
alunos['Media'] = float(input('Média de {}: '.format(alunos['Nome'])))

if alunos['Media'] < 5.0:

    alunos['Situaçao'] = 'Reprovado'

elif alunos['Media'] >= 5.0 and alunos['Media'] < 7.0:

    alunos['Situaçao'] = 'Recuperção'

else:

    alunos['Situaçao'] = 'Aprovado'

print('-='*25)
for k , v in alunos.items():

    print(f' - {k} é igual {v}')
print()
