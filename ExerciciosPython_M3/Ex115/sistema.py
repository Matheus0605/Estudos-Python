def menu():

    print('-'*40)
    print('MENU PRINCIPAL'.center(40))
    print('-'*40)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do Sistema')
    print('-'*40)

def opcao1(msg):

    import os
    if os.path.isfile('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt'):

        with open('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt', mode='r', encoding='utf-8') as arquivo:

            pessoa = []

            for v in arquivo:
                
                nome = v.replace('\n', '').split(';')
                pessoa.append(nome)
                print(f'{nome[0]:<30} {nome[1]:>3} anos')
     

    else:

        with open('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt', mode='w', encoding='utf-8') as arquivo:
            
            pass


    return arquivo

def opcao2(msg):

    with open('C:/Users/mathe/OneDrive/Documentos/Meus Projetos/Estudos-Python/ExerciciosPython_M3/Ex115/valor.txt', mode='a', encoding='utf-8') as arquivo:

        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        arquivo.write(str(f'{nome};{idade}') + '\n')
        print(f'{nome} de {idade} anos, resgitrada com sucesso')

    return msg 