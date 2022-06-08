from datetime import datetime

def votar(resp):

    if resp <= 16:

        return f'Com {resp} anos: Nao Vota'

    else:

        if resp <= 18 :

            return f'Com {resp} anos: Voto OPCIONAL!'
        
        else:

            return f'Com {resp} anos: Voto OBRIGATORIO!'

    


anoAt = datetime.today().year
anoNasc = int(input('Em que ano voce nasceu? '))
idade = anoAt - anoNasc
votar(idade)