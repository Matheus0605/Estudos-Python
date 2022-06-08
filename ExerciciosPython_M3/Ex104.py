def leiaInt(numero):
    
    fim = False
    valor = 0
    while True:
        
        resp = input(numero)
        if resp.isnumeric():

            valor = int(resp)
            fim = True
        
        else:

            print('ERROR!')

        if fim:

            break            

    return valor    

num = leiaInt('Digite um numero: ')
print(f'Voce acabdou de digitar o numero {num}')