import datetime

dia = datetime.datetime.today().weekday()

def dias():
    print('De acordo com a data de hoje você deve: ')
    tarefas = ['Lavar louça','estudar ingles','treinar','estudar python','jogar','acordar cedo','folga']
    for x in range(0,7) :
        if x == dia :
            print(tarefas[x])

dias()
print('Deseja alterar alguma tarefa ?')
alterar = input()



# Definir horas
def horas():
    from datetime import date
    data_atual = date.today()
    print(data_atual)
    print('\n')


input('Aperte qualquer tecla')


def alterardata():
    print('Insira a data que deseja a nova Atividade(sendo 0 segunda & domingo 6)')
    mudar = int(input(':'))
    atv = input('Digite A atividade:')
    for x in range(0,7) :
        if x == mudar :
            tarefas[x] = str(atv)
            print(tarefas)