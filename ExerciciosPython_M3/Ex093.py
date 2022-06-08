jogador = {}
gols = list()
total = 0

jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Gols'] = list()
partidas = int(input('Quantas partidas {} jogou? '.format(jogador['Nome'])))
for v in range(partidas):
 
    gol = int(input(f'  Quanto gols na {v+1}° partida? '))
    total += gol
    gols.append(gol)
jogador['Gols'] = gols[:] 
jogador['Total'] = total

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():

    print(f'O campo {k} tem o valor valor {v}')

print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c, v in enumerate(gols):

    print(f' => Na partida {c+1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols')