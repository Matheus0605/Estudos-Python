while True:
    
    cont = 0

    num = int(input('Quer ver a tabuada de qual valor? '))
    if num > -1: 

        while cont <= 10:

            print(f'{num} x {cont} = {num * cont}')

            cont += 1

    else:
        
        break
    
print('Fim da Tabuada!')
