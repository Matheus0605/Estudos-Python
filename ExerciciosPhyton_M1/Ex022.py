from unicodedata import name


nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiusculo fica {}'.format(nome.upper()))
print('Seu nome em minusculo fica {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
dividir = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(dividir[0],len(dividir[0])))