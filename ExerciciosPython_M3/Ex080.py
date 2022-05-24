valores = []
for c in range(0,5):

    num = int(input('Digite um valor: '))

    if c == 0 or num > valores[-1]:

        valores.append(num)
        print('Adicionaod no final da lista')

    else:
        
        pos = 0
        while pos < len(valores):
            
            if num <= valores[pos]:

                valores.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break

            pos +=1



print(valores)