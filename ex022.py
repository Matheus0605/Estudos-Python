import pygame
nome = input('Digite seu nome completo: ')
print('Seu nome em maiusculo é', nome.upper())
print('Seu nome em minusculo é', nome.lower())
print('Seu nome tem ao todo', len(nome.strip()),'letras')
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {}'.format(separa[0], len(separa[0])))