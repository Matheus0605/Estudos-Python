
PASTA = "Desafio Toni/nomes.txt"


with open(PASTA,"r", encoding="utf-8") as arquivo:

    abrir = arquivo.read()

    print(abrir)

with open(PASTA,"r", encoding="utf-8") as arquivo:

    lista = list()

    for linha in arquivo.readlines():

        nome = linha.replace('\n', '').split(";")
        lista.append(nome)

        if nome[3] not in 'mM' :

            print('1')

        else:
            
            print('2')

        print(nome) 
        
print(lista) 



'''nome = str(input('Quem procura? '))
with open(PASTA,"r", encoding="utf-8") as arquivo:  
    for linha in arquivo.readlines():
        if nome == linha.split(';')[0]: 
            print(linha)'''