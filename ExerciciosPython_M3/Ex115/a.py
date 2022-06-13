import os
if os.path.isfile('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt'):

    with open('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt', mode='r', encoding='utf-8') as arquivo:
        
        if arquivo == '':

            print('0 PESSOAS CADASTRADAS')

        else:

            
            print('-'*30)
            print('PESSOAS CADASTRADAS'.center(30))
            print('-'*30)
            

            for v in arquivo:
                print(v)
            

else:

    with open('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt', mode='w', encoding='utf-8') as arquivo:
        
        print(arquivo)
