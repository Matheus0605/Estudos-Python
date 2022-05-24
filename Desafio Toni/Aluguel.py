PAHT = "Desafio Toni/aluguel.txt"

with open(PAHT, "r", encoding="utf-8") as arquivo:

    lista = []
    
    for linha in arquivo.readlines():

        nome = linha.replace('\n', '').split()
        lista.append(nome)

        

print(lista)