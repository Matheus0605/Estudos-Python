from asyncio import sleep

jogador = {}
gols = list() 
equipe = list()
total = 0

while True:

    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas {} jogou? '.format(jogador['Nome'])))
    for v in range(partidas):
    
        gol = int(input(f'  Quanto gols na {v+1}° partida? '))
        gols.append(gol)
        
    jogador['Gols'] = gols[:] 
    jogador['Total'] = sum(gols)
    gols.clear()
    equipe.append(jogador.copy())    
    resp = str(input('Quer continuar? [S/N] ')).upper()

    if resp == 'N':

        print('-='*30)
        break

print(f'{"cod"} {"Nome":>4} {"Gols":>10} {"Total":>10}')
print('_'*30)
for k, v in enumerate(equipe):

    print(f"{k:>3} {equipe[k]['Nome']:>2}    {equipe[k]['Gols']} {equipe[k]['Total']:>4}")

print('_'*30)

while True: 

    mostra = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if mostra == 999:
        print('FINALIZANDO...')
        sleep(0.5)
        break

    if mostra >= len(equipe):

        print('Numero invalido. Tente Novamente.')
        print('_'*30) 

    else:

        print(f'  LEVANTAMENTO DO JOGADOR {equipe[mostra]["Nome"]}')                
        for i, g in enumerate(equipe[mostra]['Gols']):

            print(f'No jogo {i+1}fez {g} gols ')
                 
print('<<< Volte Sempre >>>')