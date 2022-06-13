def leiaDinheiro(preco):
        
    valido = False
    

    while not valido:
        
        resp = str(input(preco)).replace(',', '.').strip()

        if resp.isalpha() or resp == '':

            print(f'ERRO! \"{resp}\" É UM PREÇO INVALIUDO')
        
        else:

            valido = True            

    return float(resp)