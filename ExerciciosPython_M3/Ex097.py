def line(msg):
    
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


line(msg = str(input('nome: ')))