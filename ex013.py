#Minha solução
salario = float(input('Qual é o salário do fúncionário? R$'))
aumento = salario + (salario * 15 / 100)
print('Umfuncionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))