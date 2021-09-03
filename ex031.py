#Minha soluçao
n = float(input('Qual a distancia da viagem em Km? '))
resultado = n * 0.50
r2 = n * 0.45
if n < 200:
    print('O preço da sua passagem será R${:.2f}'.format(resultado))
else:
    print('O preço da sua viagem será R${:.2f}'.format(r2))


#Soluçao Guanabara
distancia = float(input('Qual é a distancia da sua viagem'))
print('Voce está preste a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))