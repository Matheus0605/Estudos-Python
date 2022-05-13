from tkinter.tix import InputOnly


print('Procurando nome "SILVA"')
name = str(input('Digite seu nome completo: ')).strip().upper()
print('Seu nome tem "SILVA"? {}'.format('SILVA' in name))