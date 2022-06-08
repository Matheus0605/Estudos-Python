from random import randint

num1 = randint(1,6)
num2 = randint(1,6)
num3 = randint(1,6)
num4 = randint(1,6)
numeros = {'Jogador1': num1, 'Jogador2': num2, 'Jogador3': num3, 'Jogador4': num4}
rankig = []
rankig = list(numeros.values())
rankig.sort(reverse=True)   

print(rankig)
