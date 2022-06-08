def jogador(nome='<desconhecido>', gols=0):

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
        
n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))

if g.isnumeric():
    
    g = int(g)

else:   

    g = 0

if n.strip() == '':

    jogador(gols=g)

else:

    jogador(n, g)

