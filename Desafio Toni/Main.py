'''with open("Desafio Toni/nomes.txt","r", encoding="utf-8") as arquivo:
    abrir = arquivo.read()
    print(abrir)'''
nome = str(input('Quem procura? '))
with open("Desafio Toni/nomes.txt","r", encoding="utf-8") as arquivo:  
    for linha in arquivo.readlines():
        print(type(linha), linha)
        print(linha.split(";"))
        print(linha.split(";")[0])
        if nome == linha.split(';')[0]: 
            print(linha)

'''with open("Desafio Toni/nomes.txt","r", encoding="utf-8") as arquivo:
    for linha in arquivo.readlines():
        nome = linha.split(";")
        print(nome[0])'''