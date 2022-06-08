from time import sleep


medias = []
aluno = []

while True:

    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    media = (aluno[1] + aluno[2]) / 2
    aluno.append(media)
    medias.append(aluno[:])
    aluno.clear()
    resp = str(input('Quer continuar? [S/N] '))

    if resp in 'nN':
        print('-='*30)
        break

print(f'{"N°.":<4} {"Nome":<10}{"Media":>8}')
print('_'*25)
for num, linha in enumerate(medias):

    print(f'{num:<4} {linha[0]:<10} {linha[3]:>7.1f}')

print('_'*25)
while True: 

    mostra = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostra == 999:
        print('FINALIZANDO...')
        sleep(0.5)
        print('<<< Volte Sempre >>>')
        break

    if mostra <= len(medias) :

        for linha in medias:

            if  medias[mostra] == linha:

                print(f'Notas de {linha[0]} sao [{linha[1]:.1f}, {linha[2]:.1f}]')
                print('_'*25)
                break
    
    else: 

        print('Numero invalido') 
        print('_'*25)  