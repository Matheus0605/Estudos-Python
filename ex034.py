#Minha Soluçao
salario = float(input('Qual é o salário do funcionario? R$ '))
p = salario + (salario * 10 / 100)
p2 = salario + (salario * 15 / 100)
if (salario >= 1250) / 10:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,p))
else:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario,p2))


#Soluçao Guanabara
salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100 )
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))