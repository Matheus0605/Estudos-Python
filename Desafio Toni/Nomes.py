
PASTA = "Desafio Toni/nomes.txt"

with open(PASTA,"r", encoding="utf-8") as arquivo:

    lista_mulheres = []
    lista_homens = []
    lista = list()

    for linha in arquivo.readlines():

        nome = linha.replace('\n', '').split(";")
        lista.append(nome)

        if nome[3] in 'mM' :
            
            lista_homens.append(nome[0])

        elif nome[3] in 'fF':

            lista_mulheres.append(nome[0])
            

print(lista_mulheres)
print(lista_homens)        
