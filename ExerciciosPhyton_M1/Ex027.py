name = str(input('Digite seu nome completo: ')).strip().split()
print('É um prazer te conhecer!')
print(f'Seu primeiro nome é {name[0]}')
print(f'E seu ultimo nome é {name[len(name)-1]}')