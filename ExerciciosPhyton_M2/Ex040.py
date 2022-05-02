'''– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média do aluno é {media}')
if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!') 