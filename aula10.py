#Condição Simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Matheus':
    print('Que nome lindo voce tem! ')
print('Bom dia, {}!'.format(nome))

#Condição Composta
nome = str(input('Qual é o seu nome? '))
if nome == 'Matheus':
    print('Que nome lindo voce tem! ')
else:
    print('Seu nome é tao normal!')
print('Bom dia, {}!'.format(nome))
